def fizz_buzz(num):
    if num%5==0:
        return 'FizzBuzz'
      elif num % 5==0:
        return 'Buzz'
    else:
        return num
for n in range(1,100):
    print(fizz_buzz(n))
