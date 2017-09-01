# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from flask import abort
from flask import Blueprint
from flask import Response
from oneview_redfish_toolkit.api.service_root import ServiceRoot

service_root = Blueprint('service_root', __name__)


@service_root.route('/', methods=["GET"])
def get_service_root():
    '''Gets ServiceRoot

    '''

    try:
        obj = ServiceRoot()
        json_str = obj.serialize()
        return Response(
            response=json_str,
            status=200,
            mimetype='application/json'
            )
    except Exception as e:
        # Todo: should be logging the error
        print(e)
        abort(500)