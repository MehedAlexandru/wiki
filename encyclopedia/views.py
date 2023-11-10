from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from markdown import markdown
import random as rnd
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/entry.html", {
        "title": name,
        "content": markdown(content),
    })

def add(request):
    if (request.method == "POST"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            if (util.get_entry(title)):
                return render(request, "encyclopedia/add.html", {
                    "error": "Entry already exists."
                })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=(title,)))
        else:
            return render(request, "encyclopedia/add.html", {
                "error": "Please fill in both fields."
            })

    return render(request, "encyclopedia/add.html")

def edit(request, name):
    if (request.method == "POST"):
        content = request.POST.get("content")
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("entry", args=(name,)))
    else:    
        content = util.get_entry(name)
        return render(request, "encyclopedia/edit.html", {
            "title": name,
            "content": content,
        })
        
def search(request):
    if (request.method == "POST"):
        query = request.POST.get("q")
        entryes = util.list_entries()
        results = []
        for entry in entryes:
            if query.capitalize() == entry.capitalize():
                return HttpResponseRedirect(reverse("entry", args=(entry.capitalize(),)))
            elif query in entry:
                results.append(entry)
        return render(request, "encyclopedia/results.html", {    
            "results": results,
        })
    

def random_page(request):
    entries = util.list_entries()
    random_entry = rnd.choice(entries)
    return HttpResponseRedirect(reverse("entry", args=(random_entry,)))
