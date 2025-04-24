# Projeto Django - Instruções para Rodar

Este é um projeto Django para cadastro de produtos e clientes.

## Requisitos

- Python 3.x instalado
- Virtualenv (opcional, mas recomendado)

## Passo a passo para rodar o projeto

1. Clone o repositório ou copie os arquivos para sua máquina.

2. Abra o terminal na pasta do projeto.

3. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

6. (Opcional) Crie um superusuário para acessar o admin:

```bash
python manage.py createsuperuser
```

7. Rode o servidor de desenvolvimento:

```bash
python manage.py runserver
```

8. Acesse no navegador:

```
http://127.0.0.1:8000/
```

## Como usar

- Na página inicial, você pode adicionar produtos e clientes.
- Use a barra de pesquisa para buscar produtos e clientes cadastrados.
- Edite ou exclua produtos e clientes conforme necessário.

## Importante

- Para adicionar imagens aos produtos, certifique-se de que a pasta `media/` está configurada corretamente no `settings.py`.
- Durante o desenvolvimento, o servidor Django serve os arquivos de mídia automaticamente.
