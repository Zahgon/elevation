# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 B-Open Solutions srl - http://bopen.eu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
import os
import subprocess
from contextlib import contextmanager

import fasteners

FOLDER_LOCKFILE_NAME = '.folder_lock'


def selfcheck(tools):
    """Audit the system for issues.

    :param tools: Tools description. Use elevation.TOOLS to test elevation.
    """
    pass


@contextmanager
def lock_tiles(datasource_root, tile_names):
    pass


@contextmanager
def lock_vrt(datasource_root, product):
    pass


def ensure_setup(root, folders=(), file_templates=(), force=False, **kwargs):
    pass


def check_call_make(path, targets=(), variables=()):
    pass
