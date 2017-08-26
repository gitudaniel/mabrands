# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from brands.models import Info

import requests



def ViewAll(request):
    data = requests.get('http://localhost:8000')

    representation = data.json()
    print representation

    context_dict = {'representation': representation}

    return render(request, 'brands_admin/all_data.html', context_dict)
