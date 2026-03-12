# Pipeline ETL com IA Generativa para Personalização de Mensagens

## Visão Geral

Este projeto implementa um pipeline ETL (Extract, Transform, Load) integrado com Inteligência Artificial Generativa para geração automatizada de mensagens de marketing personalizadas. A solução demonstra a aplicação prática de GenAI em processos de transformação de dados, combinando técnicas de engenharia de dados com modelos de linguagem avançados.

## Objetivo

Desenvolver um sistema automatizado capaz de:
- Extrair dados de clientes de múltiplas fontes (CSV e JSON)
- Transformar informações genéricas em mensagens personalizadas utilizando IA
- Carregar os dados enriquecidos de volta ao banco de dados

## Arquitetura do Pipeline

### 1. Extract (Extração)
- **Fonte Primária**: Arquivo CSV (`dados_clientes.csv`) contendo IDs de usuários-alvo
- **Fonte Secundária**: Base de dados JSON (`find_one.json`) com informações completas dos clientes
- **Processo**: Leitura e correlação de dados entre as duas fontes através de identificadores únicos

### 2. Transform (Transformação)
- **Motor de IA**: Modelo Llama 3.1 (8B parâmetros) executado localmente via Ollama
- **Processamento**: Geração de mensagens de marketing contextualizadas baseadas em:
  - Nome do cliente
  - Histórico de notícias e interesses
  - Perfil comportamental
- **Personalização**: Cada mensagem é única e adaptada ao contexto individual do usuário

### 3. Load (Carga)
- **Destino**: Atualização do arquivo JSON original
- **Estratégia**: Substituição do campo `news` com as mensagens geradas pela IA
- **Integridade**: Preservação de todos os demais campos e estrutura de dados

## Stack Tecnológico

### Linguagem e Bibliotecas
- **Python 3.x**: Linguagem principal
- **pandas**: Manipulação e análise de dados estruturados
- **requests**: Comunicação HTTP com API do modelo de IA
- **json**: Processamento de dados JSON

### Infraestrutura de IA
- **Ollama**: Servidor local para execução de modelos LLM
- **Llama 3.1 (8B)**: Modelo de linguagem para geração de texto
- **Configuração**: Otimização com GPU e multi-threading

## Estrutura do Projeto

```
desafio-explorando-genAI-etl-python/
├── data/
│   ├── dados_clientes.csv          # IDs dos clientes-alvo
│   └── find_one.json                # Base de dados completa
├── assets/
│   ├── 01-teste-mesangem-personalizada-usuario-ana.png
│   └── 02-teste-mensagem-personalizada-varios-usuarios-carregados-bd-json.png
├── desafio-genAI-pipeline-etl-python.py    # Script principal
└── readme.md                        # Documentação
```

## Funcionalidades Implementadas

### Extração Inteligente
```python
# Carregamento de IDs do CSV
df = pd.read_csv('./data/dados_clientes.csv')
user_ids = df['UserID'].tolist()

# Busca correlacionada no JSON
users = [user for id in user_ids if (user := get_user(id, dados_json)) is not None]
```

### Geração de Mensagens com IA
```python
def gerar_mensagem_ia(user):
    prompt = f"""Crie uma mensagem de marketing personalizada para:
    Nome: {user['name']}
    Notícias: {news_text}
    
    Seja breve, persuasivo e em português."""
    
    response = requests.post('http://localhost:11434/api/generate',
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()['response'].strip()
```

### Persistência de Dados
- Atualização atômica do arquivo JSON
- Codificação UTF-8 para suporte a caracteres especiais
- Formatação com indentação para legibilidade

## Tratamento de Erros

O sistema implementa estratégias robustas de tratamento de exceções:
- **Timeout de API**: Limite de 60 segundos para requisições
- **Fallback**: Mensagens genéricas em caso de falha da IA
- **Logging**: Feedback detalhado de cada etapa do processo

## Resultados

### Métricas de Execução
- **Usuários Processados**: 3 clientes (IDs: 4, 5, 6)
- **Taxa de Sucesso**: 100% de mensagens geradas
- **Tempo Médio**: ~5-10 segundos por mensagem (dependente de hardware)

### Exemplos de Saída
As mensagens geradas demonstram:
- Personalização baseada no nome do cliente
- Contextualização com informações de produtos/serviços
- Tom persuasivo e profissional
- Linguagem natural em português

## Pré-requisitos

### Software
- Python 3.8+
- Ollama instalado e configurado
- Modelo Llama 3.1 (8B) baixado

### Bibliotecas Python
```bash
pip install pandas requests
```

### Configuração do Ollama
```bash
# Instalar Ollama
curl https://ollama.ai/install.sh | sh

# Baixar modelo Llama 3.1
ollama pull llama3.1:8b

# Iniciar servidor
ollama serve
```

## Execução

```bash
python desafio-genAI-pipeline-etl-python.py
```

### Saída Esperada
```
IDs solicitados: [4, 5, 6]

Usuários encontrados: 3

✓ Mensagem gerada para Ana Costa
  Olá Ana Costa! Você está procurando por algo novo e incrível?...

✓ Mensagem gerada para Pedro Oliveira
  Olá Pedro! Nossa equipe desenvolveu uma solução inovadora...

✓ Mensagem gerada para Carla Mendes
  Mensagem de marketing personalizada para Carla Mendes...

✓ Arquivo JSON atualizado com 3 mensagens em 'news'
```

## Casos de Uso

### Marketing Personalizado
- Campanhas de email marketing segmentadas
- Notificações push contextualizadas
- Mensagens in-app personalizadas

### Automação de Comunicação
- Geração em massa de conteúdo personalizado
- Respostas automatizadas baseadas em perfil
- Comunicação proativa com clientes

### Análise de Dados
- Enriquecimento de bases de dados
- Transformação de dados estruturados em linguagem natural
- Geração de insights textuais

## Diferenciais Técnicos

1. **Execução Local**: Modelo de IA rodando localmente, garantindo privacidade e controle
2. **Escalabilidade**: Arquitetura modular permite processamento em lote
3. **Flexibilidade**: Suporte a diferentes estruturas de dados (lista ou objeto único)
4. **Manutenibilidade**: Código limpo com separação clara de responsabilidades

## Melhorias Futuras

- [ ] Implementação de cache para otimizar requisições repetidas
- [ ] Suporte a múltiplos modelos de IA (GPT, Claude, etc.)
- [ ] Interface web para visualização e edição de mensagens
- [ ] Sistema de templates para diferentes tipos de campanha
- [ ] Métricas de qualidade das mensagens geradas

## Aprendizados

Este projeto demonstra:
- Integração prática de IA Generativa em pipelines de dados
- Manipulação eficiente de dados estruturados e semi-estruturados
- Arquitetura ETL aplicada a casos reais de negócio
- Uso de modelos LLM locais para processamento de linguagem natural

## Autor

Desenvolvido por ***Ramon Azevedo***, como parte do **Bootcamp TOTVS - Fundamentos de Engenharia de Dados e Machine Learning** na plataforma DIO (Digital Innovation One).

## Licença

Este projeto é parte de material educacional e está disponível para fins de aprendizado.
