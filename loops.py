#while loop execute a block of code while the condition is true

value = 1
while value < 10 :
    print(value)
    if value  == 5:
        break
    value += 1


print("       ")

while value <= 10 :
    value += 1
    if value  == 5:
        continue
    print(value)
else:
    print("the value is now equal to "+ str(value))




print("")






#for loop
#iterate over a sequence

names = ["dave","sara","john"]
for x in names:
    print (x)
    
for x in "Mississippi":
    print(x)


for x in names:
        if  x == "sara":
            break
        print(x)


for x in names:
        if  x == "sara":
            continue
        print(x)



for x in range(4):
    print (x)


print("             ")


for x in range(2,4):
    print (x)

print("")


for x in range(0,55,5):
    print (x)
else:
     print("thats it my kinder")


     print("                                 ")


names = ["anna","sara","george"]
actions = ["ran","eat","played"]

for n in names:
     for a in actions:
          print(n +" " + a +".")


print("")
              #two different results on exchanging the for loops

for a in actions:
    for n in names:
    
          print(n +" " + a +".")








