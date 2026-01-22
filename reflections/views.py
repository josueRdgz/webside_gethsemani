from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Reflection


def reflection_list(request):
    reflections = Reflection.objects.filter(is_published=True)
    return render(request, 'reflections/reflection_list.html', {
        'reflections': reflections
    })


def reflection_detail(request, slug):
    reflection = get_object_or_404(
        Reflection,
        slug=slug,
        is_published=True
    )
    return render(request, 'reflections/reflection_detail.html', {
        'reflection': reflection
    })
