x= 2
try:
    raise Exception ("customer exception bro")
    #print(x/0)
    #if not type (x) is str :
     #   raise TypeError("only strings are allowed.")
except NameError:
    print('nameError means there is something is probably undefined')
except ZeroDivisionError:
    print('bro how can you divide somthing by 0.')
except Exception as error:
    print('error')
else:
    print ('no errors')
finally :
    print('whassap with the error bro')