# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .api.dentists import Dentists
from .api.dentists_id import DentistsId

routes = [
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistsId, urls=['/dentists/<id>'], endpoint='dentists_id'),
]
