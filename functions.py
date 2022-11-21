#Proyecto2 - Segunda parte/funciones lambda
#Teoría de la computación 
#Autor: Mariana David, Fredy Velazquez, Angel Higueros 
#Carnet: 201055, 201011, 20963


#Fuentes de referencia: 
#Funciones labda: https://borjauria.es/que-son-y-como-utilizar-lambdas-en-python-4d1d168e2f90
#Funciones labda: https://realpython.com/python-lambda/#appropriate-uses-of-lambda-expressions
#Funciones labda: https://recursospython.com/guias-y-manuales/funciones-lambda/
#Funciones beta y alfa: https://www.toppr.com/ask/question/displaystyle-alpha-beta-are-the-root-of-the-equation-displaystyle-lambda-left-x2x/
#Funciones beta y alfa: https://www.doubtnut.com/question-answer/alpha-beta-are-roots-of-lambda-x2-x-x-5-0-if-lambda1-and-lambda-2-are-the-two-values-of-lambda-for-w-6777

#-----------------------------------Inicio de funciones----------------------------

#Definimos expresiones numericas con lambda 
#a
cero = lambda f: lambda x: x
#b
uno = lambda f: lambda x: f(x)
#c
dos =  lambda f: lambda x: f(f(x))
#d
tres   = lambda f: lambda x: f(f(f(x)))


#Definimos procesos numericas con lambda 
#e
op_sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
#f
op_suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
#g
op_multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
#h
op_potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)

#Operaciones lamda con op_alfa y beta 
op_alfa = lambda x: x+1
op_beta = lambda x: 2 * x

#Funciones para ejemplificar 
def sucesor():
    print ("Valor que le sigue a 1 es: ", op_sucesor(uno)(op_alfa)(cero(op_alfa)(0)))  

def suma():
    print ("La suma de 2 + 2 es:", op_suma(dos)(dos)(op_alfa)(cero(op_alfa)(0)))

def multiplicacion():
    print ("El factor de 2 * 3 es:", op_multiplicacion(dos)(tres)(op_alfa)(cero(op_alfa)(0)))  

def potencia ():
    print ("La potencia del numero 3 es: ", op_potencia(tres)(tres)(op_alfa)(cero(op_alfa)(0)))