user = ['anna','mariya','anikha']
print(user[0])
print(user.index('mariya'))
print(user[0:2])
print(user[0:])
print(user[0:-1])


print(len(user))
user.append('feba')
print(user)


user +=['nayana']#make sure to put bracket else ech letter returns
print(user)

user.extend(['christina,aswitha'])
print(user)


user.insert(-1,'gayathri')
print(user)

user[0:0]=['nakshathra']#adding a new item to the list without replacing anything
print(user)

user.remove('gayathri')
print(user)


print(user.pop())#removes and return the last element from the the list by default. 
print(user)

del user[4]#delete the element in the list.also could use for deleting he entire list
print(user)

users1 =['34','matt','true']
print(users1)
users1.clear()#will clear the list

user[0:1]=['Anna']

#sorts into alphabetical order (first consider the capital letter while sorting.)
user.sort()
print(user)


user.sort(key=str.lower)#sorts the elements in alphabetical order without consideringn capital letter
print(user)

nums = [3,8,5]
nums.reverse()
print(nums)

nums.sort(reverse = True)
print(nums)

#make a copy of nums 
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]





#tuples
#cannot be changed

mytuple = tuple(('nakshathra','43','true'))
print (mytuple)

#to modify anything to a tuple convert tuple to a list and then back to tuple
newlist = list(mytuple)
newlist.append('neil')
newtuple = tuple (newlist)  
print(newtuple)

print(newtuple.count(43))#counts the occurace of the required element

#unpacking a tuple

latest_tuple = (1,2,3,8)

#putting values to the varible names

(one,two,*hey)=latest_tuple
print (one)
print (two)
print (hey)


(one,*two,hey)=latest_tuple
print (one)
print (two)
print (hey)
