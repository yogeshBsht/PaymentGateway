from datetime import datetime
import unittest
from app import create_app, db
from app.models import Payment
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class PaymentModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_check_payment_data(self):
        data = {
                "amount": "100",
                "currency": "USD",
                "card_type": "credit-card",
                "card": {
                        "number": "411111111111",
                        "expiration_month": "5",
                        "expiration_year": "2022",
                        "cvv": "111"
                        }
                }

        # Case-0: Correct payment & card data
        p = Payment()
        p.from_dict(data)
        self.assertEqual(p.status, 'success')

        # Case-1: Amount is negative
        data1 = data.copy()
        data1['amount'] = '-100'
        p.from_dict(data1)
        self.assertEqual(p.status, 'failure')

        # Case-2: Payment mode other than debit & credit card
        data2 = data.copy()
        data2['card_type'] = 'UPI'
        p.from_dict(data2)
        self.assertEqual(p.status, 'failure')

        # Case-3: Incorrect length of card number
        data3 = data.copy()
        data3['card']['number'] = '0123456789'
        p.from_dict(data3)
        self.assertEqual(p.status, 'failure')

        # Case-4: Card is expired
        data4 = data.copy()
        data4['card']['expiration_year'] = '2021'
        p.from_dict(data4)
        self.assertEqual(p.status, 'failure')

        # Case-5: CVV number is non-numeric
        data5 = data.copy()
        data5['card']['cvv'] = '12A'
        p.from_dict(data5)
        self.assertEqual(p.status, 'failure')


if __name__ == '__main__':
    unittest.main(verbosity=2)