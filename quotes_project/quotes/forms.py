from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, Select, ModelMultipleChoiceField, \
    SelectMultiple
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, max_length=200, required=True, widget=TextInput())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), widget=Select(attrs={"class": "form-select"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=200, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=200, required=True, widget=TextInput())
    description = CharField(min_length=3, max_length=2000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']