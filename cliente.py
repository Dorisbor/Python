import numbers
import requests
import re
from validate_docbr import CPF


class BuscaEndereco:

    def __init__(self, cep):
         cep = str(cep)
         if self.cep_e_valido(cep):
             self.cep = cep
         else:
             raise ValueError("CEP Inválido")

    def __str__(self):
       return self.format_cep()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
             return True
        else:
             return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acesso_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.jason()
        return (
            dados['bairro'],
            dados['localidade'],
             dados['uf']
        )

class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()

class ValidaNome:

    def __init__(self, nome):
        if nome != "" and not numbers:
            return nome.title()
        else:
            print("Digite um nome: ")


class CadastroCliente:

    def __init__(self, Cpf, ValidaNome):
        self.cpf = Cpf
        self.nome = ValidaNome