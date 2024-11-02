# Projeto Saúde em Primeiro Lugar


## Introdução

**Saúde Para Todos** é um aplicativo que permite o Cadastro e avaliação de Pacientes.

## Requisitos

- Python 
- Django 
- Mysql

## Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/VasconcelosVictor/projeto-saude
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. **Instale as dependências do backend:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure o banco de dados:**

    Crie um banco de dados na sua maquina e modifique as configurações de Banco de Dados pra sua Base.
    ```python
          DATABASES = {
              ''default': {
              'ENGINE': 'django.db.backends.mysql',  
              'NAME': 'NOME_DO_SEU_DATABASE',               
              'USER': 'SEU_USUÁRIO',                     
              'PASSWORD': 'SUA_SENHA',                  
              'HOST': 'localhost',                   
              'PORT': '3306',                      
          }
    
        }
    
     ```
## Execulte os Migrations do projeto 
    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8. **Acesse a aplicação:**
    Abra o navegador e vá para `http://localhost:8000`



## CASO DE TESTE 
  ```bash
    python manage.py test 
  ```



## Contato

- **Nome:** Victor Vasconcelos
- **LinkedIn:** [meu linkedin](https://www.linkedin.com/in/victor-vasconcelos-barbosa/)




