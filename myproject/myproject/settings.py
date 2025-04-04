"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9o75n8hftrp^6nxekeydddu95z+1bj$#m2hn-!z@5zphbv6uuj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'backend',
    'corsheaders',
    'channels',
    

]
ASGI_APPLICATION = "myproject.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # ✅ 确保 JWTAuthentication 作为默认认证方式
    ),
}
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # 允许 Vue 前端访问的地址
    "http://127.0.0.1:5173",

    "http://172.30.131.225:5173"

]
# ✅ 允许 CSRF 跨域（如果用 Cookie 认证）
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^http://10\.223\..*:5173$",  # 允许所有 10.223.x.x 设备
#     r"^http://172\.30\..*:5173$" 
# ]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://10\.223\.\d+\.\d+:5173$",  # ✅ 允许所有 10.223.x.x 设备
    r"^http://172\.30\.\d+\.\d+:5173$",  # ✅ 允许所有 172.30.x.x 设备
]

CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "headers",  # Allow the 'headers' field
]

from datetime import timedelta
# ✅ 允许哪些 HTTP 方法
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS"
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),  # 设置 accessToken 有效期为 1 天
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # 设置 refreshToken 有效期为 7 天
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,  # 这里使用你的 Django SECRET_KEY
    "AUTH_HEADER_TYPES": ("Bearer",),
}
ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',       # 使用 MySQL 作为数据库引擎
#         'NAME': 'the_platform',               # 数据库名称
#         'USER': 'admin',             # 数据库用户名
#         'PASSWORD': 'itglasgow',         # 数据库密码
#         'HOST': 'database-1.c3iemm2ycfl8.us-east-1.rds.amazonaws.com',                # RDS 实例的 endpoint，如 mydb-instance.abcdefghijk.us-west-2.rds.amazonaws.com
#         'PORT': '3306',                             # 端口号，默认 3306
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'GoodsAndRooms',
        'USER': 'root',
        'PASSWORD': 'lx120688',
        'HOST': '127.0.0.1',  # Use 'localhost' if socket connection is enabled
        'PORT': '3306',
        'OPTIONS': {
            'auth_plugin': 'caching_sha2_password',
        },
    }
}





# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

# Storage settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "my-it-bucket-glasgow"
AWS_S3_REGION_NAME = "eu-north-1"  # Change to your AWS region
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

# Use S3 for media files
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
# 本地存储路径
MEDIA_URL = "/media/"  
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # 存放图片的本地路径