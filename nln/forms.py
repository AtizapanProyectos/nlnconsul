from django import forms

from .models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["nombre", "empresa", "rating", "opinion"]

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        return nombre

    def clean_opinion(self):
        opinion = self.cleaned_data["opinion"].strip()
        if not opinion:
            raise forms.ValidationError("Escribe tu opinión antes de enviarla.")
        return opinion