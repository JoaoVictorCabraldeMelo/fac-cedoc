# FAC-CeDoc

## startup
install virtualenv:

```sudo apt-get install virtualenv```

create virtualenv:

```virtualenv –p /usr/bin/python3 venv```

activate virtualenv (venv):

```source venv/bin/activate```

install django2.0:

```pip install django```

criar conexao com db(por enquanto sqlite3):

```cd cedoc/ && python3 manage.py migrate``` 

criar superusuario:

```python3 manage.py createsuperuser```

rodar servidor:

```python3 manage.py runserver``` 

setar static files

```python3 manage.py collectstatic```
