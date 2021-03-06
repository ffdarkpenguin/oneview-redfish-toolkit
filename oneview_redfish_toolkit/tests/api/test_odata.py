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


import unittest
from unittest import mock


from oneview_redfish_toolkit.api.odata import Odata
from oneview_redfish_toolkit import util


class TestOdata(unittest.TestCase):
    """Tests for Odata class"""

    @mock.patch.object(util, 'OneViewClient')
    def setUp(self, oneview_client_mockup):
        """Tests preparation"""

        # Loading variable in util module
        util.load_config('redfish.conf')

    def test_class_instantiation(self):
        """Tests class instantiation and validation"""

        try:
            odata = Odata()
        except Exception as e:
            self.fail("Failed to instantiate Odata. Error: ".format(e))
        self.assertIsInstance(odata, Odata)

    def test_serialize(self):
        """Tests the serialize function result against known result"""

        odata = Odata()
        json_str = odata.serialize()

        with open(
            'oneview_redfish_toolkit/mockups_redfish/Odata.json'
        ) as f:
            odata_mockup = f.read()
        self.assertEqual(odata_mockup, json_str)
