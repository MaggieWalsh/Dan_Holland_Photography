from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Create ContactForm class """
    class Meta:
        """ Fields to render from model """
        model = Contact
        exclude = ('user', 'email_date')
        widgets = {
            'rate_us': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'John',
            'surname': 'Doe',
            'email': 'johndoe@test.com',
            'order_number': "This can be found in the order confirmation email you received",
            'enquiry': "Please let us know how we can help",
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rate_us':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder