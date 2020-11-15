import unittest
from main import create_app, db
from models.Item import Item

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

    def test_shop_index(self):
        response = self.client.get("/shop/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_item_create(self):
        response = self.client.post("/shop/", json={
            "name": "Test Item",
            "description": "Test Item Description",
            "price": 32.11
        })

        data = response.get_json()
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))

        item = Item.query.get(data["id"])
        self.assertIsNotNone(item)

    def test_item_delete(self):
        item = Item.query.first()

        response = self.client.delete(f"/shop/{item.id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        item = Item.query.get(item.id)
        self.assertIsNone(item)