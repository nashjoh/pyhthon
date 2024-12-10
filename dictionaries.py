#dictonary
    #are used to store data values that are in key value pairs.

#method1 creating dictionary
shake = {
    "banana": "main component",
    "oats" : "second main character",
    "milk" : "the creator"
}


#method 2 creating dictionary
shake2 = dict(component1 = "almond", component2 = "dates", component3 = "cashewnuts")

print(shake)
print(type(shake))
print(len(shake))


print(shake2)
print(type(shake2))
print(len(shake2))

#access items

print(shake["milk"])
print(shake.get("banana"))


#list all keys

print(shake.keys())

#list all values

print(shake2.values())

#list of key values pairs as tuple

print(shake.items())

#varify a key exist

print("banana" in shake)
print("sugar"in shake)

#change values

shake2["component1"]="peanut butter"
shake2.update({"component4":"protien powder"})
print(shake2)

#remove items

print(shake2.pop("component1"))
print (shake2)

shake2["component5"]= "boost"
print(shake2)

print(shake2.popitem())#.popitem removes the last item added to the dict
print(shake2)

#delete and clear items
del shake2 ["component4"]
print(shake2)

shake2.clear()
print (shake2)

#   del shake2 ------------   #deletes the entire dictionery



#copy dictioneries

shake2 = shake.copy()
shake2["component2"] = "saudi dates"
print(shake2)
print(shake)

#COPY using constructor functiom

shake3 = dict(shake)
print(shake3)



##############   NESTED DICTIONARY    ###################

fruits={
    "one" : "orange",
    "two" : "apple"
}

veggies = {
    "three": " carrots",
    "four": "potato"
}

fruits_n_veggies ={
    "fruits" : fruits,
    "veggies" : veggies
    }

print(fruits_n_veggies)
print(fruits_n_veggies["fruits"]["one"])


########## SETS  ##############
#no duplicates are allowed or similar item on the set



#true is a dupe of 1 , false is a dupe of 0


nums = {1,2,3,4}

nums2 = set((1,2,3,4))



print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

#check if a value is in a set

print(2 in nums)

#add a new element to a set

nums.add(8)
print(nums)

#add a elements from one set to another

morenums = {5,6,7}
nums.update(morenums)
print(nums)

#merge two set to create a new set

one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)


#keep only the duplicate


one = {1,2,3}
two = {2,3,7}

one.intersection_update(two)
print(one)

#keep everything except the duplicate

one = {1,2,3}
two = {2,3,7}

one.symmetric_difference_update(two)
print(one)