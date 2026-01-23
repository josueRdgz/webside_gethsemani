from django.shortcuts import render
from reflections.models import Reflection


def inicio(request):
    reflection = (
        Reflection.objects
        .filter(is_published=True)
        .first()
    )
    return render(request, 'core/inicio.html', {
        'reflection': reflection
    })


def nosotros(request):
    return render(request, "core/nosotros.html")


def contact(request):
    return render(request, 'core/contact.html')
