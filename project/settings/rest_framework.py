# flake8: noqa
from datetime import timedelta
from os import environ

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
    'BLACKLIST_AFTER_ROTATION': False,
    'SIGNING_KEY': environ.get('SECRET_KEY_JWT', 'INSECURE'),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
