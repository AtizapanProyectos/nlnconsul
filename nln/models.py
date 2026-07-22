from django.db import models


class Opinion(models.Model):
    """
    Una opinión/reseña dejada por un cliente en el index.
    Se guarda en tu base sqlite3 (la de Django por default).
    """

    nombre = models.CharField(max_length=150)
    empresa = models.CharField(
        "Empresa / Puesto", max_length=150, blank=True
    )  # opcional, como en tu form
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} estrella{'s' if i != 1 else ''}") for i in range(1, 6)],
        default=5,
    )
    opinion = models.TextField("Opinión")
    fecha = models.DateTimeField(auto_now_add=True)

    # Por si algún día quieres moderar antes de publicar (opcional).
    # Si no la quieres usar, déjala en True siempre y ya.
    aprobado = models.BooleanField(default=True)

    class Meta:
        ordering = ["-fecha"]  # las más nuevas primero
        verbose_name = "Opinión"
        verbose_name_plural = "Opiniones"

    def __str__(self):
        return f"{self.nombre} ({self.rating}★)"