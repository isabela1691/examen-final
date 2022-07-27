import time
def decorador(funcion):
    def calculadora(*args,**kwargs):
        comienzo = time.time()
        resultado=funcion(*args,**kwargs)
        print("Tiempo en ejecución es: {}".format(time.time() - comienzo))

        return resultado
    return calculadora
#suma de dos números para decorarla con la función anterior.
@decorador
def suma(a,b):
    time.sleep(1)
    return a+b
print(suma(15,9))
