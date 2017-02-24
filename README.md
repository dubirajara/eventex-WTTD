# Eventex

Events & Conferences Web app. Developed using [Django Framework](https://www.djangoproject.com).

Demo: https://eventex-diegoubirajara.herokuapp.com

[![Build Status](https://travis-ci.org/dubirajara/eventex-WTTD.svg?branch=master)](https://travis-ci.org/dubirajara/eventex-WTTD)
[![Code Health](https://landscape.io/github/dubirajara/eventex-WTTD/master/landscape.svg?style=flat)](https://landscape.io/github/dubirajara/eventex-WTTD/master)
[![Updates](https://pyup.io/repos/github/dubirajara/eventex-wttd/shield.svg)](https://pyup.io/repos/github/dubirajara/eventex-wttd/)



## How Dev? Running locally.

1. Clone the repository.
2. Create a virtualenv with Python 3
3. Activate the virtualenv.
4. Install the dependencies.
5. Set up your local configuration file .env
6. Run tests.

```console
git clone git@github.com:dubirajara/eventex-WTTD.git wttd    
cd wttd         
python -m venv .wttd       
source .wttd/bin/activate  
pip install -r requirements-dev.txt  
cp contrib/env-sample .env  
python manage.py test  
```

## Deploying with Heroku.

1. Create a Heroku app.
2. Send your configuration variables to Heroku.
3. Define a secret key.
4. Disable debug mode.
5. Config email service.
6. Push your code.


```console
heroku create myinstance  
heroku config:push  
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`  
heroku config:set DEBUG=False  
#config your email
git push heroku master --force  
```

