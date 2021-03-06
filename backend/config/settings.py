import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.getenv('DEBUG', True) != 'False'

if DEBUG:
    from dotenv import load_dotenv

    load_dotenv()
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'django_static/')


SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-_o#$ui!%cjrzcc111m4_lkq0f&791nlv8+bdh_a&l#l&6k5^8o'
)


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'backend',
    'marlo.sytes.net',
    'foodgram.marlo.keenetic.link',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colorfield',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'recipes.apps.RecipesConfig',
    'users.apps.UsersConfig',
    'tags.apps.TagsConfig',
    'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}


AUTH_USER_MODEL = 'users.User'
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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/django_static/'
MEDIA_URL = '/django_media/'
MEDIA_ROOT = os.path.join('django_media/')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'users.pagination.Pagination',
    'PAGE_SIZE': 6
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'SEND_ACTIVATION_EMAIL': False,
    'PASSWORD_RESET_CONFIRM_URL': 'set_password/{uid}/{token}',
    'SERIALIZERS': {
        'user': 'users.serializers.UserGetSerializer',
        'current_user': 'users.serializers.UserGetSerializer',
    },
    'PERMISSIONS': {
        'user': ('rest_framework.permissions.AllowAny',),
        'user_list': ('rest_framework.permissions.AllowAny',),
    },
    'HIDE_USERS': False,
}
