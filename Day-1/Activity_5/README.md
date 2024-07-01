# Activity 5

Look into these methods write an example of each with an
explanation of how each one works:
• upper()
• lower()
• capitalize()
• count()
• find()
• replace()
• strip()

## upper()

The upper() method returns a string where all characters are in upper case.

Symbols and Numbers are ignored.

```python
earth_greeting = "    Hello Earthling, do not be afraid!"
print(earth_greeting)

# .upper


loud_greeting = earth_greeting.upper()
print(loud_greeting)

```

## lower()

The lower() method returns a string where all characters are lower case.
Symbols and Numbers are ignored.

```python
quiet_greeting = loud_greeting.lower()
print(quiet_greeting)
```

## capitalize()

The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

```python
proper_greeting = earth_greeting.capitalize()
print(proper_greeting)
```

## count

The count() method returns the number of elements with the specified value.

```python
count_o = earth_greeting.count("o")
print(count_o)
```

## find

The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

```python
find_i = earth_greeting.find("i")
print(find_i)
```

## replace

The replace() method replaces a specified phrase (left) with another specified phrase (right).

```python
translate_greet = earth_greeting.replace("e", "z")
print(translate_greet)
```

## strip

The strip() method removes any leading, and trailing whitespaces.

Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.

```python
new_greet = earth_greeting.strip()
print(new_greet)
```

## Additional Note

The above methods were applied to a variable but with print() you can print the method on the original variable or the inital string itself

The code below all give the same result

```python
loud_greeting = earth_greeting.upper()
print(loud_greeting)

print(earth_greeting.upper())

print("    Hello Earthling, do not be afraid!".upper())
```
