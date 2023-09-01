#   This file is part of APUtils.
#   APUtils is a porting with addictions of my Embarcadero Delphi APUtils package
#   made by APressato <apressato.oss@gmail.com> in 2018 - 2023.
#
#   APUtils is free software: you can redistribute it and/or modify
#   it under the terms of the
#   Creative Commons Attribution ShareAlike 4.0 International
#   as published by Creative Commons.
#
#   APUtils is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   Creative Commons Attribution ShareAlike 4.0 International for more details.
#
#   You should have received a copy of the
#   Creative Commons Attribution ShareAlike 4.0 International
#   along with APUtils. If not,
#   see <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

from .ap_pyinfo import pyInfo
import json
import sys
import inspect

from django import __version__ as django_version
from django.template.engine import Engine
from django.conf import settings 


class djangoInfo(pyInfo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._request = kwargs.get('request')
        self._main_settings = kwargs.get('settings', settings)
        if self._request:
            self._request_class = type(self._request).__name__.replace("Request", "")
            self._request_class_version = self._request.environ.get(f"{self._request_class.lower()}.version")

    def _collect_info(self):
        super()._collect_info()
        if self._request:
            self.pyInfoDict['System']["server_api"] = f"{self._request_class} {self._request_class_version}"
            self.pyInfoDict['Request Variables'] = self._request.environ
            self.pyInfoDict['Cookies'] = self._request.COOKIES
        self._framework_info()

    def _framework_info(self):
        data = {'Django Version': django_version}
        try:
            data['Template Engine'] = Engine.get_default().default_builtins
        except:
            data['Template Engine'] = 'default'

        data['Environment'] = json.dumps({
            key: value
            for (key, value) in vars(self._main_settings).items()
            if not key.startswith("_") and not inspect.isclass(value) and not inspect.ismodule(value)
        }, indent=4, default=str).split('\n')[1:-1]

        # data['Environment'] = json.dumps(data['Environment'], indent=4, default=str).split('\n')
        self.pyInfoDict['Framework Info'] = data

    def _get_info(self):
        self._collect_info()
        return self.pyInfoDict

    info_data = property(fget=_get_info)


if __name__ == '__main__':
    myInfo = djangoInfo(settings=settings)
    print(json.dumps(myInfo.info_data, indent=4, default=str))
    quit()