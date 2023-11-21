"=1="
class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return "Задача под таким ключом уже существует"
        self.todos[key] = todo
        return self.todos

class ReadMixin:
    def read(self):
        return sorted(self.todos.items())

class UpdateMixin:
    def update(self, key, new_value):
        if key in self.todos:
            self.todos[key] = new_value
            return self.todos
        return 'Задачи с таким ключом не существует'

class DeleteMixin:
    def delete(self, key):
        if key in self.todos:
            res = self.todos.pop(key)
            return res
        return 'Задачи с таким ключом не существует'

class ToDo(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    todos = {}

    def set_deadline(self, deadline):
        from datetime import datetime
        deadline = datetime.strptime(deadline, '%d/%m/%Y')
        today = datetime.now()
        day = (today - deadline).days
        return day

task = ToDo()
print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2, 'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('31/12/2021'))
print(task.todos)

"=2="
# class Person:
#     __name = None
#     __last_name = None
#     __age = None
#     __email = None

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self,new_name):
#         self.__name = new_name
#         return self.__name
    
#     @property
#     def last_name(self):
#         return self.__last_name
    
#     @last_name.setter
#     def last_name(self,new_last_name):
#         self.__last_name = new_last_name
#         return self.__last_name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self,new_age):
#         self.__age = new_age
#         return self.__age
    
#     @property
#     def email(self):
#         return self.__email
    
#     @email.setter
#     def email(self,new_email):
#         self.__email = new_email
#         return self.__email

# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

"=3="
# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')
# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voice()

# to_pet(rex)
# to_pet(barsik)
