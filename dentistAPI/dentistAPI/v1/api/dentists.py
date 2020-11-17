# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import g

from . import Resource, dentists


class Dentists(Resource):

    @staticmethod
    def get():
        queriedName = g.args.get('name')
        if queriedName:
            matchedDentists = [dentist for dentist in dentists if dentist['name'] == queriedName]
            return matchedDentists, 200, None
        return dentists, 200, None
