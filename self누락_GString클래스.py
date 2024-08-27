#전역변수 초기화
strName = "Not Class Member"

class DemoString:
    #관용적인 표현으로 첫번째 인스턴스는 self 사용
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(self.strName)

#인스턴스 생성
d = DemoString()
d.set("First Message")
d.print()
