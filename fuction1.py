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

#global parameter
x=5
def func(a):
    return a+x
#iCall
print(func(1))

def func2(a):
    x=1
    return a+x

#iCall
print(func2(1))

#print(globals())

#add
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# iCall
print(union('ham', 'egg'))
print(union('ham', 'egg', 'spam'))

#기본값 명시
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(6))

#키워드 인자
def connectURI(server, port):
    strURL = 'http://' + server + ':' + port
    return strURL

#호출
print(connectURI('multi.com', '80'))
print(connectURI(port = '80', server = 'multi.com'))

#일회성 함수

g = lambda x,y:x*y
print(g(3,4))
print((lambda x:x*x)(3))
print(globals())
