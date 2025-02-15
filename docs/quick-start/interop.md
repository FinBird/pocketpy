---
icon: dot
label: 'Interop with PyObject'
order: 90
---

In pkpy, any python object is represented by a `PyObject*`.


### Create `PyObject*` from C type

A set of overloaded function `PyObject* py_var(VM* vm, ...)` were implemented to
create a `PyObject*` from a supported C type.
In order to make it less verbose, we usually use macro `VAR(...)`, which is just a wrapper of `py_var`.

For example, create a python `int` object from a C `i64` type:

```cpp
i64 i = 2;
PyObject* obj = VAR(i);
```

Each python type has a corresponding C type, for example, `int` in python is `i64` in C.
python's `list` corresponds to `List`, `str` corresponds to `Str`, etc.
For strings, we have defined
a set of overloaded version including `const char*`, `std::string`, `std::string_view`, `Str`, etc.

```cpp
PyObject* obj = VAR("abc");		// create a python str object
```

A more complex example is to create a python `list`.
In the following code, we create a `list` equals to `[0, 1, 2, 3]`.

```cpp
List list;
for (i64 i = 0; i < 4; i++) {
    list.push_back(VAR(i));
}

obj = VAR(std::move(list));		// create a python list object
```

Please note that `std::move` is used here to avoid unnecessary copy.
Most types have both a rvalue and a lvalue version of `VAR` function.

### Access internal C type of `PyObject*`

A set of template function `T py_cast<T>(VM* vm, PyObject* obj)` were implemented
for each supported C type. We usually use macro `CAST(T, ...)` to make it less verbose.

```cpp
i64 i = 2;
PyObject* obj = VAR(i);

// cast a PyObject* to C i64
i64 j = CAST(i64, obj);		
```

The `CAST` function will check the type of `obj` before casting.
If the type is not matched, a `TypeError` will be thrown.

However, this type check has a cost. If you are sure about the type of `obj`,
you can use the underscore version `_CAST` to skip the type check.

```cpp
// cast a PyObject* to C i64 (unsafe but faster)
i64 j = _CAST(i64, obj);		
```

For complex objects like `list`, we can use reference cast to avoid unnecessary copy.

```cpp
PyObject* obj = VAR(List());
// reference cast (no copy)
List& list = CAST(List&, obj);
```

### Check type of `PyObject*`

Each `PyObject*` has a `Type` field to indicate its type.
`Type` is just an integer which is the global index in `VM::_all_types`.

`VM` class has a set of predefined `Type` constants for quick access.
They are prefixed by `tp_`. For example, `tp_object`(object),
`tp_int`(int), `tp_str`(str), `tp_list`(list), etc.

Types are divided into **tagged type** and **non-tagged type**.
+ `int` and `float` are tagged type.
+ Other types are non-tagged type.

To determine whether a `PyObject*` is of a specific type,
you can use the following functions:

+ `bool is_type(PyObject* obj, Type type)`
+ `bool is_int(PyObject* obj)`
+ `bool is_float(PyObject* obj)`
+ `bool is_tagged(PyObject* obj)`
+ `bool is_non_tagged_type(PyObject* obj, Type type)`

```cpp
PyObject* obj = VAR(1);

bool ok = is_type(obj, vm->tp_int);		// true
ok = is_int(obj);						// true
ok = is_tagged(obj);					// true

ok = is_type(obj, vm->tp_float);		// false
ok = is_float(obj);						// false
```

Simply put, `is_type` is the most general function and can check any types.
Other variants are designed for specific types and are faster.

You can also use `check_` prefix functions assert the type of a `PyObject*`,
which will throw `TypeError` on failure.

+ `void VM::check_type(PyObject* obj, Type type)`
+ `void VM::check_non_tagged_type(PyObject* obj, Type type)`