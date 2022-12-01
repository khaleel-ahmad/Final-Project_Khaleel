class Order:
    __id = 1

    def __init__(self, date, client_id, book_id, status='ACTIVE'):
        self.id = Order.__id
        Order.__id += 1
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status

    def __str__(self):
        return (
            f'id: {self.id},  date: {self.date}, client_id: {self.client_id}, book_id: {self.book_id},  status: {self.status} ')
