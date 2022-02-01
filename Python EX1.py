###EX O1

#Question 1

def fun_polynomiale(x):
  return (x**3 - 1.5*(x**2) - 6*x + 5)

fun_polynomiale(5)


#Question 2

n = int(input())
def fun_factorielle(n):
   if n == 0:
      return print("le factorielle de 1 est: 1")
   elif n < 0:
     return print("Veuillez renseigner un nombre positif")
   else:
      F = 1
      for i in range(2, n + 1):
         F = F * i
      return F

fun_factorielle(n)

#Question 3

def fun_fibonacci(m = int(input())):
    x = 0
    y = 1
    print("la suite de fibonacci est: ")
    if m == 0:
        return x
    elif m == 1:
        return y
    else:
        print(x)
        print(y)
        for i in range(m-2):
            total = x + y
            print(total)
            x = y
            y = total
            
         
fun_fibonacci()