import os
from settings.base import *

# https://docs.microsoft.com/cs-cz/azure/key-vault/secrets/quick-create-python
# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential
# keyVaultName = os.environ["KEY_VAULT_NAME"]
# KVUri = f"https://{keyVaultName}.vault.azure.net"
# 
# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)
# SECRET_KEY = client.get_secret("DJ-SECRET-KEY")
SECRET_KEY = os.environ["DJ_SECRET_KEY"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ALLOWED_HOSTS=["localhost", os.environ['WEBSITE_HOSTNAME'], "ciis.czechinvest.org"]

DEBUG = True

#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True

DATABASES = {
            'default': {
                        'ENGINE': 'django.contrib.gis.db.backends.postgis',
                        'NAME': os.environ["DB_NAME"],
                        'PASSWORD': os.environ["DB_PASSWD"],
                        'USER': os.environ["DB_USER"],
                        'HOST': os.environ["DB_HOST"],
                        'PORT': 5432,
                }
}


# values you got from step 2 from your Mirosoft app
MICROSOFT_AUTH_CLIENT_ID = os.environ["MS_CLIENT_ID"]
MICROSOFT_AUTH_CLIENT_SECRET = os.environ["MS_CLIENT_SECRET"]

# pick one MICROSOFT_AUTH_LOGIN_TYPE value
# Microsoft authentication
# include Microsoft Accounts, Office 365 Enterpirse and Azure AD accounts
MICROSOFT_AUTH_LOGIN_TYPE = 'ma'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

