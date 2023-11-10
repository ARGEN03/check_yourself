"=1="
class Auto:
    def ride(self):
        print('Riding on a ground')

class Boat:
    def swim(self):
        print('Floating on water')

class Amphibian(Auto,Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim()

"=2="
class ContactList(list):
    def search_by_name(self,name):
        return [i for i in self if name.lower() in i.lower() ]

obj = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(obj.search_by_name('Olya'))
