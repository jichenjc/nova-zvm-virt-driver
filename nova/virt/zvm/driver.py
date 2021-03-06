# Copyright 2017 IBM Corp.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Shim layer for nova_zvm.virt.zvm.driver.ZVMDriver.

Duplicate all public symbols.  This is necessary for the constants as well as
the classes - because instances of the classes need to be able to resolve
references to the constants.
"""


import nova_zvm.virt.zvm.driver as real_drv


LOG = real_drv.LOG
CONF = real_drv.CONF
ZVMDriver = real_drv.ZVMDriver
