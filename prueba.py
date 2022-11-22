beta= lambda x: 2*x
op_alfa = lambda x: x+1

uno = lambda f: lambda x: f(x)
dos =  lambda f: lambda x: f(f(x))
cinco  = lambda f: lambda x: f(f(f(f(f(x)))))
tres   = lambda f: lambda x: f(f(f(x)))
cero = lambda f: lambda x: x
ocho = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))
#Valores
op_beta = lambda x: 2 * x
resultado1=ocho(op_beta)(5)
print (resultado1)



#operaciones 
# op_sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
# resultado2=(op_sucesor(uno)(op_alfa)(5))
# print (resultado2)

# op_suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
# resultado3=(op_suma(tres)(cero)(op_alfa)(5))
# print (resultado3)


# op_multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
# resultado4=(op_multiplicacion(dos)(tres)(op_alfa)(5))
# print (resultado4)

# op_potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x) #h
# op_beta = lambda x: 2 * x
# potencia_beta = (op_potencia(dos)(tres)(op_beta)(5))