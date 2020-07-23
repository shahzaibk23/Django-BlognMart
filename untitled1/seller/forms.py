from django import forms
from .models import Seller

class CreateSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["profile_pic"]
