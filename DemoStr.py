#DemoStr.py

data="<<<   spam and ham    >>>"
result=data.strip("<> ")
print(data)
print(result)
result=result.replace("spam", "spam egg")
print(result)
print("---리스트로 변환")
lst=result.split()
print(lst)
print("---하나의 문자열로 합치기---")
print(":)".join(lst))

#####
delete=":)".join(lst)
print(delete)
combine=delete.replace(":)", " ")
print(combine)

# print(combine.strip(':)'))

# strA='python is very powerful'
# print(len(strA))
# print(strA.capitalize())
# print(strA.upper())
# print("MBC2580".isalnum())
# print("MBC:2580".isalnum())
# print("2580".isdecimal())

# #정규표현식
# import re

# result=re.search("[0-9]*th", "__35th")
# print(result)
# print(result.group())

# #블럭 주석 처리 ctrl+/
# result=re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())

# result=re.search('apple', 'this is apple')
# print(result.group())

# result=re.search('\d{4}', '올해는 2024년 입니다. 뭘 했습니까?')
# print(result.group())

# result=re.search('\d{5}', '우리동네는 02020')
# print(result.group())