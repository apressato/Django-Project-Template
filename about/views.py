from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .utilities.ap_django_info import djangoInfo
from django.conf import settings
import os
import markdown

# Create your views here.

class PyInfoView(LoginRequiredMixin, TemplateView):
    """
    Show a page similar to phpinfo() about our virtual environment.
    """

    template_name = "about/djangoinfo.html"
    login_url = '/users/login'
    REDIRECT_FIELD_NAME = 'next'

    def get_context_data(self, **kwargs):
        context = super(PyInfoView, self).get_context_data(**kwargs)
        context["page_title"] = "PyInfo()"
        context["extra_css"] = []
        context["extra_javascript"] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        info = djangoInfo(settings=settings, request=request)
        info_data_html = {}
        for elementKey, elementValue in info.info_data.items():
            info_data_html[elementKey] = {}
            for k, v in elementValue.items():
                if isinstance(v, list):
                    if k != 'Environment':
                        v = [x for x in v if x.strip() != '']
                        v.sort()
                        info_data_html[elementKey][k] = mark_safe(f"<p>{'<br/>'.join(v)}</p>")
                    else:
                        info_data_html[elementKey][k] = mark_safe(f"<pre>{'<br/>'.join(v)}</pre>")
                elif isinstance(v, str):
                    if k not in ['Built-in Modules', 'server_api', 'Path Seperator', 'Python Version']:
                        if ';' in v:
                            v = v.split(';')
                            info_data_html[elementKey][k] = v
                        elif ',' in v:
                            v = [x for x in v.split(',') if x != ''].sort()
                            info_data_html[elementKey][k] = v
                        if isinstance(v, list):
                            info_data_html[elementKey][k] = mark_safe(f"<p>{'<br/>'.join(v)}</p>")
                        else:
                            info_data_html[elementKey][k] = v
                    else:
                        info_data_html[elementKey][k] = v
                else:
                    info_data_html[elementKey][k] = v
        info_data_context = {'info_data': info_data_html}
        context.update(info_data_context)

        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(PyInfoView, self).dispatch(*args, **kwargs)


def get_license(request):
    if os.path.isfile(os.path.join(settings.BASE_DIR, 'license.md')):
       license_md = open(os.path.join(settings.BASE_DIR, 'license.md'), encoding='utf-8').read()
    elif os.path.isfile(os.path.join(settings.BASE_DIR, 'license')):
       license_md = open(os.path.join(settings.BASE_DIR, 'license'), encoding='utf-8').read()
    else:
       license_md = "# License file not found\nIt seams that the license file was not found, this mean that you canave an incomplete release.\nPlease contact the author."
    html = markdown.markdown(license_md)
    context = {'license_html': html}

    return render(request, 'about/licensing.html', context)
