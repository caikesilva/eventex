# Eventex - A maior reunião de hackers do mundo.

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virtualenv com python 3.8.10.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os testes.

```console
    git clone git@github.com:caikesilva/eventex.git wttd
    cd wttd
    python -m venv .wttd
    source .wttd/bin/activate
    pip install -r requirements-dev.txt
    cp contrib/env-sample .env
    python manage.py test
```

## Como fazer o deploy

1. Crie uma instancia no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instancia.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
    heroku create minhainstancia
    heroku config:push
    heroku config:set SECRET_KEY='python contrib/secret_gen.py'
    heroku config:set DEBUG=False
    #Configuro email
    git push heroku main --force
```