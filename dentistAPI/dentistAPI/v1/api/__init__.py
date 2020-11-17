# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]


dentists = [
    {
        "id": 1,
        "name": "Dr Green",
        "location": "Sydney",
        "specialization": "Orthodontics"
    },
    {
        "id": 2,
        "name": "Dr James",
        "location": "Wollongong",
        "specialization": "Paediatric Dentistry"
    },
    {
        "id": 3,
        "name": "Dr Smith",
        "location": "Newcastle",
        "specialization": "Oral Surgery"
    }
]
