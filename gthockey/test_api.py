from django.test import Client, TestCase
from .models import ShopItem


class ShopListTestCase(TestCase):

    def test_shop_list_only_visible(self):
        ShopItem(name="Test_Shown", price=0, description="Desc").save()
        ShopItem(name="Test_Hidden", price=0, description="Desc", visible=False).save()
        api = Client()
        items = api.get("/api/shop/")
        self.assertContains(items, '"name": "Test_Shown"')
        self.assertNotContains(items, '"name": "Test_Hidden"')
