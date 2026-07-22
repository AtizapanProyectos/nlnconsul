# Esto va en el urls.py de tu app 'nln' (o de tu proyecto, donde ya
# tengas la ruta del index). Solo agrega/ajusta estas líneas:

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # tu inicio.html, ajusta si ya tenías otro name
    path("opiniones/nueva/", views.crear_opinion, name="crear_opinion"),
    path("testimonios/", views.testimonios, name="testimonios"),
]