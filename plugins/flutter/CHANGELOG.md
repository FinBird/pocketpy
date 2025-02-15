## 0.9.3

+ See https://github.com/blueloveTH/pocketpy/releases

## 0.8.1

+ Bug fix
+ Add `vm.bind<T>` support

## 0.8.0+2

+ add complete reflection (exec/eval/getattr/setattr/hasattr)
+ fix a bug of raw string
+ add slice support for `tuple`
+ improve performance
+ remove thread support

## 0.6.2+1

+ Break change
+ Enable bytecode optimization, which improves performance by 50%

## 0.5.2+3

+ Add web support
+ Add `re` module

## 0.5.1+3

+ Fix a bug of parsing large `list/dict/set`
+ Add `os.path.join`

## 0.5.0+7

+ Fix a bug of crash when using multi-thread

## 0.5.0+4

+ Fix a bug on Windows
+ Add `set` class
+ Fix a bug of `[]`

## 0.4.7+3

The initial version. Hello, world!

## 0.4.8+1

+ Add keyword call, i.e., `print(1, 2, sep=', ', end='\n')`
+ Support hex integer literal `0xFFFF`
+ Fix some bugs
+ Add `list.pop` and `reversed` builtin function
+ Optimize `dict` performance

## 0.4.8+2

+ Fix a bug of `bool`
+ Support type hints
+ Fix a bug about comment and indentation
+ Fix a bug about compile error line number

## 0.4.8+6

+ Downgrade to `sdk>=2.17.0`
+ Fix some bugs about compile error
+ Fix a bug for jsonify `nan` or `inf`
+ Add `math.isnan` and `math.isinf`
+ Fix a bug of `__checkType`