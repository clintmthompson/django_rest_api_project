# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v84uo)8us6myo27ui6iylhtj9)31+$=6%9w&e+4eqqe2ba)@bc'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}