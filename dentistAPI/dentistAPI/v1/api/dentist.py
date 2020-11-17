# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from flask import request, g

from . import Resource, dentists
from .. import schemas


class Dentist(Resource):

    @staticmethod
    def get():
        return dentists, 200, None
