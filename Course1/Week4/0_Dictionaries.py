# WEEK 4
#----------------------------------------DICTIONARIES---------------------------------------------
# %%
#--------------------------------------------------
#1 What is a dictionary?
#Es una estructura de datos que tiene una clave
x={}
type(x)
#OUTPUT
#dict
# %%
#Diccionario con 4 elementos
file_counts ={"jpg":"10","txt":14, "csv":2,"py":23}
print(file_counts)
#OUTPUT
# {'jpg': '10', 'txt': 14, 'csv': 2, 'py': 23}

# %%
#Acceder al valor mediante la clave
file_counts["txt"]
#OUTPUT
# 14

# %%
#pertenencia elemento de un diccionario
"jpg" in file_counts
#OUTPUT
#True
"html" in file_counts
#OUTPUT
#false
# %%
#Agregar elemento al diccionario
file_counts["cfg"]=8
file_counts["cfg"]
print(file_counts)
#OUTPUT
# {'jpg': '10', 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
# %%
#Modificar elemento del diccionario(Mutable)
file_counts["csv"]=17
print(file_counts)
#OUTPUT
# {'jpg': '10', 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
# %%
#Borrar elemento del diccionario
del file_counts["cfg"]
print(file_counts)
#OUTPUT
# {'jpg': '10', 'txt': 14, 'csv': 17, 'py': 23}
#--------------------------------------------------
#2 Iterating over the Contents of a Dictionary
# %%
#Iteraccion por clave 
file_counts ={"jpg":"10","txt":14, "csv":2,"py":23}
for extension in file_counts:
    print(extension)
#OUTPUT
# jpg
# txt
# csv
# py

# %%
#Iteraccion por clave y valor
for ext,amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
#OUTPUT
# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension

# %%
#Obtener todas las claves del diccionario
file_counts.keys()
# dict_keys(['jpg', 'txt', 'csv', 'py'])

#Iteraccion por claves
for keys in file_counts.keys():
    print(keys)
#OUTPUT
# jpg
# txt
# csv
# py
# %%
#Obtener todos las valores del diccionario
file_counts.values()
# dict_values(['10', 14, 2, 23])

#Iteraccion por valores
for value in file_counts.values():
    print(value)
#OUTPUT
# 10
# 14
# 2
# 23

#%%
cool_beasts ={"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, limbs in cool_beasts.items():
    print("{} have {}".format(animal,limbs))
#OUTPUT
# octopuses have tentacles
# dolphins have fins
# rhinos have horns
# %%
#Te devuelve en un diccionario la letra y el numero de veces que aparece 
def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:#crea el diccionario
            result[letter]=0
        result[letter]+=1
    return result

count_letters("aaaaa")
#OUTPUT
# {'a': 5}
# %%
count_letters("tenant")
#OUTPUT
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}
# %%
count_letters("a long string with a lot of letters")
#OUTPUT
# {'a': 2,
#  ' ': 7,
#  'l': 3,
#  'o': 3,
#  'n': 2,
#  'g': 2,
#  's': 2,
#  't': 5,
#  'r': 2,
#  'i': 2,
#  'w': 1,
#  'h': 1,
#  'f': 1,
#  'e': 2}

#--------------------------------------------------
# 3 Dictionaries vs. Lists
#Usar diccionarios cuando se desea utilizar elemento especifico
#Las claves pueden ser booleanos,cadenas o tuplas mientras que 
#los valores no hay restricciones
# %%
wardrove={"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth, colours in wardrove.items():
    for colour in colours:
        print("{}{}".format(colour,cloth))
#OUTPUT
# redshirt
# blueshirt
# whiteshirt
# bluejeans
# blackjeans


#--------------------------------------------------

#4 Dictionary Methods Cheat Sheet
# Syntax
# x = {key1:value1, key2:value2} 

# Operations
# len(dictionary) - Returns the number of items in the dictionary
# for key in dictionary - Iterates over each key in the dictionary
# for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
# if key in dictionary - Checks whether the key is in the dictionary
# dictionary[key] - Accesses the item with key key of the dictionary
# dictionary[key] = value - Sets the value associated with key
# del dictionary[key] - Removes the item with key key from the dictionary

# Methods
# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
# dict.keys() - Returns a sequence containing the keys in the dictionary
# dict.values() - Returns a sequence containing the values in the dictionary
# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
# dict.clear() - Removes all the items of the dictionary


# %%
