from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import OpinionForm
from .models import Opinion


def index(request):
    """
    Vista principal (tu inicio.html). Arma todo lo que la sección de
    opiniones necesita: las tarjetas, el promedio y las barras de %.
    """
    opiniones_qs = Opinion.objects.filter(aprobado=True)
    total_opiniones = opiniones_qs.count()

    promedio = opiniones_qs.aggregate(avg=Avg("rating"))["avg"] or 0
    promedio = round(promedio, 1)

    distribucion = []
    for n in [5, 4, 3, 2, 1]:
        cuenta = opiniones_qs.filter(rating=n).count()
        pct = round((cuenta / total_opiniones) * 100) if total_opiniones else 0
        distribucion.append({"estrellas": n, "pct": pct})

    context = {
        # Solo mostramos hasta 6 en el index, igual que antes
        "opiniones": opiniones_qs[:6],
        "total_opiniones": total_opiniones,
        "promedio": promedio,
        "promedio_redondeado": round(promedio),
        "distribucion": distribucion,
        "form_opinion": OpinionForm(),
    }
    return render(request, "nln/inicio.html", context)


def crear_opinion(request):
    """
    Recibe el POST del formulario 'Dejar mi opinión' y la guarda en sqlite.
    Luego regresa al index (a la sección #opiniones) para que se vea de una vez.
    """
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Gracias por tu opinión! Ya se publicó. 💜")
        else:
            messages.error(
                request,
                "No se pudo guardar tu opinión, revisa que llenaste nombre y comentario.",
            )

    # OJO: 'index' debe ser el name= que le pusiste a tu url del inicio.
    # Si tu inicio.html tiene otro name en urls.py, cámbialo aquí.
    return redirect(reverse("index") + "#opiniones")


def testimonios(request):
    """
    Vista para tu página aparte de 'Ver todas las opiniones' (testimonios.html).
    Aquí sí mostramos TODAS, no solo 6.
    """
    opiniones_qs = Opinion.objects.filter(aprobado=True)
    context = {
        "opiniones": opiniones_qs,
        "total_opiniones": opiniones_qs.count(),
    }
    return render(request, "nln/testimonios.html", context)