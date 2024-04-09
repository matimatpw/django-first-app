from django.shortcuts import render

from .froms import ContactForm

def contact (request):

    if request.method == "GET":
        form = ContactForm()

    else:
        raise NotImplementedError


    return render(request, "contact.html", {"form":form})