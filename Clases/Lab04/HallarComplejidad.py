## Hallar la complejidad del codigo escrito en google

## Código en GO
# def every_other(array):
#     array.each_with_index do |element, index|
#         if index.even?
#             arrat.each do |other_number|
#                 puts number + other_number
#             end
#         end
#     end
# end

## Implementación en Python

def every_other(array):
    for index in range(0, len(array), 2):
        for other_number in array:
            print(array[index] + other_number)

        print("----\n")

## ANÄLISIS DE COMPLEJIDAD ----------------------------
# Como se pude obserbar son 2 ciclos anidades y en cada cilo se recorre todo el arreglo
# por lo que la complejidad es O(n^2)
# -----------------------------------------------------


## Prueba del algoritmo 

arr = [1,2,3]

every_other(arr)


