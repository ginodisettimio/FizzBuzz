#Escribe un programa que imprima los números del 1 al 100.
#Pero para los múltiplos de 3, imprime la palabra "Fizz" en lugar del número, y para los múltiplos de 5, imprime "Buzz".
#Para los números que son múltiplos de tanto 3 como 5, imprime "FizzBuzz".

numbers = list(range(1,101))
for n in numbers:
  if n % 15 == 0:
    n = ('FizzBuzz')
  elif n % 3 == 0:
    n = ('Fizz')
  elif n % 5 == 0:
    n = ('Buzz')

  print(n)
