import random
def funcion(func):
    def wrapper(*args, **kwargs):
        func(*args,**kwargs)
        bloque1 = str(192)
        bloque2 = str(168)
        bloque3 = str(1)
        ips = int(input('Ingrese la cantidad de IPs a generar: '))
        return bloque1, bloque2, bloque3, ips
        generador(bloque1, bloque2, bloque3, ips) 
    return wrapper

@funcion
def generador(bloque1, bloque2, bloque3, ips):
    for i in range (ips):
        print(f'Tu IP generada es {bloque1}.{bloque2}.{bloque3}.{i}')

generador()