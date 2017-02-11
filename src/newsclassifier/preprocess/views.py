from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .forms import *


class TokenizeView(SingleObjectMixin, ListView):

    template_name = 'preprocess/tokenize.html'
    form_class = TokenizeForm

    def get(self, request, *args, **kwargs):
        form_obj = self.form_class(request.GET or None)

        return render(request, self.template_name, {
            'form': form_obj,
        })
