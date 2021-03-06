# Copyright (c) ACSONE SA/NV 2018
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

import os

HTTP_HOST = os.environ.get("HTTP_HOST")
HTTP_PORT = int(os.environ.get("HTTP_PORT") or "8080")

GITHUB_SECRET = os.environ.get("GITHUB_SECRET")
GITHUB_LOGIN = os.environ.get("GITHUB_LOGIN")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GIT_NAME = os.environ.get("GIT_NAME")
GIT_EMAIL = os.environ.get("GIT_EMAIL")

ODOO_URL = os.environ.get("ODOO_URL", "https://odoo-community.org")
ODOO_DB = os.environ.get("ODOO_DB", "odoo_community_v11")
ODOO_LOGIN = os.environ.get("ODOO_LOGIN")
ODOO_PASSWORD = os.environ.get("ODOO_PASSWORD")

BROKER_URI = os.environ.get("BROKER_URI", os.environ.get("REDIS_URI", "redis://queue"))

SENTRY_DSN = os.environ.get("SENTRY_DSN")

DRY_RUN = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")
