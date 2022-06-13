# ClickFile 
O projeto CLickFile foi desenvolvido para um teste técnico, foi utilizado o framework Django.
Caso seja definido as credenciais para o AWS S3 o sistema armazenará seus arquivos em nuvem, caso contrário serão armazenados no sistema de arquivo do computador.

### Pré-requisitos
 - Docker
 - Docker-compose
 - Psycopg2
 - Poetry


### Como utilizar
Apos a o clone do projeto é necessario entrar na pasta e baixar as dependencias

```console
foo@bar:~$ poetry install
```
logo após subir o banco de dados com:

```console
foo@bar:~$ docker-compose up
```
** Não é mais necessario, foi enviado o .env para o github ** </br>
copiar o arquivo `.env-sample` que está em contrib para a raiz do projeto removendo `"-sample"`

```console
foo@bar:~$ cp contrib/.env-sample  ./.env
```
> Mandarei os dados sensiveis por email assim que for avaliado serão desativados

### Como testar
- [Painel Admin](#painel-admin)
- [API RESTful](#why-use-it)
- [CLI](#how-to-use-it)

## Painel Admin
Crie um novo usuário e siga preenchendo as informações solicitada

```console
foo@bar:~$ python manage.py createsuperuser
```

execute a aplicação
```console
foo@bar:~$ python manage.py runserver
```

Acesse: <a href="http://127.0.0.1:8000/admin"> Painel Admin </a>

## API RESTful

execute a aplicação e utilize algo para requisitar as urls

- http://127.0.0.1:8000/api/v1/ - Lista os diretorios
- http://127.0.0.1:8000/api/v1/ - Recebe post com o name:str e parent:int
- http://127.0.0.1:8000/api/v1/{id} - Mostra apenas o diretorio selecionado
- http://127.0.0.1:8000/api/v1/files - Lista os arquivos
- http://127.0.0.1:8000/api/v1/files - Recebe post com o content:file e directory:int


```console
foo@bar:~$ python manage.py runserver
```

## CLI

Manipula apenas diretorios:

### Criando um novo diretorio
- params:
    - name: str = Nome do diretorio;
    - parent: int = Id do diretorio pai. (`Se o id não existir lançará um erro`)

```console
foo@bar:~$ python manage.py mkdir name 3
```

### Listando conteudo do diretorio
- params:
    - directory: int = Id do diretorio. 

```console
foo@bar:~$ python manage.py ls 3
```

### Removendo um diretorio e tudo que estiver dentro
- params:
    - directory: int = Id do diretorio. 

```console
foo@bar:~$ python manage.py rm 3
```



