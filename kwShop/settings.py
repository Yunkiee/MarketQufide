"""
Django settings for kwShop project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import pymysql
import boto3

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't&&jr*p*hgk^x18$(1pmh@h8_muscl)=#fwqyidhm5v!y(t!-c'

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
    'storages',
    'shop',
    'django.contrib.sites', # 사이트 정보
    'allauth', # allauth 관련 앱 위해
    'allauth.account', # 가입한 계정 관리
    'allauth.socialaccount', # 소셜계정으로 가입한 계정 관리
    'allauth.socialaccount.providers.naver', # 사용하는 소셜 서비스(naver)
    'cart',
    'coupon',
    'order',
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

ROOT_URLCONF = 'kwShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kwShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kwShop', # 설정해둔 DataBase 이름
        'USER': '', # 설정해 둔 DB 관리자 계정pytho
        'PASSWORD': '', # 설정해 둔 DB 관리자 비번
        'HOST': '', # 만들어 논 DataBase의 엔드 포인트
        'PORT': '3306',
        #'OPTIONS': {
        #    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        #}
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = ( # 어떤 형식의 로그인을 할 것인 가
    'django.contrib.auth.backends.ModelBackend', # 사용자명(기본 로그인)
    'allauth.account.auth_backends.AuthenticationBackend', # 이메일 사용
)

SITE_ID = 1

CART_ID = 'cart_in_session'

LOGIN_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'django-kwshop'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com'%(AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'

#IAMPORT
IAMPORT_KEY = ''
IAMPORT_SECRET = ''

STATIC_URL = 'https://%s/%s/'%(AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'kwShop.asset_storage.MediaStorage' # 미디어 파일을 위한 파일 스토리지 설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
