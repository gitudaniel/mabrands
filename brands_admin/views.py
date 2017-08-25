# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from brands.models import Info



def ViewAll(request):
    info = Info.objects.all()

    context_dict = { 'info': info }

    return render(request, 'brands_admin/all_data', context_dict)
