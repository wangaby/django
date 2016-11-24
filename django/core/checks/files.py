from __future__ import unicode_literals

from django.conf import settings

from . import Error, Tags, register


E999 = Error(
    "If set, MEDIA_URL must end with a slash",
    id='files.E999',
)


@register(Tags.caches)
def check_urls(app_configs, **kwargs):
    errors = []
    if settings.MEDIA_URL and not settings.MEDIA_URL.endswith('/'):
        errors.append(E999)

    return errors
