import pytest
from pytest import mark
from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 22
        funcionario_teste = Funcionario('teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When- ação
        assert resultado == esperado  # Then - desfecho

    def test_quando_sobrenone_recebe_Maria_Sanchez_deve_retornar_Sanchez(self):
        entrada = ' Maria Sanchez ' # Given
        esperado = 'Sanchez'
        maria = Funcionario(entrada, '11/11/2000', 1111)
        reultado = maria.sobrenome() #when

        assert reultado == esperado  # Then

    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retorna_9000(self):
        entrada_salario = 100_000
        entrada_nome = 'Paulo Bragança'
        esperado = 90_000

        funcionario_teste = Funcionario(entrada_nome, '23/09/1998', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):

        entrada = 1_000
        esperado = 100

        funcionario_teste = Funcionario("Teste", '23/09/1998', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exeception(self):

        with pytest.raises(Exception):
            entrada = 1_000_000

            funcionario_teste = Funcionario("Teste", '23/09/1998', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

