#6/2 = 2 + 2 + 2
def divide(numerator, denominator):
   if numerator < denominator:
      return 0
   return 1 + divide(numerator - denominator, denominator)

print divide(6, 2)
print divide(2, 6)
print divide(1, 1)
print divide(2, 1)
print divide(1, 2)
