import os
from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta (Mantenha-a segura em produção)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# Configuração do modo de depuração
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# Definição das aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'distincoes',  # Seu aplicativo personalizado
    'djongo',  # Banco de dados MongoDB
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração do arquivo de URLs raiz
ROOT_URLCONF = 'piorfilme.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configurações WSGI e ASGI
WSGI_APPLICATION = 'piorfilme.wsgi.application'
ASGI_APPLICATION = 'piorfilme.asgi.application'

# Configuração do banco de dados (MongoDB)
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'EspecificacaoPiorFilme',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        },
    },
    'auth_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'auth_db.sqlite3',
    }
}


SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Padrão, usa o banco de dados principal


# Configurar o router para usar auth_db para autenticação
DATABASE_ROUTERS = ['distincoes.routers.AuthRouter']

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


from logging.handlers import TimedRotatingFileHandler

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'when': 'midnight',  # Rotaciona o log à meia-noite
            'interval': 1,  # Intervalo de rotação
            'backupCount': 7,  # Mantém até 7 arquivos de log antigos
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'distincoes': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
