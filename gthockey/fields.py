from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

import requests


class ReCaptchaField(forms.CharField):

    def __init__(self, *args, **kwargs):
        self.required = True
        super(ReCaptchaField, self).__init__(*args, **kwargs)

    def clean(self, values):
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': values
        })
        if not r.json()['success']:
            raise ValidationError('Error validating recaptcha')
