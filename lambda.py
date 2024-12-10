#are single expression that returns a value.
squared = lambda num : num * num

print(squared(2))


addTwo =lambda num : num + 2

print(addTwo(12))

sum_total= lambda a,b : a + b

print(sum_total(8,2))



##########################


def  funcBuilder(x):
    return lambda num : num + x
addTen = funcBuilder (10)
adddTwenty = funcBuilder (20)

print(addTen (7))
print(adddTwenty (7))

#########################


##########HIGER ORDER FUNCTIONS########
    #FUNCTION THAT TAKES ONE OR MORE FUNCTIONS AS ARGUMENTS OR RETURNS FUNCTIONS THAT ARE RESULTS

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num: num * num , numbers)

print (list(squared_nums))

####################




odd_nums = filter(lambda num: num % 2 != 0,numbers)#filter filters the true function here

print(list(odd_nums))




from functools import reduce

 

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr: acc + curr,numbers,10)#reduce add up numbers here

print(total)

print(sum(numbers,10))#sum is a build in function to add up numbers





name = ['anna','sara george', 'jingglebells']

char_count = reduce(lambda acc , curr : acc + len(curr), name ,0)

print(char_count)

