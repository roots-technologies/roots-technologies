# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

# classe pour gérer les matières


class GescothMatiere(models.Model):
    _name = 'gescoth.matiere'
    _description = 'Gestion des matière'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('Cette matière existe déjà !')),
    ]

    name = fields.Char(string="Nom de la matière", required=True)
    nom_abrege = fields.Char(string="Nom abrégé")
    user_abrege = fields.Boolean(string="Utiliser le nom abrégé")
    type_matiere = fields.Selection([
        ('theorie', 'Théorique'),
        ('sport', 'Stportive')
    ],
        string="Type de matière",
        default="theorie",
        required=True,)


# classe pour ger les professeur
class GescothProfesseur(models.Model):
    _name = 'gescoth.professeur'
    _inherit = ['res.partner']
    _description = 'Gestion des professeurs'

    name = fields.Char(string="Nom et prénoms",
                       required=True, track_visibility='onchange')
    photo = fields.Binary(string="Photo de l'élève")
    date_naissance = fields.Date(
        string="Date de naissance", track_visibility='onchange')
    lieu_naissance = fields.Char(
        string="Lieu de naissance", track_visibility='onchange')
    sexe = fields.Selection(
        [('masculin', 'Masculin'), ('feminin', 'Féminin')], string="Sexe")
    nationalite = fields.Many2one('res.country', string="Nationalité")
    telephone = fields.Char(string="Téléphone", track_visibility='onchange')
    email = fields.Char(string="E-mail")
    adresse = fields.Text(string="Adresse complète")
    date_service = fields.Date(
        string='Date de prise de service'
    )
    salaire_base = fields.Float(string="Salaire de base")
    paie_par_heure = fields.Float(string="Paie par heure")
    statut = fields.Selection([('volontaire', 'Volontaire'), (
        'permanent', 'Permanent'), ('partiel', 'Partiel')], string='Statut')
    matieres = fields.Many2many('gescoth.matiere', string="Matière enseignées")
    active = fields.Boolean(string="Active", default=True)


# classe pour gerer les classes
class GescothClasse(models.Model):
    _name = 'gescoth.classe'
    _description = 'Gestion des classes'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('Cette classe existe déjà !')),
    ]

    name = fields.Char(string="Nom de la classe", required=True, index=True)
    description = fields.Char(string='Description')
    filiere = fields.Many2one('gescoth.filiere')
    professeur = fields.Many2one(
        'gescoth.professeur', string="Professeur titulaire")
    coeficient_ids = fields.One2many(
        'gescoth.coeficient', 'name', string="Coeficient de matières")
    eleve_ids = fields.One2many(
        'gescoth.eleve', 'classe', string="Liste des élèves")
    liste_des_eleves_total = fields.Integer(
        string='Total',
        compute="_liste_des_eleves_total"
    )
    niveau_id = fields.Many2one('gescoth.niveau')

    @api.multi
    def liste_des_eleves(self):
        return{
            'name': ('Elèves'),
            'domain': [('classe', '=', self.id)],
            'view_type': 'form',
            'res_model': 'gescoth.eleve',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def _liste_des_eleves_total(self):
        self.liste_des_eleves_total = len(
            self.env['gescoth.eleve'].search([('classe', '=', self.id)]))


# classe pour gerer les filières(series)
class GescothFiliere(models.Model):
    _name = 'gescoth.filiere'
    _description = 'Gestion des filiere'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('Cette filiere existe déjà !')),
    ]

    name = fields.Char(string="Nom de filiere", required=True)
    specialite = fields.Char(string="Spécialité")
    classe_ids = fields.One2many(
        'gescoth.classe', 'filiere', string="Liste des classe")


class gescothHoraire(models.Model):
    _name = 'gescoth.horaire'
    _description = 'Horaire'

    name = fields.Char(
        string='Horaire',
        required=True,
    )
    heure_debut = fields.Float(
        string='Heure de début',
        required=True,
    )
    heure_fin = fields.Float(
        string='Heure de fin',
        required=True,
    )


class gescothEmploiTemps(models.Model):
    _name = 'gescoth.emploi.temps'
    _description = 'Emploi du temps'
    _rec_name = 'jour'

    jour = fields.Selection([
        ('lundi', 'lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ], string="Jour", required=True,)

    classe_id = fields.Many2one(
        'gescoth.classe',
        string='Classe',
        required=True,
    )
    professeur_id = fields.Many2one(
        'gescoth.professeur',
        string='Professeur',
        required=True,
    )
    matiere_id = fields.Many2one(
        'gescoth.matiere',
        string='Matière',
        required=True,
    )

    horaire_id = fields.Many2one(
        'gescoth.horaire',
        string='Horaire',
    )
    heure_debut = fields.Float(
        string='Heure de début',
        # compute="_calculer_heure",
    )
    heure_fin = fields.Float(
        string='Heure de fin',
        # compute="_calculer_heure",
    )

    @api.onchange('horaire_id')
    def _onchange_horaire_id(self):
        for rec in self:
            rec.heure_fin = rec.horaire_id.heure_fin
            rec.heure_debut = rec.horaire_id.heure_debut


class GescothNiveau(models.Model):
    _name = 'gescoth.niveau'
    _description = 'Nieau'

    name = fields.Char(
        string='Description',
        required=True,
    )
    note = fields.Char(string="Note")
    frais_inscription = fields.Float(
        string="Frais d'inscription",
    )
    frais_formation = fields.Float(
        string="Frais de formation",
    )
    frais_internant = fields.Float(
        string="Frais d'internant",
    )
    frais_examen = fields.Float(
        string="Frais d'examen",
    )
    autres_frais = fields.Float(
        string="Autres frais",
    )
    classe_ids = fields.One2many(
        'gescoth.classe',
        'niveau_id',
        string='Classes',
    )

    frais_total = fields.Float(
        string="Frais total",
        compute='_onchange_frais',
    )

    @api.onchange('frais_inscription', 'frais_formation', 'frais_internant', 'frais_internant', 'frais_examen', 'autres_frais')
    def _onchange_frais(self):
        for rec in self:
            rec.frais_total = rec.frais_inscription + rec.frais_formation + \
                rec.frais_internant + rec.frais_examen + rec.autres_frais


class GescothEvenement(models.Model):

    _name = 'gescoth.evenement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Evénement'

    name = fields.Char(string="Nom de l'évènement", required=True)
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
    maxi_personne = fields.Integer(string="Maximum de participant")
    personnel_id = fields.Many2one(
        'gescoth.personnel',
        string='Organisateur',
    )
    nombre_limite = fields.Boolean(string="Le nombre de personnes est limité")
    nombre_peronne = fields.Integer(string="nombre de personne")
    participant_ids = fields.One2many('gescoth.enevement.participant', 'evement_id',
                                      string="Liste des participants")


class GescothEnevementParticipant(models.Model):

    _name = 'gescoth.enevement.participant'
    _description = 'Participant'
    _rec_name = "eleve_id"

    eleve_id = fields.Many2one(
        'gescoth.eleve',
        string='Elève',
    )
    date_inscription = fields.Date(string="Date d'inscription",)
    evement_id = fields.Many2one(
        'gescoth.evenement',
        string='Evénement',
    )
