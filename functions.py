#functions are reuseable type of code.
def hello():
    print("hello world!")
hello()


def sum(num1,num2):
    print(num1 + num2)

sum(2,3)
sum(100,200)
sum(3,7)



def sum(num1,num2):
    if (type(num1) is not int or type(num2)is not int):
        return
    return num1 + num2

total = sum(2,3)
print(total)



def multiple_items(*args):#the astrick helps to return multiple unknown items
    print(args)
    print(type(args))

multiple_items("mama","mia")


def multi_named_items(**kwargs):         #key word arguments 
    print (kwargs)
    print(type(kwargs))

multi_named_items(first = "anna",last="george")