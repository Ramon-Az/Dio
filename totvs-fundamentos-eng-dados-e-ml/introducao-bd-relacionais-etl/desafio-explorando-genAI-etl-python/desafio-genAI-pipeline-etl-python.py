import pandas as pd
import json
import requests

# Carregar o arquivo CSV
df = pd.read_csv('./data/dados_clientes.csv')
user_ids = df['UserID'].tolist()
print(f"IDs solicitados: {user_ids}")

# Carregar dados do arquivo JSON local
with open('./data/find_one.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

# Função para obter usuário por ID do JSON
def get_user(id, dados):
    # Se dados for uma lista, busca por id
    if isinstance(dados, list):
        return next((user for user in dados if user['id'] == id), None)
    # Se dados for um único objeto, verifica se o id corresponde
    elif isinstance(dados, dict) and dados.get('id') == id:
        return dados
    return None

# Extração: buscar usuários pelos IDs do CSV
users = [user for id in user_ids if (user := get_user(id, dados_json)) is not None]
print(f"\nUsuários encontrados: {len(users)}")

# Transformação: mensagem personalizada com IA
def gerar_mensagem_ia(user):
    # Extrair descrições das notícias se news for lista
    news_text = user['news']
    if isinstance(news_text, list):
        news_text = ' '.join([item['description'] for item in news_text])
    
    prompt = f"""Crie uma mensagem de marketing personalizada para:
Nome: {user['name']}
Notícias: {news_text}

Seja breve, persuasivo e em português."""
    
    try:
        response = requests.post('http://localhost:11434/api/generate',
            json={
                "model": "llama3.1:8b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_gpu": 1,
                    "num_thread": 8
                }
            },
            timeout=60
        )
        return response.json()['response'].strip()
    except Exception as e:
        print(f"Erro IA: {e}")
        return f"Olá {user['name']}, confira nossas novidades!"

# Transformação com IA
for user in users:
    mensagem_gerada = gerar_mensagem_ia(user)
    print(f"\n✓ Mensagem gerada para {user['name']}")
    print(f"  {mensagem_gerada}")
    
    # Atualizar apenas o campo 'news' no JSON original
    if isinstance(dados_json, list):
        for json_user in dados_json:
            if json_user['id'] == user['id']:
                json_user['news'] = mensagem_gerada
                if 'mensagem_personalizada' in json_user:
                    del json_user['mensagem_personalizada']
                break
    elif isinstance(dados_json, dict) and dados_json.get('id') == user['id']:
        dados_json['news'] = mensagem_gerada
        if 'mensagem_personalizada' in dados_json:
            del dados_json['mensagem_personalizada']

# Salvar as alterações de volta no arquivo JSON
with open('./data/find_one.json', 'w', encoding='utf-8') as f:
    json.dump(dados_json, f, indent=2, ensure_ascii=False)

print(f"\n✓ Arquivo JSON atualizado com {len(users)} mensagens em 'news'")

