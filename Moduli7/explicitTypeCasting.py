#int(x), float(x), str(x), list(x), tuple(x), bool(x)


#Example 1
age = 25
print(age, type(age))

age_as_str = str(age)
print(age_as_str, "of type", type(age_as_str))


#Example 2
print(bool(0))
print(bool(42))

print(bool(""))
print(bool("Hello"))

print(bool([]))
print(bool(None))