import os
import re

from decouple import Config, RepositoryEnv
from dj_database_url import parse as db_url
import pytz
import yaml

from sapl.settings import *  # flake8: noqa


config = Config(RepositoryEnv(BASE_DIR.child('.env')))


INSTALLED_APPS += (
    'sapl.s3',
)

DATABASES['s3'] = config('DATABASE_URL_FONTE', cast=db_url,)

DATABASE_ROUTERS = ['sapl.s3.router.LegacyRouter', ]

DEBUG = True
