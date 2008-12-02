#
from paste.script import templates

class FrameworkTemplate(templates.Template):

    egg_plugins = ['myapp']
    summary = 'Template for creating a basic Framework package'
    required_templates = ['basic_package']
    _template_dir = 'templates'
    use_cheetah = True

