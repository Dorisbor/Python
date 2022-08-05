import re

from validate_docbr import CPF
import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='dorisbor',
    database='andromeda',
)

cursor = conexao.cursor()

def create():
    cursor.execute(comando)
    conexao.commit()

def valida_nome(cliente_nome):
    cliente_nome.isalpha()
    if cliente_nome:
        return cliente_nome
    raise ValueError("Digite um nome:  ")

def valida_cpf(cliente_cpf):
    cliente_cpf = str(cliente_cpf)
    if len(cliente_cpf) == 11:
        validador = CPF()
        return validador.validate(cliente_cpf)
    raise ValueError("CPF Inválido: ")

def valida_sexo(cliente_sexo):
    if cliente_sexo == "Masculino":
        return cliente_sexo
    elif cliente_sexo == "Feminino":
        return cliente_sexo
    elif cliente_sexo == "Outro":
        return cliente_sexo
    raise ValueError("Selecione o sexo!")

def valida_telefone(cliente_telefone):
    cliente_telefone = str(cliente_telefone)
    if len(cliente_telefone) == 11:
        return cliente_telefone
    raise ValueError("Digite um telefone correto exemplo: xx xxxxx-xxxx")

def valida_cep(cliente_cep):
    cliente_cep = str(cliente_cep)
    if len(cliente_cep) == 8:
        return cliente_cep
    raise ValueError("Digite um CEP Válido!")

def valida_rua(cliente_rua):
    cliente_rua.isalpha()
    if cliente_rua:
        return cliente_rua
    raise ValueError("Digite o nome da rua!")

def valida_bairro(cliente_bairro):
    cliente_bairro.isalpha()
    if cliente_bairro:
        return cliente_bairro
    raise ValueError("Digite o nome do bairro!")

def valida_numero(cliente_num):
    cliente_num.isalpha()
    if cliente_num:
        return cliente_num
    raise ValueError("Digite o número da residência!")

def valida_uf(cliente_uf):
    cliente_uf.isalpha()
    if cliente_uf:
        return cliente_uf
    raise ValueError("Digite o nome do Estado!")

def valida_cidade(cliente_cidade):
    cliente_cidade.isalpha()
    if cliente_cidade:
        return cliente_cidade
    raise ValueError("Digite o nome da Cidade!")

def valida_email(cliente_email):
    validacao = re.compile("[a-z]{1,100}([0-9])?@[a-z]{0,100}([0-9]?).com(.br)?")
    search = validacao.search(cliente_email)
    if search:
        return cliente_email
    raise ValueError("Digite um email válido!")

cliente_email = "rrerwe1993a@ffa1.com"
valida_email(cliente_email)
print(cliente_email)

'''
cpf = (input("Digite o CPF: "))
nome = (input("Digite seu nome: "))
cpf = CadastroCliente(cpf)
nome = CadastroCliente(nome)
comando = f'INSERT INTO cliente (cliente_nome, cliente_cpf) VALUES ("{nome}","{cpf}")'
create()
'''

'''
#Create
comando = f'INSERT INTO cliente () VALUES ("{}","{}")' #primeira posicao nome das tabbelas separado por virgulo,
# segunda sao as variaveis e nao passa o ID
cursor.execute(comando)
conexao.commit() #sempre que editar/criar algo no banco

#Read
comando = 'select no bando'
cursor.execute(comando)
resultado = cursor.fetchall() # Usado somente para leitura no banco
print(resultado)

#Update
comando = f'UPDATE cliente SET coluna= "{}" WHERE nomedacoluna= "{}"'
cursor.execute(comando)
conexao.commit()

#Delete
comando = f'DELETE FROM cliente WHERE coluna = "{}"'
cursor.execute(comando)
conexao.commit()

'''

cursor.close()
conexao.close()