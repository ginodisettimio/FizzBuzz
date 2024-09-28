numbers = list(range(1,101))
for n in numbers:
  if n % 15 == 0:
    n = ('FizzBuzz')
  elif n % 3 == 0:
    n = ('Fizz')
  elif n % 5 == 0:
    n = ('Buzz')

  print(n)
  