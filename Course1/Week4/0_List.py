# WEEK 4
#----------------------------------------LISTS---------------------------------------------
# %%
#--------------------------------------------------
#1 What is a list?
x=["Now", "We", "are","cooking"]
#tipo dato
type(x)
print(x)
#OUTPUT
# ['Now', 'We', 'are', 'cooking']

# %%
#longitud lista
print(len(x))
#OUTPUT
# 4

#Se encuentra en la lista
"are" in x
"today" in x
print(x[0])
#OUTPUT
# Now
# %%
print(x[3])
#OUTPUT
# cooking
# %%
print(x[4])
#OUTPUT
# IndexError: list index out of range
# %%
#imprime elementos 0..2
x[1:3]
#OUTPUT
# ['We', 'are']
# %%
#imprime elementos 0..1
x[:2]
#OUTPUT
# ['Now', 'We']

# %%
# Usando el método de cadena "dividida" de la lección anterior,
# completa la función get_word para devolver la {n}ésima palabra de una oración pasada.
# Por ejemplo, get_word("Esta es una lección sobre listas", 4) debería devolver "lección"
# que es la cuarta palabra en esta oración. Sugerencia: recuerde que los índices de lista 
# comienzan en 0, no en 1.

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#OUTPUT
# lesson
# ---
# Now
# ---

#--------------------------------------------------
# 2 Modifying the Contents of a List
# %%
fruits = ["Pineapple","Banana","Apple","Melon"]

#(push)agrega elemento al final de la lista
fruits.append("kiwi")
print(fruits)
# OUTPUT
# ['Orange', 'Pineapple', 'Strawberry', 'kiwi', 'kiwi']

# %%
#inserta un elemento en una posicion dada, si insertas un elemento
#en una posicion que no existe, por ejemplo posicion 15, te lo inserta
#al final
fruits.insert(0,"Orange")
print(fruits)
# OUTPUT
# ['Orange', 'Orange', 'Orange', 'Pineapple', 'Strawberry', 'kiwi', 'kiwi']
# %%
#eliminar elemento mediante el nombre
fruits.remove("Melon")
print(fruits)
# OUTPUT
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'kiwi']

# %%
#eliminar elemento mediante una posicion dada
fruits.pop(3)
print(fruits)
# OUTPUT
# ['Orange', 'Pineapple', 'Banana', 'kiwi']
# %%
#Modificar elemento lista, las listas son mutables
fruits[2]="Strawberry"
print(fruits)
# OUTPUT
# ['Orange', 'Pineapple', 'Strawberry', 'kiwi']

# %%
#La función skip_elements devuelve una lista que contiene todos los demás elementos 
# de una lista de entrada,comenzando con el primer elemento. 
# Complete esta función para hacer eso, usando el
#for loop para iterar a través de la lista de entrada

def skip_elements(elements):
    #Initialize variables
    new_list=[]
    i=0
    #Iterate through the list
    for x in elements:
        #Does this element belong in the resulting list?
        if i%2==0:
            #Add this element to the resulting list
            new_list.insert(i,x)
            #Increment i
        i=i+1
    return new_list

print(skip_elements(["a","b","c","d","e","f","g"]))#should be ["a","c","e","g"]
print(skip_elements(["Orange","Pineapple","Strawberry","Kiwi","Peach"]))#should be ["Orange","Strawberry","Peach"]
print(skip_elements([]))#Should be []
#OUTPUT
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']
# []
# %%
#--------------------------------------------------
# 3 Lists and Tuples

#tupla, las tuplas son inmutables, no se pueden modificar
fullname=('Grace','M','Hopper')

#convierte de segundos a horas, minutos y segundos restantes
def convert_seconds(seconds):
    hours = seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-hours*3600-minutes*60
    return hours, minutes, remaining_seconds

#Obtengo una tupla
result=convert_seconds(5000)
#devuelve el tipo dato tupla
type(result)
print(result)
# OUTPUT 
# (1, 23, 20)

#unpack de result 
hours,minutes,seconds=result
print(hours,minutes,seconds)
# OUTPUT 
# 1 23 20

hours,minutes,seconds=convert_seconds(1000)
print(hours,minutes,seconds)
# OUTPUT 
# 0 16 40

# %%
# Usemos tuplas para almacenar información sobre un archivo: 
# su nombre, su tipo y su tamaño en bytes. Complete los espacios en blanco 
# en este código para devolver el tamaño en kilobytes (un kilobyte son 1024 bytes) 
# hasta con 2 decimales.
def file_size(file_info):
	name, typef, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
# OUTPUT 
# 17.46
# 0.48
# 1.21

# %%
#--------------------------------------------------
# 4 Iterating over Lists and Tuples

#devuelve numero total de letras del array, y el promedio de longitud de caracteres 
animals=["Lion","Zebra","Dolphin","Monkey"]
chars=0
for animal in animals:
    chars +=len(animal)
print("Total characters: {}, Average length: {}".format(chars,chars/len(animals)))
# OUTPUT
# Total characters: 22, Average length: 5.5


winners=["Ashley","Dylan","Reese"]
#La función enumerar devuelve una tupla para cada elemento de la lista
for index,person in enumerate(winners):
    print("{} - {}".format(index+1,person))
# OUTPUT
# 1 - Ashley
# 2 - Dylan
# 3 - Reese

#Recibe una lista de tuplas, y devuelve una lista de elementos
def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("alex@example.com","Alex Diego"),("shay@example.com","Shay Brandt")]))
# OUTPUT
# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']



# Pruebe la función de enumerar usted mismo en este ejercicio rápido. 
# Complete la función skip_elements para devolver todos los demás elementos de la lista, 
# esta vez usando la función de enumeración para verificar 
# si un elemento está en una posición par o impar.
def skip_elements(elements):
	# code goes here
	new_elements=[]
	for i,element in enumerate(elements):
		if i%2 == 0:
			new_elements.append(element)
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# OUTPUT
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']


# %%
#--------------------------------------------------
# 5 List Comprehensions
# Python proporciona una técnica llamada comprensión de listas, 
# que nos permite crear una lista en una sola línea. Las comprensiones 
# de listas nos permiten crear nuevas listas basadas en secuencias o rangos. 
# newlist=[expression for item in iterable if condition == True]

#Devuelve Multiplo de 7
multiples=[x*7 for x in range(1,11)]
print(multiples)
# OUTPUT
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#Devuelve numero letras de cada elemento
languages=["Python","Perl","Ruby","Go","Java","C"]
lengths=[len(language)for language in languages]
print(lengths)
# OUTPUT
# [6, 4, 4, 2, 4, 1]

#Devuelve multiplo de 3
z=[x for x in range(0,101) if x%3==0]
print(z)
# OUTPUT
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]


# La función números_impares devuelve una lista de números impares entre 1 y n, 
# ambos inclusive. Completa los espacios en blanco de la función, usando la comprensión de listas. 
# Sugerencia: recuerde que los contadores de lista y rango comienzan en 0 y 
# terminan en el límite menos 1.
def odd_numbers(n):
	return [x for x in range (0,n+1) if x%2 ==1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
# OUTPUT
# [1, 3, 5]
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9, 11]
# [1]
# []

# %%
#--------------------------------------------------
#Lists and Tuples Operations Cheat Sheet

# Common sequence operations
# len(sequence) - Returns the length of the sequence
# for element in sequence - Iterates over each element in the sequence
# if element in sequence - Checks whether the element is part of the sequence
# sequence[i] - Accesses the element at index i of the sequence, starting at zero
# sequence[i:j] - Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
# for index, element in enumerate(sequence) - Iterates over both the indexes and the elements in the sequence at the same time

#  Check out the official documentation for sequence operations.
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# List-specific operations and methods
# list[i] = x - Replaces the element at index i with x
# list.append(x) - Inserts x at the end of the list
# list.insert(i, x) - Inserts x at index i
# list.pop(i) - Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) - Removes the first occurrence of x in the list
# list.sort() - Sorts the items in the list
# list.reverse() - Reverses the order of items of the list
# list.clear() - Removes all the items of the list
# list.copy() - Creates a copy of the list
# list.extend(other_list) - Appends all the elements of other_list at the end of list

#  Most of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.
#Documentacion oficial para sequencias mutables
#https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
#Documentacion sobre listas
#https://docs.python.org/3/library/stdtypes.html#lists

# List comprehension
# [expression for variable in sequence] - Creates a new list based on the given sequence. Each element is the result of the given expression.
# [expression for variable in sequence if condition] - Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  