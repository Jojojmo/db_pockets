import sqlite3
import json

ufs_dict = [{'nome': 'Alabama', 'UF': 'AL', 'capital': 'Montgomery', 'area': '135765'},
{'nome': 'Alasca(Alaska)', 'UF': 'AK', 'capital': 'Juneau', 'area': '1717854'},
{'nome': 'Arcansas(Arkansas)', 'UF': 'AR', 'capital': 'Little Rock', 'area': '2937979'},
{'nome': 'Arizona', 'UF': 'AZ', 'capital': 'Phoenix', 'area': '6482505'},
{'nome': 'Califórnia(California)', 'UF': 'CA', 'capital': 'Sacramento', 'area': '423970'},
{'nome': 'Cansas(Kansas)', 'UF': 'KS', 'capital': 'Topeka', 'area': '213096'},
{'nome': 'Carolina do Norte(North Carolina)', 'UF': 'NC', 'capital': 'Raleigh', 'area': '139509'},
{'nome': 'Carolina do Sul(South Carolina)', 'UF': 'SC', 'capital': 'Columbia', 'area': '4679230'},
{'nome': 'Colorado', 'UF': 'CO', 'capital': 'Denver', 'area': '5116796'},
{'nome': 'Conecticute/Coneticute(Connecticut)', 'UF': 'CT', 'capital': 'Hartford', 'area': '14356'},
{'nome': 'Dakota do Norte(North Dakota)', 'UF': 'ND', 'capital': 'Bismarck', 'area': '183272'},
{'nome': 'Dakota do Sul(South Dakota)', 'UF': 'SD', 'capital': 'Pierre', 'area': '199905'},
{'nome': 'Delaware', 'UF': 'DE', 'capital': 'Dover', 'area': '6452'},
{'nome': 'Flórida(Florida)', 'UF': 'FL', 'capital': 'Tallahassee', 'area': '170304'},
{'nome': 'Geórgia/Jórgia(Georgia)', 'UF': 'GA', 'capital': 'Atlanta', 'area': '9815210'},
{'nome': 'Havaí/Havai(Hawaii)', 'UF': 'HI', 'capital': 'Honolulu', 'area': '1374810'},
{'nome': 'Idaho', 'UF': 'ID', 'capital': 'Boise', 'area': '1584985'},
{'nome': 'Ilha de Rodes[nota 1](Rhode Island)', 'UF': 'RI', 'capital': 'Providence', 'area': '1051302'},
{'nome': 'Ilinóis(Illinois)', 'UF': 'IL', 'capital': 'Springfield', 'area': '141998'},
{'nome': 'Indiana', 'UF': 'IN', 'capital': 'Indianápolis', 'area': '3062309'},
{'nome': 'Iowa', 'UF': 'IA', 'capital': 'Des Moines', 'area': '6516922'},
{'nome': 'Kentucky[nota 2]', 'UF': 'KY', 'capital': 'Frankfort', 'area': '104659'},
{'nome': 'Luisiana(Louisiania)', 'UF': 'LA', 'capital': 'Baton Rouge', 'area': '135382'},
{'nome': 'Maine', 'UF': 'ME', 'capital': 'Augusta', 'area': '91646'},
{'nome': 'Marilândia(Maryland)', 'UF': 'MD', 'capital': 'Annapolis', 'area': '32133'},
{'nome': 'Massachusetts[nota 2]', 'UF': 'MA', 'capital': 'Boston', 'area': '5828289'},
{'nome': 'Míchigan/Michigão(Michigan)', 'UF': 'MI', 'capital': 'Lansing', 'area': '253973'},
{'nome': 'Minesota(Minnesota)', 'UF': 'MN', 'capital': 'Saint Paul', 'area': '225181'},
{'nome': 'Mississípi(Mississippi)', 'UF': 'MS', 'capital': 'Jackson', 'area': '2978512'},
{'nome': 'Missúri(Missouri)', 'UF': 'MO', 'capital': 'Jefferson City', 'area': '180533'},
{'nome': 'Montana', 'UF': 'MT', 'capital': 'Helena', 'area': '381156'},
{'nome': 'Nebrasca(Nebraska)', 'UF': 'NE', 'capital': 'Lincoln', 'area': '200520'},
{'nome': 'Nevada', 'UF': 'NV', 'capital': 'Carson City', 'area': '286367'},
{'nome': 'Nova Hampshire(New Hampshire)', 'UF': 'NH', 'capital': 'Concord', 'area': '24217'},
{'nome': 'Nova Jérsei/Nova Jérsia(New Jersey)', 'UF': 'NJ', 'capital': 'Trenton', 'area': '22608'},
{'nome': 'Nova Iorque(New York)', 'UF': 'NY', 'capital': 'Albany', 'area': '141299'},
{'nome': 'Novo México(New México)', 'UF': 'NM', 'capital': 'Santa Fe', 'area': '315194'},
{'nome': 'Oclaoma(Oklahoma)', 'UF': 'OK', 'capital': 'Oklahoma City', 'area': '3751351'},
{'nome': 'Ohio', 'UF': 'OH', 'capital': 'Columbus', 'area': '11544951'},
{'nome': 'Óregon/Oregão(Oregon)', 'UF': 'OR', 'capital': 'Salem', 'area': '255026'},
{'nome': 'Pensilvânia[nota 2](Pennsylvania)', 'UF': 'PA', 'capital': 'Harrisburg', 'area': '119283'},
{'nome': 'Tenessi(Tennessee)', 'UF': 'TN', 'capital': 'Nashville', 'area': '6403353'},
{'nome': 'Texas', 'UF': 'TX', 'capital': 'Austin', 'area': '696241'},
{'nome': 'Utá(Utah)', 'UF': 'UT', 'capital': 'Salt Lake City', 'area': '2817222'},
{'nome': 'Vermonte(Vermont)', 'UF': 'VT', 'capital': 'Montpelier', 'area': '24293'},
{'nome': 'Virgínia[nota 2](Virginia)', 'UF': 'VA', 'capital': 'Richmond', 'area': '110785'},
{'nome': 'Virgínia Ocidental(West Virginia)', 'UF': 'WV', 'capital': 'Charleston', 'area': '1855364'},
{'nome': 'Washington', 'UF': 'WA', 'capital': 'Olympia', 'area': '184827'},
{'nome': 'Wisconsin', 'UF': 'WI', 'capital': 'Madison', 'area': '169639'},
{'nome': 'Wyoming', 'UF': 'WY', 'capital': 'Cheyenne', 'area': '568158'},]



bd_uf = sqlite3.connect("estados_eua.db")
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




# dados_for_j = cursor.execute("SELECT * FROM Estados").fetchall()

# cursor.execute("PRAGMA table_info(Estados)")

# colunas = cursor.fetchall()


# obj_j = list()
# for dado in dados_for_j:
#      add_obj = dict()
#      for index, coluna in enumerate(colunas):
#         add_obj[coluna[1]] = dado[index]
#      obj_j.append(add_obj)

# print(obj_j)