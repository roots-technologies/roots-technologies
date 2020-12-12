# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class GesctothCours(models.Model):
    _name = 'gescoth.cours'
    _description = 'Cours'
    _rec_name="titre"

    titre = fields.Char(
        string='Titre du cours',
        required=True,
    )
    chapitre_ids = fields.One2many(
        'gescoth.cours.chapitre',
        'cours_id',
        string='Liste des chapitres',
    )
    niveau_ids = fields.Many2many(
        'gescoth.niveau',
        string='Niveaux d\'étude',
    )
    filiere_id = fields.Many2one(
        'gescoth.filiere',
        string='Filiere',
    )
    professeur_id = fields.Many2one(
        'gescoth.professeur',
        string='Professeur',
        required=True,
    )

class GesctothCoursChapitre(models.Model):
    _name = 'gescoth.cours.chapitre'
    _description = 'Chapitre'

    name = fields.Char(
        string='Nom du chapitre',
        required=True,
    )
    binary_file = fields.Binary(
        string='Aperçu',
        attachment=True,
    )
    contenu = fields.Html(
       string='Contenu du cours',
    )
    chapitre_id = fields.Many2one(
        'gescoth.cours.chapitre',
        string='Chapitre Mère',
    )
    cours_id = fields.Many2one(
        'gescoth.cours',
        string='Cours',
    )
    niveau_id = fields.Many2one(
        'gescoth.niveau',
        string='Niveau',
    )