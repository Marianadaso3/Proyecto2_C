#Proyecto2 - Segunda parte/funciones lambda
#Teoría de la computación 
#Autor: Mariana David, Fredy Velazquez, Angel Higueros 
#Carnet: 201055, 201011, 20963


#Fuentes de referencia: 
#Funciones labda: https://borjauria.es/que-son-y-como-utilizar-lambdas-en-python-4d1d168e2f90
#Funciones labda: https://realpython.com/python-lambda/#appropriate-uses-of-lambda-expressions
#Funciones labda: https://recursospython.com/guias-y-manuales/funciones-lambda/
#Funciones beta y betaop_beta: https://www.toppr.com/ask/question/displaystyle-alpha-beta-are-the-root-of-the-equation-displaystyle-lambda-left-x2x/
#Funciones beta y betaop_beta: https://www.doubtnut.com/question-answer/alpha-beta-are-roots-of-lambda-x2-x-x-5-0-if-lambda1-and-lambda-2-are-the-two-values-of-lambda-for-w-6777

#-----------------------------------Inicio de funciones----------------------------

#Definimos expresiones numericas con lambda 
cero = lambda f: lambda x: x #a
uno = lambda f: lambda x: f(x)  #b
dos =  lambda f: lambda x: f(f(x)) #c
tres   = lambda f: lambda x: f(f(f(x))) #d
# Extras cuatro y cinco 
cuatro  = lambda f: lambda x: f(f(f(f(x))))
cinco  = lambda f: lambda x: f(f(f(f(f(x)))))
ocho = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))

#Definimos procesos numericas con lambda 
op_sucesor = lambda n: lambda f: lambda x: f(n(f)(x)) #e
op_suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x)) #f
op_multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x) #g
op_potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x) #h

#Operaciones lamda con op_beta y beta 
op_alfa = lambda x: x + 1
op_beta = lambda x: 2 * x

#Funciones para ejemplificar 
def valores_num():
    resultado_cero = cero(op_beta)(5) #prueba con beta
    resultado_uno = uno(op_beta)(5)
    resultado_dos = dos(op_beta)(5)
    resultado_tres = tres(op_beta)(5)
    resultado_cuatro = cuatro(op_beta)(5)
    resultado_cinco = cinco(op_beta)(5)
    print ("Los resultados de los valores respectivamente del cero al cinco son: ", "\nCERO:",resultado_cero,"\nUNO:", resultado_uno, "\nDOS:",resultado_dos,"\nTRES:",resultado_tres,"\nCUATRO:",resultado_cuatro,"\nCINCO:",resultado_cinco)

def sucesor():
    sol_sucesor = (op_sucesor(dos)(op_beta)(5))
    print ("Valor que le sigue es: ", sol_sucesor)  
def suma():
    sol_suma = (op_suma(dos)(tres)(op_beta)(5))
    print ("El reultado de la suma es: ", sol_suma)
def multiplicacion():
    sol_multiplicación = (op_multiplicacion(dos)(tres)(op_beta)(5))
    print ("El resultado de la multiplicación es: ", sol_multiplicación)  
def potencia ():
    sol_potencia = (op_potencia(dos)(tres)(op_beta)(5))
    print ("El resultado de la potencia es: ", sol_potencia)