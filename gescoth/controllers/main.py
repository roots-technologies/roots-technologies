# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Gescoth(http.Controller):

	@http.route('/gescoth/eleve/', website=True, auth='public')
	def gescoth_eleve(self, **kw):
		liste_des_eleves = request.env['gescoth.eleve'].sudo().search([])
		return request.render("gescoth.page_eleves", {
			'liste_des_eleves':liste_des_eleves
		})

	@http.route('/eleve/webform', type="http", website=True, auth='public')
	def eleve_webform(self, **kw):
		classes = request.env['gescoth.classe'].sudo().search([])
		return http.request.render("gescoth.create_eleve", {"classes":classes,})

	@http.route('/create/webeleve/', type="http", website=True, auth='public')
	def create_webeleve(self, **kw):
		request.env['gescoth.eleve'].sudo().create(kw)
		return request.render("gescoth.eleve_thanks", {})

	@http.route('/professeur/', type="http", website=True, auth='public')
	def professeur_list(self, **kw):
		professeurs = request.env['gescoth.professeur'].sudo().search([])
		return request.render("gescoth.liste_professeur", {'professeurs' : professeurs})

	@http.route('/cours/<int:cours_id>',type="http", website=True, auth="public")
	def gescoth_cours_chapitre(self,cours_id=None, **kw):
		chapitres = request.env['gescoth.cours.chapitre'].sudo().search([('cours_id','=', cours_id)])
		return request.render("gescoth.page_chapitres",{
			'chapitres' : chapitres,
		})

	@http.route('/cours/',type="http", website=True, auth="public")
	def gescoth_cours(self, **kw):
		cours = request.env['gescoth.cours'].sudo().search([])
		return request.render("gescoth.page_cours",{
			'cours' : cours,
	})
