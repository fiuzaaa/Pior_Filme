
# Pior Filme API

## Descrição

A **Pior Filme API** é uma aplicação Django que permite a gestão e consulta de dados relacionados a filmes premiados. A API fornece endpoints para autenticação JWT e para calcular intervalos entre prêmios consecutivos de produtores.

## Instruções de Configuração

### 1. Clonar o Repositório

Clone o repositório para sua máquina local usando o comando abaixo:

```bash
git clone https://github.com/fiuzaaa/pior-filme.git
cd pior-filme
```

### 2. Criar um Ambiente Virtual

Crie um ambiente virtual Python para isolar as dependências do projeto:

```bash
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

Ative o ambiente virtual para começar a trabalhar no projeto:

- No **Windows**:
  ```cmd
  venv\Scripts\activate
  ```

- No **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar as Dependências

Instale as dependências do projeto usando o pip:

```bash
pip install -r requirements.txt
```

### 5. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente necessárias. Exemplo de configuração:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 6. Aplicar as Migrações

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### 7. Carregar Dados Iniciais

Se necessário, carregue dados iniciais a partir de um arquivo CSV usando o comando customizado:

```bash
python manage.py carregar_dados_csv path/to/movielist.csv
```

### 8. Executar os Testes

Execute os testes automatizados para garantir que tudo está funcionando corretamente:

```bash
python manage.py test
```

### 9. Executar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O servidor estará acessível em `http://127.0.0.1:8000/`.

## Endpoints da API

### Autenticação

A API usa autenticação JWT. Antes de acessar os endpoints protegidos, você deve obter um token JWT.

- **Obter Token JWT:**
  ```http
  POST /api/token/
  ```
  Envie as credenciais do usuário (username e password) no corpo da requisição para obter o token JWT.

- **Atualizar Token JWT:**
  ```http
  POST /api/token/refresh/
  ```
  Envie o token de refresh para obter um novo token de acesso.

### Endpoints de Intervalos

- **Obter Intervalos entre Prêmios:**
  ```http
  GET /api/intervalo/
  ```
  Retorna os produtores com maior e menor intervalo entre prêmios consecutivos. Este endpoint requer autenticação JWT.

  **Exemplo de Resposta:**
  ```json
  {
      "min": [
          {
              "produtor": "Producer 1",
              "intervalo": 1,
              "previousWin": 2001,
              "followingWin": 2002
          }
      ],
      "max": [
          {
              "produtor": "Producer 2",
              "intervalo": 10,
              "previousWin": 2000,
              "followingWin": 2010
          }
      ]
  }
  ```

## Estrutura de Pastas

A estrutura do projeto segue as boas práticas recomendadas para projetos Django:

```
├── piorfilme/             # Diretório principal do projeto Django
│   ├── settings.py        # Configurações do Django
│   ├── urls.py            # Definição das rotas principais
│   ├── wsgi.py            # Configuração do WSGI
│   ├── asgi.py            # Configuração do ASGI (se necessário)
├── distincoes/            # Aplicação Django para gestão dos filmes
│   ├── models.py          # Modelos do Django
│   ├── views.py           # Views da aplicação
│   ├── urls.py            # Rotas específicas da aplicação
│   ├── services.py        # Lógica de negócios e cálculos
│   ├── tests/             # Testes automatizados
│   ├── migrations/        # Migrações do banco de dados
├── data/                  # Arquivos de dados como CSVs
│   └── movielist.csv      # Exemplo de arquivo CSV para carregar filmes
├── manage.py              # Comando de gerenciamento do Django
├── .env                   # Variáveis de ambiente (não versionado)
├── db.sqlite3             # Banco de dados SQLite
├── auth_db.sqlite3        # Banco de dados de autenticação
└── requirements.txt       # Dependências do projeto
```

## Licença

Este projeto está licenciado sob a Licença LIVRE

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Contato

Para mais informações, entre em contato com o mantenedor do projeto:

- **Nome**: Raphael fiuza
- **Email**: fiuzaaa.raphael@gmail.com

---
