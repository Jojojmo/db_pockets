import sqlite3
import json

ufs_dict = [{'nome': 'Acre', 'UF': 'AC', 'capital': 'Rio Branco', 'area': 164122.2},
 {'nome': 'Alagoas', 'UF': 'AL', 'capital': 'Maceió', 'area': 27767.7},
 {'nome': 'Amapá', 'UF': 'AP', 'capital': 'Macapá', 'area': 142814.6},
 {'nome': 'Amazonas', 'UF': 'AM', 'capital': 'Manaus', 'area': 1570745.7},
 {'nome': 'Bahia', 'UF': 'BA', 'capital': 'Salvador', 'area': 564692.7},
 {'nome': 'Ceará', 'UF': 'CE', 'capital': 'Fortaleza', 'area': 148825.6},
 {'nome': 'Distrito Federal','UF': 'DF','capital': 'Brasília','area': 5822.1},
 {'nome': 'Espírito Santo','UF': 'ES','capital': 'Vitória','area': 46077.5},
 {'nome': 'Goiás', 'UF': 'GO', 'capital': 'Goiânia', 'area': 340086.7},
 {'nome': 'Maranhão', 'UF': 'MA', 'capital': 'São Luís', 'area': 331983.3},
 {'nome': 'Mato Grosso', 'UF': 'MT', 'capital': 'Cuiabá', 'area': 903357.9},
 {'nome': 'Mato Grosso do Sul','UF': 'MS','capital': 'Campo Grande','area': 357125.0},
 {'nome': 'Minas Gerais','UF': 'MG','capital': 'Belo Horizonte','area': 586528.3},
 {'nome': 'Pará', 'UF': 'PA', 'capital': 'Belém', 'area': 1247689.5},
 {'nome': 'Paraíba', 'UF': 'PB', 'capital': 'João Pessoa', 'area': 56439.8},
 {'nome': 'Paraná', 'UF': 'PR', 'capital': 'Curitiba', 'area': 199314.9},
 {'nome': 'Pernambuco', 'UF': 'PE', 'capital': 'Recife', 'area': 98311.6},
 {'nome': 'Piauí', 'UF': 'PI', 'capital': 'Teresina', 'area': 251529.2},
 {'nome': 'Rio de Janeiro','UF': 'RJ','capital': 'Rio de Janeiro','area': 43696.1},
 {'nome': 'Rio Grande do Norte','UF': 'RN','capital': 'Natal','area': 52796.8},
 {'nome': 'Rio Grande do Sul','UF': 'RS','capital': 'Porto Alegre','area': 281748.5},
 {'nome': 'Rondônia','UF': 'RO','capital': 'Porto Velho','area': 237576.2},
 {'nome': 'Roraima', 'UF': 'RR', 'capital': 'Boa Vista', 'area': 224299.0},
 {'nome': 'Santa Catarina','UF': 'SC','capital': 'Florianópolis','area': 95346.2},
 {'nome': 'São Paulo', 'UF': 'SP', 'capital': 'São Paulo', 'area': 248209.4},
 {'nome': 'Sergipe', 'UF': 'SE', 'capital': 'Aracaju', 'area': 21910.3},
 {'nome': 'Tocantins', 'UF': 'TO', 'capital': 'Palmas', 'area': 277620.9}]



bd_uf = sqlite3.connect("estados_brasil.db")
cursor = bd_uf.cursor()

def create_tables(name: str, command: str):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
    tab_existe = cursor.fetchone() is not None
    if tab_existe:
        print(f"Tabela {name} já existente")
    else:
        cursor.execute(command)
        print(f"Tabela {name} criada!")

command = """
CREATE TABLE Estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    UF TEXT,
    capital TEXT,
    area REAL
);"""

create_tables("Estados", command)

insert_items = False

if insert_items:
    for values in ufs_dict:
        cursor.execute("INSERT INTO Estados (nome, UF, capital, area) VALUES (?, ?, ?, ?)",
                    (values['nome'], values['UF'], values['capital'], float(values['area'])))
        bd_uf.commit()




dados_for_j = cursor.execute("SELECT * FROM Estados").fetchall()

cursor.execute("PRAGMA table_info(Estados)")

colunas = cursor.fetchall()


obj_j = list()
for dado in dados_for_j:
     add_obj = dict()
     for index, coluna in enumerate(colunas):
        add_obj[coluna[1]] = dado[index]
     obj_j.append(add_obj)

print(obj_j)