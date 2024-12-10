name = "naksh"
count=1

    




def another():
    color = "blue"
    global count  #accessing the global variable by local and modifying it
    count +=1
    print(count)
    def greeting(name):
        nonlocal color# modifying color from globl variable by global keyword nonlocal
        color = "red"
        print(color)
        print(name)

    greeting("dave")

another()
    