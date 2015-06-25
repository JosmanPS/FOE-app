# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response

#
# FOE, main site
#


def index(request):
    args = {}
    return render_to_response('foe/main/index.html', args)
