from django import forms
from .models import Category, Cuisine

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = ['name', 'description', 'category']
