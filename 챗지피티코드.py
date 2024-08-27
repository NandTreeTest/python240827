class Person:
    def __init__(self, id, name):
        # id와 이름을 초기화하는 생성자
        self.id = id
        self.name = name

    def printInfo(self):
        # Person 객체의 정보를 출력하는 메서드
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        # Person 클래스의 생성자를 호출하여 id와 이름을 초기화하고,
        # 추가적으로 직함(title)을 초기화하는 생성자
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        # Manager 객체의 정보를 출력하는 메서드
        # Person 클래스의 printInfo를 먼저 호출한 후, 직함을 추가로 출력
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        # Person 클래스의 생성자를 호출하여 id와 이름을 초기화하고,
        # 추가적으로 기술(skill)을 초기화하는 생성자
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        # Employee 객체의 정보를 출력하는 메서드
        # Person 클래스의 printInfo를 먼저 호출한 후, 기술을 추가로 출력
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
if __name__ == "__main__":
    # 1. Person 객체 생성 및 printInfo() 테스트
    p1 = Person(1, "Alice")
    p1.printInfo()  # ID: 1, Name: Alice 출력

    # 2. Manager 객체 생성 및 printInfo() 테스트
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()  # ID: 2, Name: Bob, Title: Project Manager 출력

    # 3. Employee 객체 생성 및 printInfo() 테스트
    e1 = Employee(3, "Charlie", "Python Developer")
    e1.printInfo()  # ID: 3, Name: Charlie, Skill: Python Developer 출력

    # 4. 또 다른 Person 객체 생성 및 printInfo() 테스트
    p2 = Person(4, "David")
    p2.printInfo()  # ID: 4, Name: David 출력

    # 5. 또 다른 Manager 객체 생성 및 printInfo() 테스트
    m2 = Manager(5, "Eve", "Team Lead")
    m2.printInfo()  # ID: 5, Name: Eve, Title: Team Lead 출력

    # 6. 또 다른 Employee 객체 생성 및 printInfo() 테스트
    e2 = Employee(6, "Frank", "Data Scientist")
    e2.printInfo()  # ID: 6, Name: Frank, Skill: Data Scientist 출력

    # 7. Manager 클래스의 title 속성 변경 후 printInfo() 테스트
    m1.title = "Senior Project Manager"
    m1.printInfo()  # 변경된 Title: Senior Project Manager 출력

    # 8. Employee 클래스의 skill 속성 변경 후 printInfo() 테스트
    e1.skill = "Full Stack Developer"
    e1.printInfo()  # 변경된 Skill: Full Stack Developer 출력

    # 9. Person 클래스의 name 속성 변경 후 printInfo() 테스트
    p1.name = "Alicia"
    p1.printInfo()  # 변경된 Name: Alicia 출력

    # 10. 다양한 클래스를 리스트에 담아 순차적으로 printInfo() 호출
    people = [p1, p2, m1, m2, e1, e2]
    for person in people:
        person.printInfo()  # 각각의 객체 정보가 순차적으로 출력됨
