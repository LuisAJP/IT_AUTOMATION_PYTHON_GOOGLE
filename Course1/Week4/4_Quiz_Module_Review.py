#%% con rangos
#--------------------------------------------------
# Question 1 
# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name
#  which may contain numbers, but never by themselves, and could be several words long. 
#  For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
#  Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  number=""
  street=""
  # Separate the address string into parts
  separate_string= address_string.split()
  # Traverse through the address parts
  for x in separate_string:
    # Determine if the address part is the
    # house number or part of the street name
    number= " ".join(separate_string[:1])
    street=" ".join(separate_string[1:])
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(number,street)

print(format_address("123 Main Street"))
#OUTPUT
# "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
#OUTPUT
#"house number 1001 on street named 1st Ave"
print(format_address("55 North Center Drive"))
#OUTPUT
#"house number 55 on street named North Center Drive"



#--------------------------------------------------
# %%
# Question 2 
# The highlight_word function changes the given word in 
# a sentence to its upper-case version. For example, 
# highlight_word("Have a nice day", "nice") returns "Have a NICE day".
#  Can you write this function in just one line?
def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
#OUTPUT
# Have a NICE day
# Shhh, don't be so LOUD!
# Automating with Python is FUN

#--------------------------------------------------
# %%
# Question 3
# A professor with two assistants, Jamie and Drew, wants an attendance 
# list of the students, in the order that they arrived in the classroom. 
# Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them 
# to the professor, who needs to combine them into one, in the order of 
# each student's arrival. Jamie emailed a follow-up, saying that her list is 
# in reverse order. Complete the steps to combine them into one list as follows:
#  the contents of Drew's list, followed by Jamie's list in reverse order, 
#  to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  list2.extend(list1)
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))
#OUTPUT
# ['Mike', 'Carol', 'Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Alice']

#--------------------------------------------------
# %%
# Question 4 
# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end, and returns a 
# list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].

def squares(start, end):
	return [ x**2 for x in range (start, end+1) ]

print(squares(2, 3)) 
#OUTPUT
#[4, 9]
print(squares(1, 5)) 
#OUTPUT
#[1, 4, 9, 16, 25]
print(squares(0, 10)) 
#OUTPUT
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# %%
# Question 5
# Complete the code to iterate through the keys and values of the car_prices dictionary,
# printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for car, price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
#OUTPUT
# Kia Soul costs 19000 dollars
# Lamborghini Diablo costs 55000 dollars
# Ford Fiesta costs 13000 dollars
# Toyota Prius costs 24000 dollars
#--------------------------------------------------
# %%
# # Question 6
# Taylor and Rory are hosting a party. They sent out invitations, 
# and each one collected responses into dictionaries, with names of 
# their friends and how many guests each friend is bringing. 
# Each dictionary is a partial list, but Rory's list has more current 
# information about the number of guests. Fill in the blanks to combine 
# both dictionaries into one, with each friend listed only once, 
# and the number of guests from Rory's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))
#OUTPUT
# {'David': 1, 'Nancy': 1, 'Robert': 4, 'Adam': 2, 'Samantha': 3, 'Chris': 5, 'Brenda': 3, 'Jose': 3, 'Charlotte': 2, 'Terry': 1}

#--------------------------------------------------
# %%
# # Question 7
# Use a dictionary to count the frequency of letters in the input string.
#  Only letters should be counted, not blank spaces, numbers, or punctuation. 
#  Upper case should be considered the same as lower case. For example, 
#  count_letters("This is a sentence.") should return 
#  {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  text=text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter not in result:
        result[letter]=0
    # Add or increment the value in the dictionary
      result[letter]+=1
  return result

print(count_letters("AaBbCc"))
#OUTPUT
# {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
#OUTPUT
# {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
#OUTPUT
#{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}



#--------------------------------------------------
# %%
# Question 8
#What do the following commands return when animal = "Hippopotamus"?
animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
#OUTPUT
# pop
# t
# us


#--------------------------------------------------
# %%
# Question 9
# What does the list "colors" contain after these commands are executed?
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
#OUTPUT
# ['red', 'white', 'yellow', 'blue']



# %%
# # Question 10
# What do the following commands return?
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
#OUTPUT
# dict_keys(['router', 'localhost', 'google'])
# %%