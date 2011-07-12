MEDIA_URL = "/2012/site_media/media/"
STATIC_URL = "/2012/site_media/static/"
ADMIN_MEDIA_PREFIX = "/2012/site_media/static/admin/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_HOST_USER = "sendgrid@eldarion.com"
EMAIL_HOST_PASSWORD = "at8di4op5va"
EMAIL_USE_TLS = True

SITE_ID = 2