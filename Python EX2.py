###EX 02


n = input('saisissez un nombre:  ')
def fun_factorielle(n):
   if n: 
    try:    
      if int(n) < 0:  
        raise ValueError("le nombre saisie est négatif")

      elif int(n) >= 100:
        raise ValueError('le nombre saisie est très grand')

      elif int(n) < 1:
        raise ValueError('le nombre saisie est très petit') #redondance avec la première exception

    except ValueError as error:
        return print(error)
   
    else:
      F = 1
      for i in range(2, int(n) + 1):
         F = F * i
      return F

fun_factorielle(n)