
import ckan.plugins as plugins
import ckan.plugins.toolkit as plugins_toolkit
from ckan.lib.plugins import DefaultTranslation


class GroupLabelPlugin(plugins.SingletonPlugin, DefaultTranslation):

    # ITranslation
    plugins.implements(plugins.ITranslation)
