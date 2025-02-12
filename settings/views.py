from django.shortcuts import render

from django.views.generic.edit import FormView

# Create your views here.
class InvertView(formview):
    
    def form_valid(self, form):
        invert = 
        response = super().form_valid(form)
        response.set_cookie( 'invert',invert )
        return response
