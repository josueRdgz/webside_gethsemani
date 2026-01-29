from django.shortcuts import render
from reflections.models import Reflection
from .models import Elder


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
    elders = Elder.objects.all()
    return render(request, "core/nosotros.html", {
        "elders": elders
    })


def contact(request):
    return render(request, 'core/contact.html')
