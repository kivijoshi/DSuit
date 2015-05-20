"""
Django settings for DocTool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6#rnf-!yy_anv7i3_i6)4mrm)xy20578%faid)r!ogx7n9i*to'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'DoctorsCompanion',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webcam',
    
)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#TEMPLATE_DIRS = (
 #   os.path.join(os.path.dirname(__file__), 'DoctorsCompanion/templates/').replace('\\', '/'),
#)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),"..",'templates/').replace('\\', '/'),
)

PICTURE_ROOT = os.path.join(os.path.dirname(__file__),"..",'pictures').replace('\\', '/')
SUIT_CONFIG = {
  
    'ADMIN_NAME': 'Doctors Companion',
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'DoctorsCompanion': 'icon-heart',       
    },
  'MENU_EXCLUDE': ('DoctorsCompanion.billingsrec','DoctorsCompanion.timingsrec','DoctorsCompanion.medicinerec','auth'),  
   
  'MENU': (
         'sites',
         {'label': 'Patient', 'icon':'icon-plus', 'models': ('DoctorsCompanion.patientsrec',)},
         {'label': 'Finance', 'icon':'icon-signal', 'models': ('DoctorsCompanion.financialrecord',)},
         {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
         {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
     ),
    

}

print TEMPLATE_DIRS
print "***********************************************************************************************"
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DocTool.urls'

WSGI_APPLICATION = 'DocTool.wsgi.application'

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
print(os.getcwd())
STATIC_URL = os.path.join("..","/DoctorsCompanion/static/")
print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
print(STATIC_URL)