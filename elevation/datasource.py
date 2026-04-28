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
import math
import os.path
import pkgutil
import uuid

import appdirs

from . import util

# declare public all API functions and constants
__all__ = [
    'info',
    'seed',
    'clip',
    'clean',
    'distclean',
    'CACHE_DIR',
    'DEFAULT_PRODUCT',
    'PRODUCTS',
    'DEFAULT_OUTPUT',
    'MARGIN',
    'TOOLS',
]

CACHE_DIR = appdirs.user_cache_dir('elevation', 'bopen')
DEFAULT_OUTPUT = 'out.tif'
MARGIN = '0'


def srtm1_tile_ilonlat(lon, lat):
    pass


def srtm3_tile_ilonlat(lon, lat):
    pass


def srtm1_tiles_names(left, bottom, right, top, tile_name_template='{slat}/{slat}{slon}.tif'):
    pass


def srtm3_tiles_names(left, bottom, right, top, tile_template='srtm_{ilon:02d}_{ilat:02d}.tif'):
    pass


def srtm_ellip_tiles_names(left, bottom, right, top, tile_name_template='{slat}{slon}_wgs84.tif'):
    pass


DATASOURCE_MAKEFILE = pkgutil.get_data('elevation', 'datasource.mk').decode('utf-8')

SRTM1_ELLIP_SPEC = {
    'folders': ('spool', 'cache'),
    'file_templates': {'Makefile': DATASOURCE_MAKEFILE},
    'datasource_url': 'https://opentopography.s3.sdsc.edu/raster/SRTM_GL1_Ellip/SRTM_GL1_Ellip_srtm',
    'tile_ext': '.tif',
    'compressed_pre_ext': '',
    'compressed_ext': '',
    'tile_names': srtm_ellip_tiles_names,
}

SRTM1_SPEC = {
    'folders': ('spool', 'cache'),
    'file_templates': {'Makefile': DATASOURCE_MAKEFILE},
    'datasource_url': 'https://s3.amazonaws.com/elevation-tiles-prod/skadi',
    'tile_ext': '.hgt',
    'compressed_pre_ext': '.hgt',
    'compressed_ext': '.hgt.gz',
    'tile_names': srtm1_tiles_names,
}

SRTM3_SPEC = {
    'folders': ('spool', 'cache'),
    'file_templates': {'Makefile': DATASOURCE_MAKEFILE},
    'datasource_url': 'https://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF',
    'tile_ext': '.tif',
    'compressed_pre_ext': '',
    'compressed_ext': '.zip',
    'tile_names': srtm3_tiles_names,
}

PRODUCTS_SPECS = collections.OrderedDict(
    [('SRTM1', SRTM1_SPEC), ('SRTM3', SRTM3_SPEC), ('SRTM1_ELLIP', SRTM1_ELLIP_SPEC),]
)

PRODUCTS = list(PRODUCTS_SPECS)
DEFAULT_PRODUCT = PRODUCTS[0]
TOOLS = [
    ('GNU Make', 'make --version'),
    ('curl', 'curl --help'),
    ('unzip', 'unzip -v'),
    ('gunzip', 'gunzip --version'),
    ('gdal_translate', 'gdal_translate --version'),
    ('gdalbuildvrt', 'gdalbuildvrt --version'),
]


def ensure_tiles(path, ensure_tiles_names=(), **kwargs):
    pass


# FIXME: force=True is an emergency hack to ensure that the file always contains the intended body
def ensure_setup(cache_dir, product, force=True):
    pass


def do_clip(path, bounds, output, product=DEFAULT_OUTPUT, **kwargs):
    pass


def seed(cache_dir=CACHE_DIR, product=DEFAULT_PRODUCT, bounds=None, max_download_tiles=9, **kwargs):
    """Seed the DEM to given bounds.

    :param cache_dir: Root of the DEM cache folder.
    :param product: DEM product choice.
    :param bounds: Output bounds in 'left bottom right top' order.
    :param max_download_tiles: Maximum number of tiles to process.
    :param kwargs: Pass additional kwargs to ensure_tiles.
    """
    pass


def build_bounds(bounds, margin=MARGIN):
    pass


def clip(bounds, output=DEFAULT_OUTPUT, margin=MARGIN, **kwargs):
    """Clip the DEM to given bounds.

    :param bounds: Output bounds in 'left bottom right top' order.
    :param output: Path to output file. Existing files will be overwritten.
    :param margin: Decimal degree margin added to the bounds. Use '%' for percent margin.
    :param cache_dir: Root of the DEM cache folder.
    :param product: DEM product choice.
    """
    pass


def info(cache_dir=CACHE_DIR, product=DEFAULT_PRODUCT):
    """Show info about the product cache.

    :param cache_dir: Root of the DEM cache folder.
    :param product: DEM product choice.
    """
    pass


def clean(cache_dir=CACHE_DIR, product=DEFAULT_PRODUCT):
    """Clean up the product cache from temporary files.

    :param cache_dir: Root of the DEM cache folder.
    :param product: DEM product choice.
    """
    pass


def distclean(cache_dir=CACHE_DIR, product=DEFAULT_PRODUCT):
    """Remove the product cache entirely.

    :param cache_dir: Root of the DEM cache folder.
    :param product: DEM product choice.
    """
    pass
