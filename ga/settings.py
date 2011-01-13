from django.conf import settings
ANALYTICS_CODE = getattr(settings, 'GA_ANALYTICS_CODE', None)
VERIFICATION_CODE = getattr(settings, 'GA_VERIFICATION_CODE', None)
