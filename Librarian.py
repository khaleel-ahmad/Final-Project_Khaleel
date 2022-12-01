import datetime
from data import clients, books, borrowed_count, borrowed, available_count, orders_count


class Librarian:
    __id = 1

    def __init__(self, fullname, age, id_no, employment_type='FULL'):
        self.id = Librarian.__id
        Librarian.__id += 1
        self.fullname = fullname
        self.age = age
        self.id_no = id_no
        self.employment_type = employment_type

    def borrow(self, book_id, client_id):
        # check if book is exists in the list
        if book_id not in books:
            raise Error('book is not exists')

        # get the book instance
        book = books[book_id]

        #  check if the book's status is active
        if book.status != 'ACTIVE':
            raise Error('book is in-active')

        # check if client is exists in the list
        if client_id not in clients:
            raise Error('client is not exists')

        # get the client
        client = clients[client_id]

        order = Order(datetime.datetime.now(), client_id, book_id, 'ACTIVE')
        borrowed[order.id] = order

        book.status = 'IN-ACTIVE'
        available_count -= 1
        orders_count += 1
        borrowed_count += 1

    def returnBook(self, borrowing_id):
        if borrowing_id not in borrowed:
            raise Error('order is not exists')

        order = borrowed[borrowing_id]
        book = books[order.book_id]
        del borrowed[order.id]
        book.status = 'ACTIVE'

        available_count += 1
        borrowed_count -= 1
        orders_count -= 1

    def __str__(self):
        return (
            f'id: {self.id},  fullname: {self.fullname}, age: {self.age}, employment_type: {self.employment_type},  id_no: {self.id_no} ')