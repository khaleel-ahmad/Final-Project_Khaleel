class Client:
    __id = 1
    def __init__(self, id_no, name, age, phone_number):
        self.id = Client.__id
        Client.__id += 1
        self.id_no = id_no
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return (f'id: {self.id},  name: {self.name}, age: {self.age}, phone_number: {self.phone_number},  id_no: {self.id_no} ')
