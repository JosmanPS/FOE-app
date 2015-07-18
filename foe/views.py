# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render, render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import *
from .models import *
#
# FOE, main site
#


def index(request):
    args = {}
    return render_to_response('foe/main/index.html', args)


@login_required
def registro_oe(request):
    args = dict()
    usuario = request.user
    oe_usuario = OrganizacionEstudiantil(usuario=usuario)
    oe = OrganizacionEstudiantil.objects.filter(usuario=usuario)
    args['completo'] = False

    if request.method == 'POST':
        if oe:
            form = OEForm(request.POST, request.FILES, instance=oe[0])
        else:
            form = OEForm(request.POST, request.FILES, instance=oe_usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse('registro_oe'))

    else:
        if oe:
            form = OEForm(instance=oe[0])
        else:
            form = OEForm(instance=oe_usuario)
    args['form'] = form
    return render(request, "foe/forms/registroOE.html", args)

