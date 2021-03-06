# -*- coding: utf-8 -*-
import os
import socket

from .domain.config import ServerConfig, ApiConfig


class Config(object):
    def __init__(self, environment, server_config, api_config):
        self.environment = environment
        self.server_config = server_config
        self.api_config = api_config


def _load_unsafe():
    return {
        'port': int(os.environ.get('PORT')),
        'host': os.environ.get('HOST'),
        'host_ip': socket.gethostbyname(socket.gethostname()),
        'environment': os.environ.get('ENVIRONMENT'),
        'api_endpoint': os.environ['API_ENDPOINT'],
    }


def load():
    env = _load_unsafe()
    return Config(
        env['environment'],
        ServerConfig(
            env['host'],
            env['port'],
            env['host_ip']
        ),
        ApiConfig(env['api_endpoint']),
    )
