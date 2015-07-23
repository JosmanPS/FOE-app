# -*- coding: utf-8 -*-
from .models import *
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, MultiWidgetField, Div
from crispy_forms.bootstrap import TabHolder, Tab, Field, Alert, AppendedText
from crispy_forms.bootstrap import StrictButton, FieldWithButtons


class OEForm(ModelForm):

    class Meta:
        model = OrganizacionEstudiantil
        exclude = ['usuario', 'fiscalizador', 'slug']


class MiembroForm(ModelForm):

    class Meta:
        model = Miembro
        exclude = ['organizacion_estudiantil']


class BancarioForm(ModelForm):

    class Meta:
        model = DatosBancarios
        exclude = ['organizacion_estudiantil']


class ComiteForm(ModelForm):

    class Meta:
        model = Comite
        exclude = ['usuario']
