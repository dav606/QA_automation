def SumOfDigits(number):
  sum=0
  digit = 0
  while number != 0:
    digit=int(number%10)
    sum += digit
    number/=10
  return sum

number = int(input("Enter a number: "))
res = int(SumOfDigits(number))
print(res)
