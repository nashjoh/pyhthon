person = "naksh"
coins = 3

print ("\n" + person + " has " + str(coins) + " coins left . ")


#formatting the strings
#  the above print statement formatted into a diffferent method same result.

#method 1 
message = "\n %s has %s  coins left ." % (person,coins)
print(message)


#format method

message = "\n {} has {} coins left ." .format(person,coins)
print(message)

#method 2  assigning the values
message = "\n {0} has {1} coins left ." .format(person,coins)
print(message)

#method 3 
message = "\n {person} has {coins} coins left ." .format(person = person,coins = coins)
print(message)

# method 4  getting from the dictioneries

player = {'person': 'naksh','coins':'3'}
message = "\n {person} has {coins} coins left ." .format(**player) 
print(message)



######## f-strings ########## this is the wayyyyy!


message = f"\n {person} has {coins} coins left."
print (message)


message = f"\n {person} has {2*5} coins left."
print (message)


message = f"\n {person.lower()} has {2*5} coins left."
print (message)


message = f"\n {player ['person']} has {2*5} coins left."
print (message)

######## you can pass formatting options###########

num = 10 
print(f"\n2.25 times{num}is {2.25*num:.2f}")#here f means fixed. and .2 means 2 decimak digit.

for num in range(1,11):
    print(f"\n2.25 times{num}is {2.25*num:.2f}")


for num in range(1,11):
    print(f"\n{num}divided by 4.52 is {num/4.52:.2%}")
      



