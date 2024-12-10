#constuctor function

pizza =str("pepperonni")
print(type(pizza))
print (type (pizza)==str)
print (isinstance(pizza,str))


#concatation

first = "nakshathra"
last = "johnson"
fullname = first +" " + last
print (fullname)

# casting a number to a string

decade = str(1980)
print (type(decade) )
print (decade)

#multiple lines

multiline ='''
how are you       all good'''
print (multiline)

#escaping special characters
sentence = 'I\'m alright \t thankyou!\n\n have a good day'
#\ escapes the ' from i'am
#\t is tab
#\n is newline
print (sentence)


#tring methods

print (first)
print (first.lower())#print everything in lowercase
print(first.upper())#print everything in uppercase

print (first.title())#makes into title formate with first letter capital
print(first.replace('k','t'))#replace something with the other
print (first)

print (len(first))
first +="             "
print (len(first))#len()returns length
print (len(first.lstrip()))#removes the whitespaces from left side
print (len(first.rstrip()))#removes whitespaces from the right hand side

#build a menu

title = "menu".upper()
print (title.center(10,"="))#puts the title to the centre 
print ("coffee".ljust (16,".")+"$1".rjust(4) )#.ljust  justfies the space on left so is rjust space in right
print ("muffin".ljust (16,".")+"$1".rjust(4) )
print ("pancake".ljust (16,".")+"$1".rjust(4) )

#string index values
print(first[1])
print(first[-1])
print(first[5])
print(first[0:5])

#some methods return boolean values
print(first.startswith("n"))
print(first.endswith("n"))

#numeric datatype
price = 100
print(type(price))
best_price = int(180)
print (isinstance(best_price,int))

#float_types
gpa = 4.2
y = float(4.4)
print (type(gpa))
print (type(y))