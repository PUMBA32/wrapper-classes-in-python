# Wrapper classes for python: Integer, Boolean, Float (not finished), String

I tried to wrote wrapper classes for main primitive types of data in the Python language. I was inspired by wrapper classes from Java and this is why there are lot of methods from Java wrapper classes there, however i also added some my personal methods for variety) 

## Integer 
```python
from integer import Integer as Int

n: Int = Int(10)

# Some methods

print(n.to_bin())  # 1010
print(n.to_hex())  # A
print(n.to_oct())  # 12
print(n.float_value())  # 10.0
print(n.to_str())  # "10"
print(n.get_bit_count())  # 4

print(Int.parse_int("12345"))  # 12345
print(Int.parse_int("1010", 2))  # 10
print(Int.parse_int("A", 16))  # 10
print(Int.bit_count(100)) # 7
print(Int.convert_to_oct(54))  # "66"
print(Int.compare(2, -34))  # 2
```

## Boolean

```python
from boolean import Boolean as Bool

is_f: Bool = Bool(True)

# Some methods

print(is_f.to_string())  # "True"
print(is_f.compare_to(True))  # 1

print(Bool.logical_and(True, False))  # False
print(Bool.logical_or(False, True))  # True
print(Bool.logical_xor(False, True))  # True
print(Bool.parse_boolean("True"))  # True

```

## String

```python
from string improt String as Str

text: Str = Str("There is 100")

# Some methods

print(text.to_lower())  # there is 100
print(text.to_upper())  # THERE IS 100
print(text.index("T"))  # 0
print(text.replace("0", "P"))  # There is 1pp
print(text.split())  # ["There", "is", "100"]
```
