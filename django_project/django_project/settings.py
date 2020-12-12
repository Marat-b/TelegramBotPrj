"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from data import config

from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR3 = Path(__file__).resolve().parent.parent.parent
# T_CONFIG_DIR = os.path.abspath(os.path.join(BASE_DIR, '../data'))
# config_path = os.path.join(os.path.join(T_CONFIG_DIR, 'config.py'))
#
# print(f'BASE_DIR={BASE_DIR}\nBASE_DIR2={BASE_DIR2}\nT_CONFIG_DIR={T_CONFIG_DIR}\nconfig_path={config_path}')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j+=f^2fh9-@+ekj+hzug%u$aj+%_n3(msfnzmeep=sbn4j@zgf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_project.user_manager',
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

ROOT_URLCONF = 'django_project.django_project.urls'

TEMPLATES = [
	{
		'BACKEND':'django.template.backends.django.DjangoTemplates',
		'DIRS':[],
		'APP_DIRS':True,
		'OPTIONS':{
			'context_processors':[
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'django_project.django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
	'default':{
		'ENGINE':'django.db.backends.postgresql',
		'HOST':config.DBHOST,
		'NAME':config.DATABASE,
		'USER':config.PGUSER,
		'PASSWORD':config.PGPASSWORD,
	}
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'