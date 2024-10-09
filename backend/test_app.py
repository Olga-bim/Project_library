import unittest
from backend import app
from app import create_initial_data
from extensions import db  
from models import customer, cart, book, loan 

class TestInitialData(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        create_initial_data()  # Вызываем функцию для создания начальных данных


    def test_initial_data(self):
        books = book.Book.query.all()
        customers = customer.Customer.query.all()

        self.assertEqual(len(books), 5)  # Проверяем, что 5 книг добавлено
        self.assertEqual(len(customers), 2)  # Проверяем, что 2 клиента добавлено

        self.assertEqual(books[0].author, 'Isaac Asimov')  # Проверяем автора первой книги
        self.assertEqual(customers[0].name, 'Alice')  # Проверяем имя первого клиента


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_customers_exist(self):
        self.assertGreater(customer.Customer.query.count(), 0, "Customers not found!")

    def test_books_exist(self):
        self.assertGreater(book.Book.query.count(), 0, "Books not found!")

    def test_loans_exist(self):
        self.assertGreater(loan.Loan.query.count(), 0, "Loans not found!")

if __name__ == '__main__':
    unittest.main()
