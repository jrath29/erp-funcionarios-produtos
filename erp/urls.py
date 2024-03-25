from django.urls import path
from erp import views

app_name = 'erp'

urlpatterns = [
#FUNCIONÁRIOS
    # GET /
    path('', views.HomeView.as_view(), name="index"),

    # POST /funcionarios/cadastrar
    path('funcionarios/cadastrar', views.CriaFuncionarioView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios
    path('funcionarios/lista', views.ListaFuncionariosView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionarios/{pk}
    path('funcionarios/<pk>', views.AtualizaFuncionarioView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionarios/excluir/<pk>', views.DeletaFuncionarioView.as_view(), name="deleta_funcionario"),

#PRODUTOS
   
    #POST /produtos/cadastrar
    path('produtos/cadastrar', views.CriaProdutoView.as_view(), name="cadastra_produto"),

    #GET /produtos
    path('produtos/lista', views.ListaProdutosView.as_view(), name="lista_produtos"),

    #GET/POST /produtos/<pk>
    path('produtos/<pk>', views.AtualizaProdutoView.as_view(), name="atualiza_produto"),

    #GET/POST /produtos/excluir
    path('produtos/excluir/<pk>', views.DeletaProdutoView.as_view(), name="deleta_produto")

]
