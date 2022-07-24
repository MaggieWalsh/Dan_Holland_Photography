from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Create ContactForm class """
    class Meta:
        """ Fields to render from model """
        model = Contact
        exclude = ('user', 'email_date')

    def __init__(self, *args, **kwargs):
        """ Add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'surname': 'Last name',
            'email': 'Email',
            'order_number': 'Order number',
            'enquiry': 'Enquiry',
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['required'] = True
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder