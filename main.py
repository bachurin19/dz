class Human():
        def __init__(self, name):
            self.name = name
            self.age = 0
            self.clever = 5
        def live(self):
            print(self.name, 'is alive')
        def sleep(self):
            print(self.name,'is sleeping')
        def statistics(self):     
            print('Name:',self.name,'Clever:',self.clever, 'Age:',self.age)
            
class Student(Human):
    def __init__(self,name):
        super().__init__(name)
        self.grades=0
    def live(self):
        super().live()
        print('What a great day at',self.name,'\'s school')
    def studiyng(self):
        print(self.name,'is studiyng')
        self.grades+=2
        self.clever+=10
    def do_hm(self):
        print(self.name,'is doing homework')
        self.grades+=4
        self.clever+=10
class Teacher(Human):
    def __init__(self,name):
        super().__init__(name)
        self.money=100
        self.clever=100
    def live(self):
        super().live()
        print('What a wonderful day of teaching,',self.name)
    def teaching(self):
        print(self.name,'is teaching')
        self.money+=10
        
    def check_hm(self):
        self.money+=10
        print(self.name,'is checking homework')
obj = Student('Bob')
obj2 = Teacher('Clara')
obj.live()
obj2.live()
obj2.teaching()
obj.studiyng()

obj.do_hm()
obj2.check_hm()
obj.sleep()
obj2.sleep()
obj.statistics()
obj2.statistics()

    