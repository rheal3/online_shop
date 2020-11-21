import unittest
from main import create_app, db
from models.Order import Order
from models.OrderShipping import OrderShipping

class TestShop(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_order_index(self):
        response = self.client.get("/orders/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_order_create(self):
        shipping = self.client.post("/orders/shipping", json={
            "address": "123 street",
            "state": "QLD",
            "zip_code": "1234",
            "first_name": "Edward",
            "last_name": "Scissorhands"
        }).get_json()

        response = self.client.post("/orders/?shipping_id=1", json={})

        data = response.get_json()

        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))
        self.assertTrue(bool("date_ordered" in data.keys()))
        self.assertTrue(bool("shipped" in data.keys()))

        order = Order.query.get(data["id"])
        self.assertIsNotNone(order)

    def test_shipping_create(self):
        response = self.client.post("/orders/shipping", json={
            "address": "123 street",
            "state": "QLD",
            "zip_code": "1234",
            "first_name": "Edward",
            "last_name": "Scissorhands"
        })

        data = response.get_json()
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))
        self.assertTrue(bool("address" in data.keys()))
        self.assertTrue(bool("first_name" in data.keys()))
