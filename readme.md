# 📚 Repositório DIO — Cursos & Bootcamps

Repositório de aprendizado prático desenvolvido durante cursos e bootcamps na plataforma [DIO (Digital Innovation One)](https://www.dio.me/). Reúne projetos, desafios de código e experimentos nas áreas de **Machine Learning**, **IA Generativa**, **Engenharia de Dados** e **Ciência de Dados**.

---

## 🗂️ Trilha de Cursos

| # | Curso / Bootcamp | Foco Principal |
|---|---|---|
| 01 | [Fundamentos de ML e GenAI](#01---fundamentos-de-ml-e-genai) | Reconhecimento de fala, transcrição com IA |
| 02 | [Bootcamp Bradesco: GenAI e Dados](#02---bootcamp-bradesco-genai-e-dados) | GenAI, SQL, estruturas de dados, agentes inteligentes |
| 03 | [Bootcamp TOTVS: Engenharia de Dados e ML](#03---bootcamp-totvs-engenharia-de-dados-e-ml) | ETL, MongoDB, redes neurais, cloud |
| 04 | Bootcamp Neo4j: Análise de Dados com Grafos | *(em andamento)* |

---

## 01 - Fundamentos de ML e GenAI

> **Objetivo:** Entender como computadores compreendem a linguagem humana por meio de modelos de IA.

📁 `fundamentos-ml-genai/exemplo-python-transcrever-audio-ia/`

### Conteúdo
- Transcrição de áudio em tempo real com **Google Speech Recognition**
- Reconhecimento de comandos de voz para automação de tarefas no sistema operacional
- Integração com a API do Google Speech (`pt-BR`)

### Stack
`Python` `SpeechRecognition` `PyAudio`

---

## 02 - Bootcamp Bradesco: GenAI e Dados

> **Objetivo:** Construir soluções práticas com IA Generativa, banco de dados relacional e estruturas de dados em Python.

📁 `bradesco-genai-dados/`

---

### 🤖 Pipeline de Voz com ChatGPT e Whisper

📁 `bradesco-genai-dados/ml-genai-chatgpt-whisper-python/`

Pipeline completo de interação por voz com IA:

```
Microfone → Whisper (STT) → ChatGPT → gTTS (TTS) → Reprodução de áudio
```

| Etapa | Tecnologia |
|---|---|
| Gravação de áudio | `sounddevice` + `scipy` |
| Transcrição (Speech-to-Text) | `openai-whisper` (local) |
| Geração de resposta | `openai` API — `gpt-3.5-turbo` |
| Síntese de voz (Text-to-Speech) | `gTTS` (Google) |
| Reprodução de áudio | `winsound` (Windows) |

**Configuração:**
```bash
cd bradesco-genai-dados/ml-genai-chatgpt-whisper-python
cp .env.example .env        # adicione sua OPENAI_API_KEY
pip install -r requirements.txt
python main.py
```

> ⚠️ Requer `ffmpeg` instalado: `choco install ffmpeg` (Windows)

---

### 🗄️ Excel ao SQL — ETL e Banco de Dados Relacional

📁 `bradesco-genai-dados/excel-ao-sql/`

- Modelagem e criação de banco de dados relacional
- Manipulação de dados com SQL (DDL, DML, consultas avançadas)
- Processo ETL com **Power Query** (Excel → banco de dados)
- Geração de schema com auxílio de IA Generativa

---

### 🐍 Python — Estruturas de Dados

📁 `bradesco-genai-dados/python-estruturas-dados/`

Módulo completo de estruturas de dados com exemplos práticos em Jupyter Notebook e desafios de código em múltiplas linguagens.

| Módulo | Conteúdo |
|---|---|
| `01-listas/` | Criação, fatiamento, métodos, compreensão de listas |
| `02-tuplas/` | Imutabilidade, desempacotamento, uso prático |
| `03-conjuntos/` | Operações de conjunto, deduplicação |
| `04-dicionarios/` | Acesso, iteração, dicionários aninhados |
| `05-funcoes/` | Funções, parâmetros, escopo, lambdas |

**Desafios de código implementados em 5 linguagens:**

| Desafio | Python | Java | C# | JavaScript | Kotlin |
|---|:---:|:---:|:---:|:---:|:---:|
| Corretora de valores | ✅ | ✅ | ✅ | ✅ | ✅ |
| Saldo diário bancário | ✅ | — | — | — | — |
| Remoção de duplicatas | ✅ | — | — | — | — |
| String maiúsculas | ✅ | — | — | — | — |

---

### 🧠 NotebookLM — Segundo Cérebro sobre Investimentos

📁 `bradesco-genai-dados/notebook-lm/`

Experimento com a plataforma **Google NotebookLM** para criar uma base de conhecimento sobre a metodologia de investimentos de **Benjamin Graham**.

- 🔗 [Notebook no NotebookLM](https://notebooklm.google.com/notebook/c28faba9-6ac8-492c-ab90-180e4cb9e292)
- 🗺️ Mapa mental gerado com IA
- 📄 Apresentação resumo: *Investimento Inteligente — Filosofia e Prática*

---

### 🏆 Desafio Final — Agente Inteligente Financeiro

Fork do projeto oficial da DIO: construção de um agente inteligente para o setor financeiro.

🔗 [dio-lab-bia-do-futuro](https://github.com/Ramon-Az/dio-lab-bia-do-futuro)

---

## 03 - Bootcamp TOTVS: Engenharia de Dados e ML

> **Objetivo:** Construir base sólida em Python, banco de dados, ETL e cloud, evoluindo até Machine Learning aplicado a desafios reais de mercado.

📁 `totvs-fundamentos-eng-dados-e-ml/`

---

### 📊 Análise de Dados com Excel e Copilot

📁 `totvs-fundamentos-eng-dados-e-ml/analise-dados-excel-copilot/`

- Dashboard de vendas Xbox construído no Excel com auxílio do **Microsoft Copilot**
- Aplicação do método **ABCDE** para priorização e tomada de decisão

---

### 🔬 Fundamentos e Técnicas de ML

📁 `totvs-fundamentos-eng-dados-e-ml/fundamentos-e-tecnicas-de-ml/`

| Notebook | Conteúdo |
|---|---|
| `01_exemplo_estruturas_simples.ipynb` | Estruturas condicionais e de repetição em Python |
| `02_codigo_python_para_ML.ipynb` | Regressão linear com `scikit-learn` e `matplotlib` |
| `03_rede_neural_do_zero.ipynb` | Rede neural com **PyTorch** treinada no dataset MNIST |

**Arquitetura da rede neural (MNIST):**
```
Input (784) → Linear(128) → ReLU → Linear(64) → ReLU → Linear(10) → LogSoftmax
Otimizador: SGD | Loss: NLLLoss | Epochs: 10
```

---

### 🗃️ Banco de Dados Relacionais e ETL com Python

📁 `totvs-fundamentos-eng-dados-e-ml/introducao-bd-relacionais-etl/`

| Arquivo | Descrição |
|---|---|
| `02_exemplos_com_mongodb_in_python.py` | CRUD completo no MongoDB com `pymongo` |
| `03_fundamentos_de_etl_com_python.py` | Pipeline ETL com `Luigi` e `pandas` |
| `desafio_etl_simples_para_processamento_vendas.py` | ETL de vendas com parsing de entrada |
| `desafio_transform_etl_de_nomes_para_processos_empresariais.py` | Transformação e normalização de strings |

**Pipeline ETL com Luigi:**
```
ExtractTask → TransformTask → LoadTask
(raw_data.csv) → (transformed_data.csv) → (final_data.csv)
```

**MongoDB via Docker:**
```bash
cd totvs-fundamentos-eng-dados-e-ml/introducao-bd-relacionais-etl
docker-compose up -d
```

---

### 🤖 Desafio: Pipeline ETL com IA Generativa

📁 `totvs-fundamentos-eng-dados-e-ml/introducao-bd-relacionais-etl/desafio-explorando-genAI-etl-python/`

Pipeline ETL que integra IA Generativa local (**Ollama + LLaMA 3.1**) para geração de mensagens de marketing personalizadas:

```
CSV (UserIDs) → JSON (dados clientes) → LLaMA 3.1 (mensagem personalizada) → JSON atualizado
```

---

### ☁️ Desafio: Redução de Custos com AWS

📁 `totvs-fundamentos-eng-dados-e-ml/nocoes-computacao-em-nuvem/`

Estudo de caso: proposta de redução de custos de infraestrutura para uma rede de farmácias utilizando serviços AWS.

---

### 🐍 Introdução à Ciência de Dados com Python

📁 `totvs-fundamentos-eng-dados-e-ml/introducao-ciencia-de-dados-e-python/`

- Desafio de decisão automática para aprovação de pedidos com lógica condicional
- Exercícios com operadores estruturais e condicionais

---

## 🛠️ Stack Tecnológico

### Linguagens
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)

### IA / ML
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)

### Dados & Infra
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonwebservices&logoColor=white)

---

## ⚙️ Instalação

```bash
# Clonar o repositório
git clone https://github.com/Ramon-Az/Dio.git
cd Dio

# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

# Instalar todas as dependências
pip install -r requirements.txt
```

> Para projetos específicos, consulte os comentários no `requirements.txt`.

---

## 📁 Estrutura do Repositório

```
Dio/
├── fundamentos-ml-genai/
│   └── exemplo-python-transcrever-audio-ia/   # Reconhecimento de voz com Google Speech
├── bradesco-genai-dados/
│   ├── ml-genai-chatgpt-whisper-python/        # Pipeline voz → Whisper → ChatGPT → TTS
│   ├── excel-ao-sql/                           # ETL Excel → SQL + Power Query
│   ├── python-estruturas-dados/                # Listas, tuplas, conjuntos, dicionários, funções
│   └── notebook-lm/                            # Análise de investimentos com NotebookLM
└── totvs-fundamentos-eng-dados-e-ml/
    ├── analise-dados-excel-copilot/            # Dashboard Excel + Copilot
    ├── fundamentos-e-tecnicas-de-ml/           # Regressão linear + Rede neural PyTorch
    ├── introducao-bd-relacionais-etl/          # MongoDB, Luigi ETL, pipeline GenAI
    ├── introducao-ciencia-de-dados-e-python/   # Desafios Python
    └── nocoes-computacao-em-nuvem/             # Estudo de caso AWS
```

---

## 📄 Licença

Este repositório é de uso educacional. Os projetos foram desenvolvidos como parte de cursos e bootcamps da plataforma DIO.
