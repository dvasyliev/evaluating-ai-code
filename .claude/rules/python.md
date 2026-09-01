---
description: Python coding rules. Applies to Python files only.
paths:
  - "**/*.py"
---

# Python Rules

Scope: `*.py` files only. These rules do not apply to other languages.

## Never use a mutable default argument

A default `[]` or `{}` is created once at definition and shared by every call.

```python
# bad
def add_item(item, cart=[]):
    cart.append(item)
    return cart

# good
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```

## Use `is` only for `None` and other singletons

`is` compares identity, not value. It appears to work on small ints and literals, then fails when equal values come from elsewhere.

```python
# bad
if name is "hello world":

# good
if name == "hello world":
if value is None:
```

## Open files with `with`

The context manager closes the file even when the body raises.

```python
# bad
f = open("data.txt")
data = f.read()
f.close()

# good
with open("data.txt") as f:
    data = f.read()
```

## Catch specific exceptions

A bare `except:` also swallows `KeyboardInterrupt` and `SystemExit`, so the program hides bugs and can't be stopped.

```python
# bad
try:
    value = int(raw)
except:
    value = 0

# good
try:
    value = int(raw)
except ValueError:
    value = 0
```

## Return or raise, never print, to report failure

A printed message never reaches the caller, and `None` looks like a real value until something does arithmetic on it.

```python
# bad
def square_root(a):
    if a < 0:
        print("Negative input")
        return None

# good
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
```

## Iterate over the object, not its indices

```python
# bad
for i in range(len(names)):
    print(names[i])

# good
for name in names:
    print(name)

# when you need the index
for i, name in enumerate(names):
    print(i, name)
```

## Use `dict.get` for a missing key

The default applies only when the key is absent. A key present with value `None` returns `None`, not your default.

```python
# bad
if "timeout" in config:
    timeout = config["timeout"]
else:
    timeout = 30

# good
timeout = config.get("timeout", 30)
```

## Guard the entry point with `__name__`

Without it, importing the module runs it, which also makes it untestable.

```python
# bad
main()

# good
if __name__ == "__main__":
    main()
```

## Name constants, don't inline the number

An unexplained literal can't be found or changed safely.

```python
# bad
if attempts > 3:

# good
MAX_ATTEMPTS = 3
if attempts > MAX_ATTEMPTS:
```

## Let each function do one thing

Mixing input, computation and output means none of the three can be reused or tested alone.

```python
# bad
def process():
    raw = input("Number: ")
    print(f"Result: {float(raw) * 2}")

# good
def double(value):
    return value * 2
```

## Test for the condition you mean, not truthiness

`if x:` is false for `0`, `""` and `[]`. Use it only when empty and missing should behave the same.

```python
# bad
if count:                  # 0 is a real count

# good
if count > 0:
if items is not None:      # empty list is still a value
```

## Bound anything that grows

A list appended to in a loop grows for the life of the process, even if you only ever read the tail.

```python
# bad
history = []
history.append(entry)

# good
from collections import deque

history = deque(maxlen=5)
history.append(entry)
```
