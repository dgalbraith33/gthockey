from django import forms
from .fields import ReCaptchaField, ItemField


class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''


class ProspectForm(MyForm):

    SUBJECT = "Prospective Player"

    STATUS_CHOICES = [
        (0, "-- Select one --"),
        (1, 'Current Tech Student'),
        (2, 'Incoming Freshman'),
        (3, 'Admitted to Tech (Undecided)'),
        (4, 'Applying to Tech'),
        (5, 'High School Senior'),
        (6, 'High School Junior'),
        (7, 'Other')
    ]

    POSITION_CHOICES = [
        (0, '-- Select one --'),
        (1, 'Forward'),
        (2, 'Defense'),
        (3, 'Goalie')
    ]

    name = forms.CharField(required=True, label="Full Name")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField(required=False, label="Phone Number")
    birth = forms.DateField(required=False, label="Date of Birth")
    hometown = forms.CharField(required=False, label="Hometown")
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Status")
    experience = forms.CharField(required=False, label="Experience Level")
    position = forms.ChoiceField(choices=POSITION_CHOICES, label="Position")
    comments = forms.CharField(required=False, widget=forms.Textarea, label="Comments")
    captcha = ReCaptchaField(label="")

    @staticmethod
    def get_subject():
        return ProspectForm.SUBJECT

    def get_message(self):
        message = ""
        message += "Name: %s\n" % self.cleaned_data['name']
        message += "Email: %s\n" % self.cleaned_data['email']
        message += "Phone: %s\n" % self.cleaned_data['phone']
        message += "Date of Birth: %s\n" % self.cleaned_data['birth']
        message += "Hometown: %s\n" % self.cleaned_data['hometown']
        message += "Status: %s\n" % ProspectForm.STATUS_CHOICES[int(self.cleaned_data['status'])][1]
        message += "Experience: %s\n" % self.cleaned_data['experience']
        message += "Position: %s\n" % ProspectForm.POSITION_CHOICES[int(self.cleaned_data['position'])][1]
        message += "Comments: %s\n" % self.cleaned_data['comments']
        return message


class ContactForm(MyForm):

    SUBJECT = "GT Hockey Contact Form"

    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=True, label="Subject")
    message = forms.CharField(required=True, widget=forms.Textarea, label="Message")
    captcha = ReCaptchaField(label="")

    def get_subject(self):
        return self.SUBJECT

    def get_message(self):
        message = ""
        message += "From: %s\n" % self.cleaned_data['name']
        message += "Email: %s\n" % self.cleaned_data['email']
        message += "Subject: %s\n" % self.cleaned_data['subject']
        message += "\n%s" % self.cleaned_data['message']
        return message


class EmailListForm(MyForm):

    SUBJECT = "Email List Sign Up"

    RELATIONS = (('1', "I'm a GT Hockey Alum"),
                 ('2', "I'm a regular GT Alum"),
                 ('3', "I'm related to GT Hockey player"),
                 ('4', "I'm a regular fan"))

    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    relation = forms.ChoiceField(widget=forms.RadioSelect, choices=RELATIONS, label="")
    captcha = ReCaptchaField(label="")

    @staticmethod
    def get_subject():
        return EmailListForm.SUBJECT

    def get_message(self):
        message = ""
        message += "Name: %s\n" % self.cleaned_data['name']
        message += "Email: %s\n" % self.cleaned_data['email']
        message += "Relation: %s\n" % EmailListForm.RELATIONS[int(self.cleaned_data['relation'])][1]
        return message


class GolfForm(MyForm):

    SUBJECT = "Golf Sign Up"

    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    foursome = forms.CharField(required=False, widget=forms.Textarea, label="Foursome Members")

    @staticmethod
    def get_subject():
        return GolfForm.SUBJECT

    def get_message(self):
        message = ""
        message += "Name: %s\n" % self.cleaned_data['name']
        message += "Email: %s\n" % self.cleaned_data['email']
        message += "Foursome:\n %s\n" % self.cleaned_data['foursome']
        return message


class OrderForm(MyForm):
    SUBJECT = "GT Hockey Order Placed"

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    message = forms.CharField(required=False)
    items = ItemField(required=True)
    captcha = ReCaptchaField(label="")

    def get_total_cost(self):
        pass

    @staticmethod
    def get_subject():
        return OrderForm.SUBJECT

    def get_message(self):
        message = "An order has been placed!\n\n"
        message += "Name: %s\n" % self.cleaned_data['name']
        message += "Email: %s\n" % self.cleaned_data['email']
        message += "Phone: %s\n" % self.cleaned_data['phone']
        message += "Address:\n%s\n" % self.cleaned_data['address']
        message += "Custom message: %s\n\n" % self.cleaned_data['message']
        message += "Items:\n"
        message += "\n\n".join(self.cleaned_data['items'])
        return message

    def get_customer_subject(self):
        return "Your GT Hockey order has been placed."

    def get_customer_message(self):
        message = "Hi %s, thank you for ordering from GT Hockey!\n\n" % self.cleaned_data['name']
        message += "Please keep in mind that we are a student-run organization. While "
        message += "we strive to fulfill your order as fast as possible, some delays may "
        message += "be inevitable.\n\n"
        message += "One great way to help us expedite the process would be to pay for your "
        message += "order right now on paypal. You can follow this link and pay the total listed below!\n\n"
        message += "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2MEXK924Y38Z4\n\n"
        message += "Items:\n"
        message += "\n\n".join(self.cleaned_data['items'])


        return message
