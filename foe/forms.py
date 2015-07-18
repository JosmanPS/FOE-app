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
        exclude = ['usuario', 'fiscalizador']



class MiembroForm(ModelForm):

    class Meta:
        model = Miembro
        exclude = ['organizacion_estudiantil']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit(
            'guardar',
            'Guardar',
            css_class='btn-primary'))
        super(MiembroForm, self).__init__(*args, **kwargs)


class BancarioForm(ModelForm):

    class Meta:
        model = DatosBancarios
        exclude = ['organizacion_estudiantil']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit(
            'guardar',
            'Guardar',
            css_class='btn-primary'))
        super(BancarioForm, self).__init__(*args, **kwargs)


class ComiteForm(ModelForm):

    class Meta:
        model = Comite
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit(
            'guardar',
            'Guardar',
            css_class='btn-primary'))
        super(ComiteForm, self).__init__(*args, **kwargs)
