from datetime import timedelta
from os import getenv
from pathlib import Path

# User Accounts
AUTH_USER_MODEL = "customusers.User"  # New custom user
LOGIN_REDIRECT_URL = "tickets_tickets"  # Log In
LOGOUT_REDIRECT_URL = "tickets_tickets"  # Log Out

# Build paths inside the project like this: ROOT_DIR / "subdir".
SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SRC_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", default="INVALID")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = getenv("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS").split(", ")
# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]


LOCAL_APPS = [
    # "accounts.apps.AccountsConfig",
    # "repairs.apps.RepairsConfig",
    # "users.apps.UsersConfig",
    "customusers.apps.CustomUsersConfig",
    "exchange_rates.apps.ExchangeRatesConfig",
    "tickets",
    "core",
    "comments",
    "shared",
    "authentication",
]

REST_FRAMEWORK_AUTHENTICATION = [
    "django.contrib.sites",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "djoser",
]

INSTALLED_APPS = (
    DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + REST_FRAMEWORK_AUTHENTICATION
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ROOT_DIR / "src/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",  # new
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# DataROOT
# https://docs.djangoproject.com/en/4.1/ref/settings/#dataROOTs

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": ROOT_DIR / "db.sqlite3",
    # }
    "default": {
        "ENGINE": getenv("DB_ENGINE"),
        "HOST": getenv("DB_HOST"),
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "PORT": getenv("DB_PORT"),
    }
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "uk"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# STATICFILES_DIRS = [ROOT_DIR / "src/static"]

# STATIC_ROOT = ROOT_DIR / "src/staticfiles"

MEDIA_URL = "/media/"

# MEDIA_ROOT = ROOT_DIR / "src/media"


# email
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SITE_ID = 1
# DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
# EMAIL_HOST = getenv("EMAIL_HOST")
# EMAIL_PORT = getenv("EMAIL_PORT")
# EMAIL_HOST_USER = getenv("EMAIL_USER")
# EMAIL_HOST_PASSWORD = getenv("EMAIL_PASS")
# EMAIL_USE_TLS = getenv("EMAIL_USE_TLS")


# Exchange rates service (Alpha Vantage)
# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json
ALPHA_VANTAGE_BASE_URL = getenv(
    "ALPHA_VANTAGE_BASE_URL", default="https://www.alphavantage.co"
)
ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY")

# User Authentication
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 2,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
