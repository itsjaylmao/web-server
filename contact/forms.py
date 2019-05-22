from django import forms

CHOICES = (
    ('Other', "What's this about?"),
    ('Branding', 'Branding'),
    ('Website', 'Website'),
    ('E-commerce', 'E-commerce'),
    ('Getting a Quote', 'Getting a Quote'),
    ('Other', 'Other')
)

class ContactForm(forms.Form):
    from_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "contact-form-field w-input",
            'autofocus': "true",
            'maxlength': "256",
            'data-name': "Name",
            'style': "opacity:0",
            'placeholder': "Name",
            'data-w-id': "64b41296-4951-47b6-9936-2532b2af6a6d",
        })
    )
    from_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "contact-form-field w-input",
            'maxlength': "256",
            'data-name': "Email",
            'style': "opacity:0",
            'placeholder': "Email",
            'data-w-id': "64b41296-4951-47b6-9936-2532b2af6a70",
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': "contact-form-field textarea w-input",
            'maxlength': "5000",
            'style': "opacity:0",
            'data-w-id': "27515d10-5add-9c89-a789-ca6fb26596d6",
        })
    )
    subject = forms.ChoiceField(
        choices=CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': "contact-form-field w-select",
            'data-name': "Subject",
        })
    )

