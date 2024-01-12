from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact



def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            "form": form,
            "form_action": form_action,
            "title": "Novo Contato",
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(request, 'contact/create.html', context)
    
    form = ContactForm()

    context = {
            "form": form,
            "title": "Novo Contato",
        }
    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "form": form,
            "form_action": form_action,
            "title": "Editar Contato",
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(request, 'contact/create.html', context)
    
    context = {
            "form": ContactForm(instance=contact),
            "title": "Editar Contato",
        }
    return render(request, 'contact/create.html', context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    context = {
        "contact":contact,
        "confirmation":confirmation
    }

    return render(request, 'contact/contact.html', context)