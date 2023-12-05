from bson import ObjectId
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# from models import Author, Quote
from mongoengine import connect
from pymongo import MongoClient

from .forms import QuoteForm, AuthorForm
from .models import Author, Quote
from .utils import get_mongodb, URI

client = MongoClient("mongodb://localhost:27018")

db = client.qp


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def about(request, _id):
    db = get_mongodb()
    author_info = db.authors.find_one({"_id": ObjectId(_id)})
    author_info1 = {'fullname': author_info.get("fullname"),
                    'born_date': author_info.get("born_date"),
                    'born_location': author_info.get("born_location"),
                    'description': author_info.get("description")
                    }
    return render(request, 'quotes/about.html', context={'author': author_info1})


def profile(request):
    return render(request, 'quotes/profile.html')


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():

            print(form.cleaned_data)
            author = db.authors.find_one({"fullname": form.cleaned_data.get('author').fullname})
            print(author)
            if not author:
                return redirect(to="quotes:add_author")
            else:
                tags = [tag.name for tag in form.cleaned_data['tags']]
                db.quotes.insert_one({"quote": form.cleaned_data['quote'],
                                      "tags": tags,
                                      "author": author.get('_id')})
            form.save()
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            print(form.cleaned_data)

            db.authors.insert_one({"fullname": form.cleaned_data['fullname'],
                                   "born_date": form.cleaned_data['born_date'],
                                   "born_location": form.cleaned_data['born_location'],
                                   "description": form.cleaned_data['description']
                                   })
            form.save()
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})
