import common.constants

# https://medium.com/@malvin.lok/how-to-add-global-variable-on-django-template-83e57a96a8b5
# https://betterprogramming.pub/django-quick-tips-context-processors-da74f887f1fc
# https://stackoverflow.com/questions/3430451/using-django-settings-in-templates
# https://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/


def constant_context_processor(request):
    my_dict = {
        'SITE_NAME': common.constants.TITLE,
        "COPYRIGHT_NAME": common.constants.COPYRIGHT_NAME,
        "COPYRIGHT_URL": common.constants.COPYRIGHT_URL,
        "COPYRIGHT_YEARS": common.constants.COPYRIGHT_YEARS
    }
    return my_dict
