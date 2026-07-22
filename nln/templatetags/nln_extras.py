from django import template

register = template.Library()


@register.filter
def iniciales(nombre):
    """
    Convierte 'Roberto Medina' -> 'RM' para el circulito del avatar.
    Se usa en el template así: {{ o.nombre|iniciales }}
    """
    if not nombre:
        return ""
    partes = nombre.strip().split()
    letras = [p[0].upper() for p in partes[:2] if p]
    return "".join(letras)