# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UpdateDetailsView(generic.UpdateView):
    model = User
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
