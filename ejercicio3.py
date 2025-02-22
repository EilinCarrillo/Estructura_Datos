#num=5
#resultado:int
#def factorial(n:int)->int:
    #res: int=1
    #for i in range(1,n+1):
        #res=res*i
    #return res

#print(factorial(num))


#num=5
#resultado:int
#def factorial(n:int)->int:
    #res: int=1
    #con=1
    #while con in range(1,n+1):
        #res=res*con
        #con +=1
    #return res

#print(factorial(num))


#num=5
#resultado:int

#def factorial(n):
    #if n==1:
       # return 1
    #return factorial(n-1)*n
#resultado=factorial(5)
#print(factorial(num))


#Ejercicio1
#def fibonacci(n):
    #fib_sequence = [0, 1]  # Inicializamos la lista con los dos primeros términos
    #for i in range(2, n):
       # fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])  # Suma de los dos anteriores
    #return fib_sequence[:n]  # Retornamos solo los primeros 'n' elementos
#n = 20
#print(fibonacci(n))

#Ejercicio2
#def sumar(list):
    #if len(list)==1:
       # print(list[0])
        #return list[0]
    #return list[0]+sumar(list[1:])
#numero=[]
#numeros=0
#for n in range (7):
   #numero.append (int(input ("Ingrese los numeros:")))
#print(sumar(numero))


#Ejercicio3
#def multiplicar(c,b):
    #if b==1:
        #return c
    #return c + multiplicar(c,b-1)
#print(multiplicar(6,2))


#Ejercicio4
#def dividir (a,e):
   # if a < e:
       # return 0
    #return 1 + dividir(a-e,e)
#print(dividir(6,3))














