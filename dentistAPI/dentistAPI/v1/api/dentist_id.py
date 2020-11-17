# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, dentists
from .. import schemas


class DentistId(Resource):

    def get(self, id):
        requestedID = id
        for dentist in dentists:
            if str(dentist['id']) == requestedID:
                return dentist, 200, None
        return {}, 404, None
