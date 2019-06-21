
from flask import Blueprint, current_app
from flask_restplus import Api
from .v1.task import task_namespace


api = Blueprint("api", __name__, url_prefix="/api/v1")

SCANAPP_API_v1 = Api(api,  doc='/apidoc/', version="v1")
SCANAPP_API_v1.add_namespace(task_namespace)

"""
from flask_restplus import Api
from .v1.task import task_namespace

from .namespace1 import api as ns1
api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)
api.add_namespace(ns1)
api.add_namespace(task_namespace)

"""