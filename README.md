# Supabase Z-API Messenger

Projeto em Python que consulta contatos cadastrados no Supabase e envia mensagens personalizadas pelo WhatsApp utilizando a Z-API.

A mensagem enviada segue exatamente este formato:

```text
Olá, <nome_contato> tudo bem com você?
```

## Tecnologias

- Python
- Supabase
- Z-API

## Fluxo da aplicação

```text
Supabase → Python → Z-API → WhatsApp
```

1. O programa consulta os contatos ativos no Supabase.
2. Seleciona até três contatos, ordenados pela data de criação.
3. Personaliza a mensagem com o nome de cada contato.
4. Envia as mensagens pela Z-API.
5. Exibe um resumo com a quantidade de sucessos e falhas.

## Estrutura do projeto

```text
supabase-zapi-messenger/
├── src/
│   ├── main.py
│   ├── supabase_client.py
│   └── zapi_client.py
├── supabase/
│   └── schema.sql
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

- `src/main.py`: carrega as configurações, cria as mensagens e coordena os envios.
- `src/supabase_client.py`: consulta os contatos ativos no Supabase.
- `src/zapi_client.py`: realiza o envio das mensagens pela Z-API.
- `supabase/schema.sql`: permite reproduzir a estrutura da tabela de contatos.
- `.env.example`: documenta as variáveis de ambiente necessárias sem expor credenciais.

## Pré-requisitos

- Python instalado.
- Projeto criado no Supabase.
- Conta e instância criadas na Z-API.
- WhatsApp conectado à instância Z-API.

## Instalação

Clone o repositório e acesse a pasta do projeto:

```powershell
git clone https://github.com/ribeiro-7/supabase-zapi-messenger.git
cd supabase-zapi-messenger
```

Crie e ative um ambiente virtual no Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Configuração do Supabase

No SQL Editor do Supabase, execute o conteúdo de `supabase/schema.sql`. Esse script cria a tabela `contatos` com as seguintes colunas:

- `id`: identificador gerado automaticamente.
- `nome`: nome usado na personalização da mensagem.
- `telefone`: número único com DDI, DDD e apenas dígitos.
- `ativo`: define se o contato pode receber a mensagem.
- `created_at`: data e hora de criação do registro.

Cadastre de um a três contatos pelo Table Editor. O telefone deve ser informado sem `+`, espaços, parênteses ou hífens.

## Configuração da Z-API

1. Crie uma instância no painel da Z-API.
2. Conecte o WhatsApp pelo QR Code.
3. Localize o ID e o token da instância.
4. Em **Segurança**, configure o **Token de Segurança da Conta**.

## Variáveis de ambiente

Crie o arquivo `.env` a partir do modelo:

```powershell
Copy-Item .env.example .env
```

No Linux ou macOS:

```bash
cp .env.example .env
```

Preencha o `.env`:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-secreta-do-supabase
ZAPI_INSTANCE_ID=id-da-instancia
ZAPI_INSTANCE_TOKEN=token-da-instancia
ZAPI_CLIENT_TOKEN=token-de-seguranca-da-conta
```

- `SUPABASE_URL`: URL da API do projeto Supabase.
- `SUPABASE_KEY`: chave secreta utilizada pelo programa backend.
- `ZAPI_INSTANCE_ID`: identificador da instância Z-API.
- `ZAPI_INSTANCE_TOKEN`: token específico da instância.
- `ZAPI_CLIENT_TOKEN`: token de segurança da conta, enviado no cabeçalho `Client-Token`.

## Execução

> **Atenção:** o comando abaixo realiza envios reais para todos os contatos ativos retornados pela consulta, respeitando o limite de três.

No Windows:

```powershell
.\.venv\Scripts\python.exe src\main.py
```

No Linux ou macOS:

```bash
.venv/bin/python src/main.py
```

Exemplo de saída com dados fictícios:

```text
Mensagem enviada para Maria (final 1234).
Envios concluídos: 1 sucesso(s), 0 falha(s).
```

Se um envio falhar, o programa continua processando os demais contatos e retorna um resumo ao final.