# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from flask import request, g

from . import Resource, dentists
from .. import schemas


class Dentist(Resource):

    @staticmethod
    def get():
        queriedName = g.args.get('name')
        if queriedName:
            matchedDentists = [dentist for dentist in dentists if dentist['name'] == queriedName]
            return matchedDentists, 200, None
        return dentists, 200, None
