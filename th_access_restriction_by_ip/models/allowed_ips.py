# -*- coding: utf-8 -*-
##############################################################################
from odoo import models, fields


class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    allowed_ips = fields.One2many('allowed.ips', 'users_ip', string='Adresse IP')


class AllowedIPs(models.Model):
    _name = 'allowed.ips'

    users_ip = fields.Many2one('res.users', string='Adresse IP')
    ip_address = fields.Char(string='Adresse IP autorisée')
