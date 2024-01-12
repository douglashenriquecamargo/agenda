from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "title": "Contatos",
    }
    return render(request, 'contact/index.html', context)


def search(request):
    search_value = request.GET.get("q", "").strip()

    if search_value == '':
        return redirect('contact:index')

    contact = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value)|
            Q(last_name__icontains=search_value)
        )\
        .order_by('-id')
    paginator = Paginator(contact, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "title": "Contatos",
        "search_value": search_value
    }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)

    context = {
        "contact": single_contact,
        "title": f"{single_contact.first_name} {single_contact.last_name}",
    }
    return render(request, 'contact/contact.html', context)


def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})
