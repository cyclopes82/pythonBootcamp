def exponent(num, power=2):
    """exponent(num, power) raises num to specified power. Power defaults to 2."""
    return num ** power

print(exponent(2,3)) #8
print(exponent(3,2))
print(exponent(2))

print(exponent.__doc__)