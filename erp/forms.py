from core.models import Funcionario, Produto
from django import forms

# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao',
        ]

# FORMULÁRIO DE INCLUSÃO DE PRODUTOS
# -------------------------------------------
class InsereProdutoForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Produto

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'preco'
        ]
