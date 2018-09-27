import MySQLdb, cliente
#Conectando ao banco de dados
db = MySQLdb.connect(user="root", passwd="123456", db="treinaweb_clientes", host="localhost", autocommit=True)

#Criando cursor
cursor = db.cursor()


def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())

def inserir_cliente(cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) values(%s, %s)", (cliente.nome, cliente.idade))

def editar_cliente(id, cliente):
    cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE id=%(id)s",
                   ({'nome':cliente.nome, 'idade':cliente.idade, 'id':id}))

def remover_cliente(id):
    cursor.execute("DELETE FROM cliente WHERE id=%s", (id,))

cliente = cliente.Cliente("Amelia", 71)

listar_clientes()
inserir_cliente(cliente)
editar_cliente(2, cliente)
remover_cliente(2)

db.close()

