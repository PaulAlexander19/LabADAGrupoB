## Minimum Add to Make Parentheses Valid
## Luque Ccosi Paul Alexander

## Encontrar la minima cantidad de parentesis para que sea valida la entrada de parentesis

## Aqui podemos agregar mas elementos
first = ["("]
finish = [")"]

def parenthesesValid(str):
    s = [] ## stack
    for i in str:
        print(i)
        if(i in first):
            s.append(i)
        elif(i in finish):
            if(len(s) == 0 or s[-1] in finish):
                s.append(i)
            elif(s[-1] in first):
                s.pop()
    return s
        
        

## Datos de Prueba
res = parenthesesValid("())")
print(res)
print(len(res))

## Datos de Prueba
res = parenthesesValid("(()))(")
print(res)
print(len(res))

res = parenthesesValid("()))((")
print(res)
print(len(res))
