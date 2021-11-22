# InterviewWait

# Verificar el tiempo enque nos tocara esperar para la entrevista, nosotros somos el valor -1, siempre elige al menos valor de los extremos
# Luque Ccosi Paul Alexander

def InterviewWait(listaWait):
    resul = 0

    while True:
        # Verificamos si ya termianmos
        if(listaWait[0] < 0):
            return resul
        elif(listaWait[-1] < 0):
            return resul
        # Ingresamos el minimo valor
        else:
            if(listaWait[0] < listaWait[-1]):
                resul += listaWait.pop(0)
            else:
                resul += listaWait.pop(-1)
    return resul


# Datos de prueba
print("lista: " + [4, -1, 5, 2, 3, 1, 0].__str__())
print(InterviewWait([4, -1, 5, 2, 3]))