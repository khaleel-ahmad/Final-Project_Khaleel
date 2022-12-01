from Book import Book
from Client import Client
from Librarian import Librarian
from data import clients, books, librarians

#  create client and insert it to clients collections.
client = Client("0597662116", "khaleel", 25, '1')
client = Client("0595892565", "Ahmad", 22, '2')
client = Client("0596985248", "Ali", 25, '3')

clients[client.id] = client

# create librarian and insert int to librarians collection.
librarian = Librarian('Sami Ali', 25, '503684398', 'FULL')
librarian = Librarian('Mphammed Helo', 30, '503684399', 'part time')

librarians[librarian.id] = librarian


# Create Books
book = Book('Friends, Lovers, and the Big Terrible Thing: A Memoir',
            "The BELOVED STAR OF FRIENDS takes us behind the scenes of the hit sitcom and his struggles with addiction in this “CANDID, DARKLY FUNNY...POIGNANT” memoir  ", "Matthew Perry ", "ACTIVE")
books[book.id] = book

book = (Book('The Extraordinary Life of an Ordinary Man: A Memoir',
             "The raw, candid, unvarnished memoir of an American icon. The greatest movie star of the past 75 years covers everything ",
        "Paul Newman", "IN-ACTIVE"))
books[book.id] = book

book = (Book('التأريخ العربي وتاريخ العرب، كيف كتب وكيف يكتب؟: الإجابات الممكنة',
        "ان الوثائق تُبطل استناد التاريخ إلى أخبار الإخباريين أو أصحاب التراجم", "إبراهيم القادري بوتشيش ووجيه كوثراني", "IN-ACTIVE"))
books[book.id] = book


# fffff
