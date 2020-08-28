# Modules
def iseven(starting,ending):
    for i in range(starting,ending):
        if i%2==0:
            print(i, end=' ')

## restart kernel
###required, not required arguments            
def isodd(starting=1,ending=10):
    for i in range(starting,ending):
        if i%2!=0:
            print(i, end=' ')
              
def add(x,y):
    return (x+y)

def sub(x,y):
    return (x-y)