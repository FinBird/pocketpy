# pocketpy: python interpreter in 1 file

<p>
<a title="Build" href="https://github.com/blueloveTH/pocketpy/actions/workflows" ><img src="https://github.com/blueloveTH/pocketpy/actions/workflows/main.yml/badge.svg" /></a>
<a href="https://github.com/blueloveth/pocketpy/blob/main/LICENSE">
<img alt="GitHub" src="https://img.shields.io/github/license/blueloveth/pocketpy.svg?color=blue"></a>
<a href="https://github.com/blueloveth/pocketpy/releases">
<img alt="GitHub release" src="https://img.shields.io/github/release/blueloveth/pocketpy.svg"></a>
</p>

**English |** [**简体中文**](README_zh.md)

pkpy is a lightweight(~10000 LOC) Python interpreter for game scripting, built on C++17 with STL.

It aims to be an alternative to lua for game scripting, with elegant syntax, powerful features and competitive performance.
pkpy is extremely easy to embed via a single header file `pocketpy.h`, without external dependencies.

Please see https://pocketpy.dev for details or try [Live Demo](https://pocketpy.dev/static/web/).

<a href="https://www.buymeacoffee.com/blueloveTH"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=blueloveTH&button_colour=FF5F5F&font_colour=ffffff&font_family=Bree&outline_colour=000000&coffee_colour=FFDD00" /></a>

## Quick start

Download the `pocketpy.h` on our [GitHub Release](https://github.com/blueloveTH/pocketpy/releases) page.
And `#include` it in your project.

### Compile flags

To compile it with your project, these flags must be set:

+ `--std=c++17` flag must be set
+ Exception must be enabled
+ RTTI is not required

!!!
For maximum performance, we recommend to use `clang++` with `-O2` flag.
!!!

### Example

```cpp
#include "pocketpy.h"

using namespace pkpy;

int main(){
    // Create a virtual machine
    VM* vm = new VM();
    
    // Hello world!
    vm->exec("print('Hello world!')", "main.py", EXEC_MODE);

    // Create a list
    vm->exec("a = [1, 2, 3]", "main.py", EXEC_MODE);

    // Eval the sum of the list
    PyObject* result = vm->exec("sum(a)", "<eval>", EVAL_MODE);
    std::cout << CAST(int, result);   // 6
    return 0;
}
```

## Features

| Name            | Example                         | Supported |
| --------------- | ------------------------------- | --------- |
| If Else         | `if..else..elif`                | YES       |
| Loop            | `for/while/break/continue`      | YES       |
| Function        | `def f(x,*args,y=1):`           | YES       |
| Subclass        | `class A(B):`                   | YES       |
| List            | `[1, 2, 'a']`                   | YES       |
| ListComp        | `[i for i in range(5)]`         | YES       |
| Slice           | `a[1:2], a[:2], a[1:]`          | YES       |
| Tuple           | `(1, 2, 'a')`                   | YES       |
| Dict            | `{'a': 1, 'b': 2}`              | YES       |
| F-String        | `f'value is {x}'`               | YES       |
| Unpacking       | `a, b = 1, 2`                   | YES       |
| Star Unpacking  | `a, *b = [1, 2, 3]`             | YES       |
| Exception       | `raise/try..catch`              | YES       |
| Dynamic Code    | `eval()/exec()`                 | YES       |
| Reflection      | `hasattr()/getattr()/setattr()` | YES       |
| Import          | `import/from..import`           | YES       |
| Context Block   | `with <expr> as <id>:`          | YES       |
| Type Annotation | `def  f(a:int, b:float=1)`      | YES       |
| Generator       | `yield i`                       | YES       |
| Decorator       | `@cache`                        | YES       |

## Contribution

All kinds of contributions are welcome.

- Submit a Pull Request
  - fix a bug
  - add a new feature
- Open an Issue
  - any suggestions
  - any questions

Check our [Coding Style Guide](https://pocketpy.dev/coding_style_guide/) if you want to contribute C++ code.

## Reference

+ [cpython](https://github.com/python/cpython)

  The official implementation of Python programming language.

+ [byterun](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

  An excellent learning material. It illustrates how Python's virtual machine works.


## License

pkpy is licensed under the [MIT License](http://opensource.org/licenses/MIT).

