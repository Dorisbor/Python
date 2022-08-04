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

def retorna_sexo():
    pass

def valida_telefone(cliente_telefone):
    pass

def valida_cep(cliente_cep):
    pass

def valida_rua(cliente_rua):
    pass

def valida_bairro(cliente_bairro):
    pass

def valida_numero(cliente_num):
    pass

def valida_uf(cliente_uf):
    pass

def valida_cidade(cliente_cidade):
    pass

def valida_email(cliente_email):
    pass

cpf = "03546800133"
valida_cpf(cpf)
print(cpf)

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