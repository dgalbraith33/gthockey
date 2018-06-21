from django.test import Client, TestCase
from .models import ShopItem


class ShopTestCase(TestCase):

    def test_shop_list_only_visible(self):
        ShopItem(name="Test_Shown", price=0, description="Desc").save()
        ShopItem(name="Test_Hidden", price=0, description="Desc", visible=False).save()
        api = Client()
        items = api.get("/api/shop/")
        self.assertContains(items, '"name": "Test_Shown"')
        self.assertNotContains(items, '"name": "Test_Hidden"')

    def test_shop_item_shows_visible(self):
        item = ShopItem(name="Test_Shown", price=0, description="Desc")
        item.save()
        api = Client()
        items = api.get("/api/shop/%d/" % item.pk)
        self.assertContains(items, '"name": "Test_Shown"')

    def test_shop_item_hides_not_visible(self):
        item = ShopItem(name="Test_Hidden", price=0, description="Desc", visible=False)
        item.save()
        api = Client()
        items = api.get("/api/shop/%d/" % item.pk)
        self.assertNotContains(items, '"name": "Test_Hidden"', status_code=404)
