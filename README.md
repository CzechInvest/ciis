# CI-IS

CzecInvest information system - spatial-enabled, Django-based, internal
information system.

## Dependenices

Django and basic geo-stuff

```
pip install -r requirements.txt
```

## Setting up

```
django-admin startproject ciis
git clone https://github.com/czechinvest/ciis.git ciis_django
```

Now you have to adjust the `settings.py` file

1. Add `ciis_django` to `$PYTHONPATH`
2. Add ciis apps to `INSTALLED_APPS`
3. Add `django.contrib.gis` to `INSTALLED_APPS`
4. Adjust database engine for support of spatial models https://docs.djangoproject.com/en/1.11/ref/contrib/gis/tutorial/#configure-settings-py
5. If using `spatialite`, use `SPATIALITE_LIBRARY_PATH` settings option

In `settings.py`:

```
...
import sys
sys.path.append(os.path.join(BASEDIR, "../ciis_django/"))

...

INSTALLED_APPS = [
    'suppliers.apps.SuppliersConfig',
    'infrastructure.apps.InfrastructureConfig',
    'addresses.apps.AddressesConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.gis',
    ...
]

...

SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```


Do further settings modifications.

## Init databse

```
python manage.py makemigrations
python manage.py migrate
```

## Initial data load

Enumerations, address database ...

```
python manage.py import_suppliers
python manage.py import_infrastructure
python manage.py import_addresses # will take some time
python manage.py import_lau1
```

## Testing

```
python manage.py runserver
```

## Running in production

```
gunicorn -c gunicorn-config.py ciis.wsgi
```

## Docker 

Create local docker file `settings_local.py` with configuration content
Create local configuration file `local.env` with following content:

```
DB_HOST="database host"
DB_NAME="database name"
DB_USER="database user"
DB_PASSWD="password"
```

Run using `docker-compose web`

