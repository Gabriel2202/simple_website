from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import receive
# Create your views here.

class homeIndex(CreateView):
    model = receive
    fields = ("thefile",)
    template_name = "receive_form.html"
    context_object_name = "ok"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.thefile = self.request.POST.get("thefile")
        messages.success(self.request, "the file is saved successfully")
        return super().form_valid(form)

    
