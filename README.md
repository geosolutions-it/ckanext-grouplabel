# CKAN plugin for rendering "`groups`" as "`categories`"

This extension overrides all the `.po` entries defined in CKAN which contain references to groups.

The `msgid`s have been extracted from a CKAN 2.9.5, so they may mismatch if used with other CKAN versions.  
 
Avalable languages so far: `it`, `en`, `en_GB`

## Plugins

Available plugins in this extension:

- ``grouplabel``: Replaces the label "group" with "category".

## Requirements

No requirements.

## Installation

1. Activate your CKAN virtual environment, for example:

     `. /usr/lib/ckan/default/bin/activate`
     
1. Go into your CKAN path for extension (e.g. `/usr/lib/ckan/default/src`):

    ```bash
    git clone https://github.com/geosolutions-it/ckanext-grouplabel.git
    cd ckanext-grouplabel 
    pip install -e .
    ```

4. Add ``grouplabel`` to the ``ckan.plugins`` setting in your CKAN config file (by default the config file is located at ``/etc/ckan/default/ckan.ini``).

5. Restart CKAN.   
   For example if you've deployed CKAN with Apache on Ubuntu::

       sudo service apache2 reload

## Development notes

Entries in the `.po` files have been created by hand, mainly grepping the CKAN i18n files.

Only the `python setup.py compile_catalog` command has been issues, since there are not templates in this extension. 


