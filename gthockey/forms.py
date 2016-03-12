from django import forms


class ProspectForm(forms.Form):

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
    comments = forms.CharField(required=False, widget=forms.Textarea)

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