# Eventex

Sistema de eventos encomendado pela Morena.

Demo: https://eventex-diegoubirajara.herokuapp.com

[![Build Status](https://travis-ci.org/dubirajara/eventex-WTTD.svg?branch=master)](https://travis-ci.org/dubirajara/eventex-WTTD)
[![codecov.io](https://codecov.io/github/dubirajara/eventex-WTTD/coverage.svg?branch=master)](https://codecov.io/github/dubirajara/eventex-WTTD?branch=master)
[![Code Health](https://landscape.io/github/dubirajara/eventex-WTTD/master/landscape.svg?style=flat)](https://landscape.io/github/dubirajara/eventex-WTTD/master)
[![Requirements Status](https://requires.io/github/dubirajara/eventex-WTTD/requirements.svg?branch=master)](https://requires.io/github/dubirajara/eventex-WTTD/requirements/?branch=master)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative seu virtualenv.
4. Instale as dependências.
5. Configure a instância como .env
6. Execute os testes.

```console
git clone git@github.com:dubirajara/eventex-WTTD.git wttd    
cd wttd         
python -m venv .wttd       
source .wttd/bin/activate  
pip install -r requirements-dev.txt  
cp contrib/env-sample .env  
python manage.py test  
```

## Como fazer o deploy?

1. Crie uma instâcia no Heroku.
2. Enviar as configuraçoes para o Heroku
3. Defina una SECRET KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku


```console
heroku create minhainstacia  
heroku config:push  
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`  
heroku config:set DEBUG=False  
#configuro o email
git push heroku master --force  
```

