# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class GescothReglePaie(models.Model):

    _name = 'gescoth.regle.paie'
    _description = 'Règles de paie'

    name = fields.Char(string="Nom")
    montant = fields.Float("Montant")
