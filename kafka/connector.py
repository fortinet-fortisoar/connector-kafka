"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector
from .operations import operations, _check_health
import requests


class Kafka(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations.get(operation)
        return action(config, params, **kwargs)

    def check_health(self, config):
        _check_health(config)
