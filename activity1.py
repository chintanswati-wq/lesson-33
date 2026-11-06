from abc import ABC, abstractclassmethod

class Absclass(ABC):

    def print(self,x):
        print("passed value: ", x)

    def task(self):
             print("we are inside absclass")

class test_class(Absclass):
    def task(self):
        print("we are inside Absclass task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)