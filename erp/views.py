from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from core.models import Funcionario, Produto
from erp.forms import InsereFuncionarioForm, InsereProdutoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------
class HomeView(TemplateView):
    template_name = "erp/index.html"

# PÁGINA PRINCIPAL FUNCIONÁRIOS
# ----------------------------------------------

class HomeFuncionarioView(TemplateView):
    template_name = "erp/funcionarios/index.html"

# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ListaFuncionariosView(ListView):
    template_name = "erp/funcionarios/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class CriaFuncionarioView(CreateView):
    template_name = "erp/funcionarios/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("erp:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class AtualizaFuncionarioView(UpdateView):
    template_name = "erp/funcionarios/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("erp:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------
class DeletaFuncionarioView(DeleteView):
    template_name = "erp/funcionarios/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("erp:lista_funcionarios")
    

# LISTAR PRODUTOS
# ---------------------------------------------- 
class ListaProdutosView(ListView):
    template_name = "erp/produtos/lista.html"
    model = Produto
    context_object_name = 'produtos'

# CRIAR PRODUTO
# ---------------------------------------------- 
class CriaProdutoView(CreateView):
    template_name = "erp/produtos/cria.html"
    model = Produto
    form_class = InsereProdutoForm
    success_url = reverse_lazy("erp:lista_produtos")

# ATUALIZA PRODUTO
# ---------------------------------------------- 
class AtualizaProdutoView(UpdateView):
    template_name = "erp/produtos/atualiza.html"
    model = Produto
    fields = '__all__'
    context_object_name = "produto"
    success_url = reverse_lazy("erp:lista_produtos")

# EXCLUI PRODUTO
# ---------------------------------------------- 
class DeletaProdutoView(DeleteView):
    template_name= "erp/produtos/exclui.html"
    model = Produto
    context_object_name = "produto"
    success_url = reverse_lazy("erp:lista_produtos")