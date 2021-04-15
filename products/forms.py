from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='The Title', widget=forms.TextInput(
        attrs={
            'placeholder': 'title',
            'id': 'eng_name',
            "class": "engs_class",

        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
                attrs={
                    'cols': 25,
                    'rows': 8
                }
            ))
    price = forms.DecimalField(initial=199.99)
    # email =forms.EmailField()
    class Meta:
        model  = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    
    # def clean_email(self, *args, **kwargs):
    #     mail = self.cleaned_data.get("email")
    #     print(f"This is MAIL: {mail}")
    #     if not mail.endswith("com"):
    #         raise ValidationError("Email not valid!")
    #     return mail
        
        
        
    
# Django Purre `FORM`
# class RawProductForm(forms.Form):q
    # title = forms.CharField(label= 'The Title', widget=forms.TextInput(
    #     attrs= {
    #         'placeholder': 'title',
    #         'id': 'eng_name',
    #         "class": "engs",
            
    #     }
    # ))
#     description = forms.CharField(required= True, widget=forms.Textarea(
#         attrs={
#             'cols': 25,
#             'rows': 8
#         }
#     ))
#     price = forms.DecimalField()
    
