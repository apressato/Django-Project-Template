#  Copyright (c) 2020-2023 by APressato <apressato.oss@gmail.com>
#
#  This file is part of Support_DashBoard.
#  Support_DashBoard is a website to help Support Teams in their work.
#
#  Support_DashBoard is free software: you can redistribute it and/or modify
#  it under the terms of the
#  Creative Commons Attribution ShareAlike 4.0 International
#  as published by Creative Commons.
#
#  Support_DashBoard is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY.  See the
#  Creative Commons Attribution ShareAlike 4.0 International for more details.
#
#  You should have received a copy of the
#  Creative Commons Attribution ShareAlike 4.0 International
#  along with Support_DashBoard. If not,
#  see <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

import re
from urllib.parse import urlsplit

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path
from django.views.static import serve


def static(prefix, view=serve, **kwargs):
    """
    Return a URL pattern for serving files in debug mode.

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")

    return [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs
        ),
    ]
