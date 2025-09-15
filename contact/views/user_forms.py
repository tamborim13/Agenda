from django.shortcuts import render
from contact.forms import registerForm


def register(request):
    form = registerForm()

    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )