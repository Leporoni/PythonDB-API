import MySQLdb

class ClienteRepository():

    @staticmethod
    def listar_clientes():
        db = MySQLdb.connect(user="root", passwd="123456", db="treinaweb_clientes", host="localhost", autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cliente")
        print(cursor.fetchall())
        db.close()

    @staticmethod
    def inserir_cliente(cliente):
        db = MySQLdb.connect(user="root", passwd="123456", db="treinaweb_clientes", host="localhost", autocommit=True)
        cursor = db.cursor()
        cursor.execute("INSERT INTO cliente (nome, idade) values(%s, %s)", (cliente.nome, cliente.idade))
        db.close()

    @staticmethod
    def editar_cliente(id, cliente):
        db = MySQLdb.connect(user="root", passwd="123456", db="treinaweb_clientes", host="localhost", autocommit=True)
        cursor = db.cursor()
        cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE id=%(id)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id': id}))
        db.close()

    @staticmethod
    def remover_cliente(id):
        db = MySQLdb.connect(user="root", passwd="123456", db="treinaweb_clientes", host="localhost", autocommit=True)
        cursor = db.cursor()
        cursor.execute("DELETE FROM cliente WHERE id=%s", (id,))
        db.close()
