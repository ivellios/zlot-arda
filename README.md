# Zlot Arda - website project

Website project in Python 2.7 / Django 1.5 for Arda Tolkienistic Convention in Poland.

# Important note
The project was developed in the closed environment for a years now. It has been moved to the public repository for community use. It is not a complete project - it does not include static files (may be included in the future), nor pictures or documents.

# Install & Running notes
In order to run the project you need to setup your own `settings_local.py` file in the `arda` dir. It should contain following settings:

```

DATABASES = {
    'default': {
        'ENGINE': 'd', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

MAIL_ACCOUNT = ''
MAIL_PASSWORD = ''
MAIL_SERVER = ''
MAIL_PORT = 0

```

# Depndencies

All necesary libs are listed in `requirements.txt` file. 
