import os
import sqlite3
import json
from flask import Flask, jsonify, request, make_response


### Criação do banco de dados

class Banco_de_dados():
    def __init__(self, NAME_DB):
        self.__NAME_DB = NAME_DB
        self.conn = sqlite3.connect(f"{self.__NAME_DB}.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.tables = list()
    
    def create_table(self,name_table,rows):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
            {rows}
        )
        ''')
        if name_table not in self.tables:
            self.tables.append(name_table)
            return f'Tabela {name_table} criada!'
        
    def close(self):
        self.conn.close()
        

def bd_for_json(DB,TABLE_NAME):
    dados_for_j = DB.cursor.execute(f"SELECT * FROM {TABLE_NAME}").fetchall()
    colunas = DB.cursor.execute(f"PRAGMA table_info({TABLE_NAME})").fetchall()
    DB.close()
    obj_j = list()

    for dado in dados_for_j:
        add_obj = dict()
        for index, coluna in enumerate(colunas):
            add_obj[coluna[1]] = dado[index]
        obj_j.append(add_obj)    
    return obj_j


def read_db(DB, ID,TABLE):
    DB.cursor.execute('SELECT nome, arquivo FROM Registros WHERE id = ?', (ID,))
    row = DB.cursor.fetchone()
    if row:
        nome_do_banco, banco_de_dados_binario = row
        path = f"read\\{nome_do_banco}"
        with open(path + ".db", 'wb') as file:
            file.write(banco_de_dados_binario)
        db_copy = Banco_de_dados(path)
        result = bd_for_json(db_copy, TABLE)
        db_copy.close()
        os.remove(path + ".db")
        return result
    return 'ID não localizado!'

def insert_into(nome,categoria,tabela,data,path):
    with open(path, 'rb') as file:
        insert_binario = file.read()
    try:
        db.cursor.execute("INSERT INTO Registros (nome,  categoria, tabelas, data_criacao, arquivo) VALUES (?, ?, ?, ?, ?)",
                        (nome,categoria,tabela,data,insert_binario))
        db.conn.commit()
        id_registrado = db.cursor.lastrowid
        return f'O ID: {id_registrado} foi registrado com sucesso!'
    except sqlite3.IntegrityError as e:
        return f'Erro: {e}. Você não pode inserir o mesmo nome de banco de dados duas vezes!'





db = Banco_de_dados("registros")

db.create_table('Registros',"""
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    data_criacao DATE,
    categoria TEXT,
    tabelas JSON,
    arquivo BLOB
""")

def insert_mensage(insert_items,nome,categoria,tabela,data,path):
    if insert_items:
        try:
            result = insert_into(nome,categoria,tabela,data,path)
            print(result)
        except Exception as e:
            print(f'Erro inesperado: {e}')
    pass

insert_items = False
insert_mensage(insert_items,'iris','Data Science',json.dumps(['iris']),'2023-10-29','outros_bancos\iris.db')
insert_mensage(insert_items,"estados_brasil","Demografia",json.dumps(['Estados']),"2023-10-30","outros_bancos\estados_brasil.db")
insert_mensage(insert_items,"estados_americanos","Demografia",json.dumps(['Estados']),"2023-10-31","outros_bancos\estados_eua.db")


##### APP FLASK E ENDPOINTS

app = Flask(__name__)

@app.route('/list_sheet',methods=['GET'])
def list_sheet():
    db.cursor.execute("""
        SELECT json_object('id', id, 
                    'content', json_object('nome', nome, 
                                            'data_criacao', data_criacao,
                                            'categoria', categoria, 
                                            'tabelas', tabelas)) 
        FROM Registros
        """)
    json_data = db.cursor.fetchall()
    

    response_dic = {"list":[]}
    for row in json_data:
        raw_j = json.loads(row[0])
        response_dic["list"].append(raw_j)

    return jsonify(response_dic)


@app.route('/category/<string:categoria>', methods=['GET'])
def category(categoria):
    db.cursor.execute("""
        SELECT json_object('id', id, 
                    'content', json_object('nome', nome, 
                                            'data_criacao', data_criacao,
                                            'categoria', categoria, 
                                            'tabelas', tabelas)) 
        FROM Registros
        WHERE categoria = ?;
        """, (categoria,))
    json_data = db.cursor.fetchall()

    response_dic = {"list": []}
    for row in json_data:
        raw_j = json.loads(row[0])
        response_dic["list"].append(raw_j)

    return jsonify(response_dic)



# http://localhost:5000/sheet/1?TABLE=iris
# http://localhost:5000/sheet/{ID}
# http://localhost:5000/sheet/{ID}?TABLE={TABLE}
@app.route('/sheet/<int:ID>', methods=['GET'])
def sheet_id(ID):
    TABLE = request.args.get('TABLE', default=None) 
    db.cursor.execute("SELECT * FROM Registros WHERE id = ?", (ID,))
    result = db.cursor.fetchone()
    if TABLE and result:
        return jsonify(read_db(db, ID,TABLE)[:])
    if result:
        return jsonify(read_db(db, ID,json.loads(result[4])[0])[:])
    else:
        return jsonify({"message": "ID não localizado!"}), 404


@app.route('/sheet/<int:ID>', methods=['PUT'])
def sheet_update(ID):
    db.cursor.execute("SELECT * FROM Registros WHERE id = ?", (ID,))
    existing_record = db.cursor.fetchone()
    if existing_record is None:
        db.conn.close()
        return jsonify({"error": "Registro não encontrado"}), 404

    sql = "UPDATE Registros SET "
    for column, value in request.args.items():
        sql += f"{column} = '{value}', "

    sql = sql.rstrip(', ')
    sql += f" WHERE id = {ID}"
    
    try:
        db.cursor.execute(sql)
        db.conn.commit()
        return jsonify({"message": "Registro atualizado com sucesso"}), 200
    except Exception as e:
        # Capturando a exceção e retornando uma mensagem de erro com a exceção ocorrida.
        return jsonify({"error": f"Erro ao atualizar o registro: {str(e)}"}), 500


@app.route('/sheet/<int:ID>', methods=['DELETE'])
def del_index(ID):
    try:
        db.cursor.execute("DELETE FROM Registros WHERE ID = ?;", (ID,))
        db.conn.commit()
        return jsonify({"message": f"Registro com ID {ID} excluído com sucesso."}), 200
    
    except Exception as e:
        return jsonify({"error": f"Erro ao excluir o registro: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)










