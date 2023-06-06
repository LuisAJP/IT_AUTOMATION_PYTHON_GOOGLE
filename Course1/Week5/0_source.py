#-----------------------1 Object-oriented Programming-----------------------------------------------------
#%%
#Ejemplo de definicion de clases
class Apple:
  pass
class Apple:
  color=""
  flavor=""
jonagold=Apple()
jonagold.color="red"
jonagold.flavor="sweet"
print(jonagold.color)

#red
#%%
#Want to give this a go? Fill in the blanks in the code to make it print a poem
class Flower:
  color='unknown'
rose=Flower()
rose.color="red"

violet=Flower()
violet.color="blue"

this_pun_is_for_you="Sugar is sweet, and so are you"
print("Roses are {},".format(rose.color))
print("Violets are {},".format(violet.color))
print(this_pun_is_for_you)

#OUTPUT
# Roses are red,
# Violets are blue,
# Sugar is sweet, and so are you

#-----------------------2 Classes and Methods-----------------------------------------------------
#%%
#Ejemplo de Instancia de metodos
class Piglet:
  name="piglet"

  def speak(self):
    print("Oink! I'm {}! Oink!".format(self.name))

hamlet=Piglet()
hamlet.name="Hamlet"
hamlet.speak()
petunia=Piglet()
petunia.name="Petunia"
petunia.speak()

# Oink! I'm Hamlet! Oink!
# Oink! I'm Petunia! Oink!
#%%
class Piglet:
  years=0
  def pig_years(self):
    return self.years*18

piggy=Piglet()
print(piggy.pig_years())

piggy.years=2
print(piggy.pig_years())

# 0
# 36

#%%

#In this doce, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so
#that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting
#states the assigned name.
class Dog:
  years:0
  def dog_years(self):
    return self.years*7

fido=Dog()
fido.years=3
print(fido.dog_years())

#21

#-----------------------Constructors and other special methods----
#%%
class Apple:
  def __init__(self, color,flavor):
    self.color=color
    self.flavor=flavor

jonagold= Apple("red","sweet")
print(jonagold.color)
#-----------------------3 Code Reuse-----------------------------------------------------
# %% Inheritance/Object Inheritance
class Fruit:
     def __init__(self, color, flavor):
         self.color = color
         self.flavor = flavor

class Apple(Fruit):
     pass
 
class Grape(Fruit):
     pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)

# %% Inheritance/Object Inheritance
class Animal:
    sound=""
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("{sound} I'm {name}! {sound} ".format(name=self.name,sound=self.sound))

class Piglet(Animal):
    sound="Oink!"

class Cow(Animal):
     sound = "Moooo"


hamlet= Piglet("Hamlet")
hamlet.speak()     
milky = Cow("Milky White")
milky.speak()



#------------------------------------------------------------------------------------------------#
# %%
# Composition/Object Composition
class Repository:
    amount=0
    def __init__(self):
        self.packages = {}

    def add_package(self,package):
        self.packages[package.name]=package

    def total_size(self):
        result=0
        for package in self.packages.values():
            result += package.total_size
        return result

# class Package:
#     def __init__(self,name):

# %%
# Composition Question
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name

  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)

  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")

polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")

print(current_stock)



#------------------------------------------------------------------------------------------------#
# %% 
# Python Modules (Optional)/Augmenting Python with Modules
import random
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)


# %%
# Python Modules (Optional)/Augmenting Python with Modules
import datetime
now = datetime.datetime.now()
type(now)
print(now)
# %%
