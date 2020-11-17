# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource, dentists


class DentistsId(Resource):

    @staticmethod
    def get(id):
        requestedID = id
        for dentist in dentists:
            if str(dentist['id']) == requestedID:
                return dentist, 200, None
        return {}, 404, None
