from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from core.forms import CadUsuarioForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = "blog/index.html"


class CadUsuarioView(CreateView):
    template_name = 'blog/usuarios/cadusuario.html'
    form_class = CadUsuarioForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        form.save()
        messages.success(self.request, 'Usuario Cadastrado!!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário não cadastrado!!!')
        return super().form_invalid(form)