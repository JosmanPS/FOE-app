# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render, render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import *
from .models import *
from django.utils.text import slugify

#
# FOE, main site
#


def index(request):
    args = dict()
    return render_to_response('foe/main/index.html', args)


@login_required
def registro_oe(request):
    args = dict()
    usuario = request.user
    oe_usuario = OrganizacionEstudiantil(usuario=usuario)
    oe = OrganizacionEstudiantil.objects.filter(usuario=usuario)
    args['completo'] = False

    if request.method == 'POST':
        print(usuario)
        if oe:
            form = OEForm(request.POST, request.FILES, instance=oe[0])
        else:
            form = OEForm(request.POST, request.FILES, instance=oe_usuario)
        if form.is_valid():
            f = form.save()
            f.slug = slugify(f.nombre)
            f.save()
            return redirect(reverse('registro_oe'))

    else:
        if oe:
            form = OEForm(instance=oe[0])
        else:
            form = OEForm(instance=oe_usuario)
    args['form'] = form
    return render(request, "foe/forms/registroOE.html", args)


@login_required
def registro_comite(request):
    args = dict()
    usuario = request.user
    cm_usuario = Comite(usuario=usuario)
    cm = Comite.objects.filter(usuario=usuario)

    if request.method == 'POST':
        print(usuario)
        if cm:
            form = ComiteForm(request.POST, request.FILES, instance=cm[0])
        else:
            form = ComiteForm(request.POST, request.FILES, instance=cm_usuario)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        if cm:
            form = ComiteForm(instance=cm[0])
        else:
            form = ComiteForm(instance=cm_usuario)
    args['form'] = form
    return render(request, "foe/forms/comite.html", args)


@login_required
def miembros_oe(request):
    args = dict()
    usuario = request.user
    oe = get_object_or_404(OrganizacionEstudiantil, usuario=usuario)
    m_oe = Miembro(organizacion_estudiantil=oe)
    m = Miembro.objects.filter(organizacion_estudiantil=oe)

    if request.method == 'POST':
        print(usuario)
        if m:
            form = MiembroForm(request.POST, request.FILES, instance=m[0])
        else:
            form = MiembroForm(request.POST, request.FILES, instance=m_oe)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        if m:
            form = MiembroForm(instance=m[0])
        else:
            form = MiembroForm(instance=m_oe)
    args['form'] = form
    return render(request, "foe/forms/miembro.html", args)


@login_required
def datos_bancarios(request):
    args = dict()
    usuario = request.user
    oe = get_object_or_404(OrganizacionEstudiantil, usuario=usuario)
    m_oe = DatosBancarios(organizacion_estudiantil=oe)
    m = DatosBancarios.objects.filter(organizacion_estudiantil=oe)

    if request.method == 'POST':
        print(usuario)
        if m:
            form = BancarioForm(request.POST, request.FILES, instance=m[0])
        else:
            form = BancarioForm(request.POST, request.FILES, instance=m_oe)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        if m:
            form = BancarioForm(instance=m[0])
        else:
            form = BancarioForm(instance=m_oe)
    args['form'] = form
    return render(request, "foe/forms/datos-bancarios.html", args)


def directorio(request):
    args = dict()
    oes = OrganizacionEstudiantil.objects.all()
    oes.order_by('clasificacion', 'nombre')
    args['organizaciones'] = oes
    return render(request, "foe/main/directorio.html", args)


def perfil_oe(request, oe_slug):
    args = dict()
    oe = get_object_or_404(
        OrganizacionEstudiantil, slug=oe_slug)
    args['oe'] = oe
    args['logo_url'] = oe.logo._get_url()
    args['plan_trabajo_url'] = oe.plan_trabajo._get_url()
    args['presupuesto_url'] = oe.presupuesto._get_url()
    return render(request, "foe/main/perfil.html", args)
