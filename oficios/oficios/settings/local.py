from .base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE':'sql_server.pyodbc',
        'NAME':'OficiosDB',
        'Trusted_Connection':'yes',
        'HOST':'FERNANDO-PC\SQLEXPRESS',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0',
        }
    },
}
