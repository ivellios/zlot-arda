import sys, os

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "arda.settings"



from  django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
