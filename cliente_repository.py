import fabrica_conexao

class ClienteRepository():

    @staticmethod
    def listar_clientes():
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())
        finally:
            fabrica.close()

    @staticmethod
    def inserir_cliente(cliente):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("INSERT INTO cliente (nome, idade) values(%s, %s)", (cliente.nome, cliente.idade))
        finally:
            fabrica.close()

    @staticmethod
    def editar_cliente(id, cliente):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE id=%(id)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id': id}))
        finally:
            fabrica.close()

    @staticmethod
    def remover_cliente(id):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("DELETE FROM cliente WHERE id=%s", (id,))
        finally:
            fabrica.close()
