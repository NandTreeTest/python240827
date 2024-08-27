# DemoDict.py

#사전식 구조
colors = {'apple':'사과', 'banana':'바나나'}
print(colors)
print(len(colors))
#search
print(colors['apple'])
#input
colors['cherry']='red'
print(colors)
#modify
colors['apple']='pink'
#delete
del colors['banana']
print(colors)

#loop
for item in colors.items():
    print(item)

print('---key, value---')
for k,v in colors.items():
    print(k,v)