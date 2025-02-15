---
icon: dot
label: 'Create modules'
order: 50
---

Modules are stored in `vm->_modules` and `vm->_lazy_modules`.
They are both dict-like objects.

### Lazy modules

A lazy module is a python source file.
It is compiled and executed when it is imported.
Use `[]` operator to add a lazy module.

```cpp
vm->_lazy_modules["test"] = "pi = 3.14";
```

```python
import test
print(test.pi)  # 3.14
```

### Native modules

A native module is a module written in c++ or mixed c++/python.
Native modules are always compiled and executed when the VM is created.

To creata a native module,
use `vm->new_module(...)`.

```cpp
PyObject* mod = vm->new_module("test");
mod->attr().set("pi", VAR(3.14));

vm->bind_func<2>(mod, "add", [](VM* vm, ArgsView args){
    i64 a = CAST(i64, args[0]);
    i64 b = CAST(i64, args[1]);
    return VAR(a + b);
});
```

```python
import test
print(test.pi)  # 3.14
print(test.add(1, 2))  # 3
```

### Module resolution order

When you do `import` a module, the VM will try to find it in the following order:

1. Search `vm->_modules`, if found, return it.
2. Search `vm->_lazy_modules`, if found, compile and execute it, then return it.
3. Search the working directory and try to load it from file system via `read_file_cwd`.


### Filesystem hook

You can use `set_read_file_cwd` to provide a custom filesystem hook, which is used for `import` (3rd step).
The default implementation is:

```cpp
set_read_file_cwd([](const Str& name){
    std::filesystem::path path(name.sv());
    bool exists = std::filesystem::exists(path);
    if(!exists) return Bytes();
    std::string cname = name.str();
    FILE* fp = fopen(cname.c_str(), "rb");
    if(!fp) return Bytes();
    fseek(fp, 0, SEEK_END);
    std::vector<char> buffer(ftell(fp));
    fseek(fp, 0, SEEK_SET);
    fread(buffer.data(), 1, buffer.size(), fp);
    fclose(fp);
    return Bytes(std::move(buffer));
});
```