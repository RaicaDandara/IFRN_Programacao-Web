from .settings import *
DEBUG = False
#Crie a secret key para seu ambiente de produção
SECRET_KEY = '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'
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}