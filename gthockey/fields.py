from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

import requests

from .models import ShopItem, ShopItemOptionList, ShopItemCustomOption


class ReCaptchaField(forms.CharField):

    def __init__(self, *args, **kwargs):
        self.required = True
        super(ReCaptchaField, self).__init__(*args, **kwargs)

    def clean(self, value):
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': value
        })
        if not r.json()['success']:
            raise ValidationError('Error validating recaptcha')


class ItemField(forms.CharField):
    def clean(self, value):
        if type(value) != list:
            raise ValidationError('Must pass list to items')
        item_strs = []
        total_price = 0.0
        for item in value:
            item_str = ""
            shopitem = ShopItem.objects.get(pk=item['item_id'])
            item_str += shopitem.name
            price = shopitem.price
            if 'options' in item:
                for optionlistid in item['options'].keys():
                    shopitemoptionlist = ShopItemOptionList.objects.get(pk=int(optionlistid))
                    item_str += "\n" + shopitemoptionlist.display_name \
                                + ":" + item['options'][optionlistid]
            if 'custom_options' in item:
                for customoptionid in item['custom_options'].keys():
                    shopitemcustomoption = ShopItemCustomOption.objects.get(pk=int(customoptionid))
                    item_str += "\n" + shopitemcustomoption.display_name \
                                + ":" + item['custom_options'][customoptionid]
                    if shopitemcustomoption.extra_cost:
                        price += shopitemcustomoption.extra_cost
            total_price += price
            item_str += "\nPrice: $%.2f" % price
            item_strs.append(item_str)

        return ["Total: $%.2f" % total_price] + item_strs
