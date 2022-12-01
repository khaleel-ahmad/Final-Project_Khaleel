class Book:
    __id = 1

    def __init__(self, title, description, author, status="ACTIVE"):
        self.id = Book.__id
        Book.__id += 1
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    def __str__(self):
        return (
            f'id: {self.id},  title: {self.title}, description: {self.description}, author: {self.author},  status: {self.status} ')
