# -*- coding: utf-8 -*-
import logging
from itertools import chain
from odoo.http import request
from odoo import models, fields, api
import requests

_logger = logging.getLogger(__name__)
USER_PRIVATE_FIELDS = ['password']
concat = chain.from_iterable


class LoginUserDetail(models.Model):
    _inherit = 'res.users'

    @api.model
    def _check_credentials(self, password):
        connection_info = requests.get("https://ipinfo.io/").json()
        result = super(LoginUserDetail, self)._check_credentials(password)
        ip_address = request.httprequest.environ['REMOTE_ADDR']
        vals = {'name': self.name,
                'ip_address': ip_address,
                'ip_internet':connection_info["ip"],
                'connection_country':connection_info["country"],
                'connection_region':connection_info["region"],
                'geo_localisation':connection_info["loc"],
                'telecom_net_work':connection_info["org"],
                'time_zone':connection_info["timezone"],
                'techniques_details':connection_info,
                }
        self.env['login.detail'].sudo().create(vals)
        return result


class LoginUpdate(models.Model):
    _name = 'login.detail'

    name = fields.Char(string="Nom d'utilisateur")
    date_time = fields.Datetime(string="Date et heure de connexion", default=lambda self: fields.datetime.now())
    ip_address = fields.Char(string="Adresse IP")
    ip_internet = fields.Char(string="IP sur Internet")
    connection_country = fields.Char(string="Pays de connexion")
    connection_region = fields.Char(string="Région de connexion")
    geo_localisation = fields.Char(string="Géolocalisation")
    telecom_net_work = fields.Char(string="Réseau télécom")
    time_zone = fields.Char(string="Timezone de connexion")
    techniques_details = fields.Char(string="Détails techniques")
