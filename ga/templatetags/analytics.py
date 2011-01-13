from django.template import Library
register = Library()

from .. import settings

@register.inclusion_tag('ga/analytics.html')
def analytics(code=None):
    return {'code': code or settings.ANALYTICS_CODE}

@register.inclusion_tag('ga/verification.html')
def verification(code=None):
    return {'code': code or settings.VERIFICATION_CODE}
