# function1.py
# 1.func defintion
def setValue(input):
    #local parameter
    x = input
    print('지역변수:', x)

# 2 iCall
retValue = setValue(5)  
print(retValue) 

# iProc
def swap(x,y):
    return y,x

# iCall
retValue = swap(3,4)
print(retValue)