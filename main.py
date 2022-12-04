# print('Hello world')
from random import *


class University:
    def __init__(self, title, faculty):
        self.title = title
        self.faculty = faculty
        self.budget = False
        self.student=True

    def studying(self, name):
        print(name + ' is studying')

    def isbudget(self):
        if self.budget == True:
            print('Congratulations! You are on budget!')
        else:
            print('Pay money and study')


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.mood = 0
        self.grades = 0


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 100

    def ask_budget(self):
        if self.progress > 30 or teacher.grades>15 and teacher.mood>10:
            self.gladness += 10
            univer.budget = True

    def say_hello(self):
        print('Hello!')

    def work(self):
        if univer.budget == False or self.money < 0:
            print('Work')
            self.money += 10
            self.gladness -= 3
            self.progress -= 1
            teacher.grades-=2
            teacher.mood-=1


    def to_study(self):
        if self.progress < 5:
            self.gladness -= 4
            self.progress += 5
            self.gladness -= 1
            teacher.grades+=5
            teacher.mood+=5
        if univer.budget == True:
            self.gladness -= 1
            print('Too much responsibility')
        elif univer.budget == False:
            self.money -= 5
    print('Time to study')


    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 2


    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 2
        self.money -= 5
        teacher.mood-=1
        teacher.grades-=2
        univer.budget = False
    def grades_check(self):
        if teacher.grades<-50:
            univer.student=False



    def is_alive(self):
        if self.progress < -10:
            print('You are bad')
            self.alive = False
        elif self.gladness <= 0:
            print('Dead inside')
            self.alive = False
        elif self.progress > 50:
            print('Amazing! You are so smart')
            self.alive = False
        elif univer.student==False:
            print('You are not student')
            self.alive=False


    def statics(self, univer):
        print('Gladness: ', self.gladness, 'Progress: ', self.progress, 'Money:', self.money)
        print('Budget: ', univer.budget,'Are you student?',univer.student)
        print('Teacher mood:',teacher.mood,'Grades:',teacher.grades)


    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(day)
        self.grades_check()
        live_cube = randint(1, 5)
        if live_cube == 1:
            self.to_study()
            self.ask_budget()
            univer.studying(self.name)
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.say_hello()
        elif live_cube == 5:
            self.work()
        self.statics(univer)
        self.is_alive()


univer = University('Step', 'Computer Science')
teacher = Teacher('Uchitel', 'Computer Science')
sanya = Student('Sanya')
for day in range(365):
    if sanya.alive == False:
        break
    sanya.live(day)

#