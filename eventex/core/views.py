from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from eventex.core.models import Speaker, Talk
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    model = Speaker    

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)