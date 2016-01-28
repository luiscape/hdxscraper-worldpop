#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
PARSER:
-------
This parser will intake dataverse dataset classes and
generate an HDX-like dictionary. It was designed to
register datasets in HDX in a posterior process.

'''
import os
import sys
import json
import requests

from copy import copy
from slugify import slugify
from datetime import datetime
from countrycode.countrycode import countrycode

def parse_dataset(data, private=True):
    '''
    Function that parses a dataset.

    '''
    #
    #  Check that there is acually
    #  metadata to parse.
    #
    # if data.get('worldPopData') is None:
    #     raise ValueError('No data to parse.')

    resource = {
        "package_id": str(slugify(data['Dataset Title']))[:90],
        "url": data['URL_direct'],
        "name": data['Location'] + '.zip',
        "format": 'zip',
        "description": None
    }

    metadata = {
        'name': str(slugify(data['Dataset Title']))[:90],
        'title': str(data['Dataset Title']),
        'owner_org': 'worldpop',
        'author': 'luiscape',
        'author_email': 'capelo@un.org',
        'maintainer': 'worldpop',
        'maintainer_email': 'ifpri-data@cgiar.org',
        'license_id': 'cc-by-sa',
        'dataset_date': None,    # has to be MM/DD/YYYY
        'subnational': 1,    # has to be 0 or 1. Default 1 for WorldPop.
        'notes': data['Description'],
        'caveats': None,
        'methodology': 'Other',
        'methodology_other': 'For more information about methods, please refer to ' + data['URL_summaryPag'],
        'dataset_source': data['Source'],
        'package_creator': 'luiscape',
        'private': private,    # has to be True or False
        'url': None,
        'state': 'active',    # always "active".
        'tags': [{ 'name': 'Map' }, { 'name': 'Population' }],    # has to be a list with { 'name': None }
        'groups': [ { 'id': countrycode(codes=str(data['Location']), origin='country_name', target='iso3c').lower() }]    # has to be ISO-3-letter-code. { 'id': None }
    }

    return { 'metadata': metadata, 'resource': resource }
