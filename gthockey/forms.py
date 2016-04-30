from django import forms
from captcha.fields import ReCaptchaField


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
    email = forms.CharField(required=True, label="Email")
    phone = forms.CharField(required=False, label="Phone Number")
    birth = forms.DateField(required=False, label="Date of Birth")
    hometown = forms.CharField(required=False, label="Hometown")
    status = forms.ChoiceField(choices=STATUS_CHOICES,label="Status")
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
    email = forms.CharField(required=True, label="Email")
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

    RELATIONS = (('1', "I'm a GT Hockey Alum"),
                 ('2', "I'm a regular GT Alum"),
                 ('3', "I'm related to GT Hockey player"),
                 ('4', "I'm a regular fan"))

    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    relation = forms.ChoiceField(widget=forms.RadioSelect, choices=RELATIONS, label="")
    captcha = ReCaptchaField(label="")