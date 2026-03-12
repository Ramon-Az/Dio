# cSpell:ignore pymongo dotenv testedb
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Conectar ao MongoDB
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)

# Acessar banco de dados
db = client['testedb']

"""Inserir documento, um registro de teste para verificar a inserção inicial
documento = {"nome": "Teste", "valor": 123}
resultado = collection.insert_one(documento)
print(f"Documento inserido com ID: {resultado.inserted_id}")"""

# Primeira inserção de acordo com a aula
collection_destinos = db['destinos']
collection_reservas = db['reservas']
collection_usuarios = db['usuarios']

# 1:
documento_reservas = {
    "nome": "Pamela", 
    "email": "pamela.apolinario@yahoo.com",
    "idade": 30,
    "data_nascimento": "1990-05-10"
    }

# 2: 
documento_usuarios = [{
    "nome": "pedro",
    "idade": 28,
    "cidade": "Belo Horizonte",
    "estado": "MG",
    "endereco": {
        "rua": "Rua A",
        "numero": "123",
        "cidade": "Belo Horizonte",
        "estado": "MG"
    }
},
    {
    "nome": "Maria Silva",
    "idade":  23,
    "cidade": "São Paulo",
    "estado": "SP",
    "endereco": {
        "rua": "Av. B",
        "numero": "456",
        "cidade": "São Paulo",
        "estado": "SP"
    }
},
    {
    "nome": "Carlos Souza",
    "idade":  35,
    "cidade": "Rio de Janeiro",
    "estado": "RJ",
    "endereco": {
        "rua": "Rua C",
        "numero": "789",
        "cidade": "Rio de Janeiro",
        "estado": "RJ"
    }
}
]

# 3:
documento_destinos = {
    "destino": "Paris",
    "data_ida": "2023-07-15",
    "data_volta": "2023-07-22",
    "preco": 2500.00,
    "vagas": 2,
    "usuario_id": "12345"
}

"""outro modo de insert para multiplos valores:
resultado = collection.insert_many([documento1, documento2, ...])"""

# resultado_reservas = collection_reservas.insert_one(documento_reservas)
# resultado_usuarios = collection_usuarios.insert_many(documento_usuarios)
# resultado_destinos = collection_destinos.insert_one(documento_destinos)

# print(f"Documentos inseridos com ID: {resultado_reservas.inserted_id}")
# print(f"Documentos inseridos com IDs: {resultado_usuarios.inserted_ids}")
# print(f"Documento inserido com ID: {resultado_destinos.inserted_id}")

# Update Operadores
# Usando o operador $set para definir o valor de um campo específico
resultado_usuarios = collection_usuarios.update_one({ "nome": "pedro" }, { "$set": { "idade": 26 } })

# Usando o operador $inc para incrementar o valor de um campo numérico
# resultado_usuarios = collection_usuarios.update_one({ "nome": "João" }, { "$inc": { "idade": 1 } })

# Usando o operador $rename para renomear um campo existente
# resultado_usuarios = collection_usuarios.update_one({ "nome": "João" }, { "$rename": { "endereco.rua": "endereco.nomeRua" } })

# Usando o operador $unset para remover um campo específico de um documento
# resultado_usuarios = collection_usuarios.update_one({ "nome": "João" }, { "$unset": { "endereco" : "" } })

#  Delete
# Usando o método delete_one() para excluir o primeiro documento que corresponde ao filtro especificado
resultado_usuarios_delete_one = collection_usuarios.delete_one({ "nome": "pedro" })

# Usando o método delete_many() para excluir todos os documentos que correspondem ao filtro especificado
# resultado_usuarios_delete_many = collection_usuarios.delete_many({"cidade": "São Paulo" })

# Operadores Lógicos
resultado_usuarios_op_logicos = collection_usuarios.find({"$and": [{ "idade": { "$gte": 18 } }, { "cidade": "São Paulo" }]})

# resultado_usuarios_op_logicos = collection_usuarios.find({"$or": [{ "idade": { "$lt": 18 } }, { "cidade": "Rio de Janeiro" }]})

# resultado_usuarios_op_logicos = collection_usuarios.find({ "idade": { "$not": { "$eq": 25 } } })

# Operadores de Comparação
# $eq - operador igual
resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$eq": 25 } })

# # $ne - operador diferente
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$ne": 30 } })

# # $gt - operador maior que
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$gt": 30 } })
 
# # $gte - operador maior ou igual que
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$gte": 30 } })

# # $lt - operador menor que
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$lt": 30 } })

# # $lte - operador menor ou igual que
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "idade": { "$lte": 30 } })

# # $in - operador dentro de um array
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "cidade": { "$in": ["São Paulo", "Rio de Janeiro"] } })

# # $nin - operador não dentro de um array
# resultado_usuarios_op_comparacao = collection_usuarios.find({ "cidade": { "$nin": ["São Paulo", "Rio de Janeiro"] } })

# # Projeção
# resultado_usuarios_projecao = collection_usuarios.find({}, { "nome": 1, "idade": 1 })

# Ordenação
resultado_usuarios_projecao = collection_usuarios.find().sort({ "idade": 1 })

# # Limitação
# resultado_usuarios_projecao = collection_usuarios.find().limit(10)

# # Paginação
# resultado_usuarios_projecao = collection_usuarios.find().skip(10).limit(5)

# Buscar documentos
documentos = collection_usuarios.find()
print("\nDocumentos no banco:")
for doc in documentos:
    print(doc)

# Fechar conexão
client.close()
