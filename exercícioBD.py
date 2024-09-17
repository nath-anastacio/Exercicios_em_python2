import sqlite3
 
# Conectar ao banco de dados (ou criar se não existir)
# Isso cria um arquivo chamado 'meu_banco.db' na pasta onde o script está sendo executado
conn = sqlite3.connect('meu_banco.db')
 
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()
 
# Criar uma tabela (se ela não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
''')
 
# Inserir dados na tabela
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES ('João', 30)")
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES ('Maria', 25)")
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES ('Carlos', 40)")
 
# Confirmar as mudanças
conn.commit()
 
# Consultar os dados para verificar se foram inseridos corretamente
cursor.execute("SELECT * FROM pessoas")
 
# Fetch all rows from the query
rows = cursor.fetchall()
 
# Exibir os resultados
for row in rows:
    print(row)
 
# Fechar a conexão
conn.close()