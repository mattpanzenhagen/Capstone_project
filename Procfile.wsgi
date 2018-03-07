web: gunicorn hickory_theatre.wsgi --log-file -

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)