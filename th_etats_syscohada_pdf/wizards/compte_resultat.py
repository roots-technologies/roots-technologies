# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
import re


class PrintCompteResultatWizards(models.TransientModel):
    _name = 'compte.resultat'

    date_fin = fields.Date(
        string="A la date du",
        default=fields.date.today(),
    )
    est_comptabilise = fields.Boolean(
        string="Inclure les écritures non comptabilisées"
    )

    def imprimer_compte_resultat(self):
        data = {}
        state = 'posted'
        if self.est_comptabilise == True:
            state = 'draft'
        liste_ecriture_comptable = []
        date_debut = str(self.date_fin.year) + '-01-01'
        ecriture_comptable = self.env['account.move.line'].search(
            [('date', '<=', self.date_fin), ('date', '>=', date_debut)])
        for e in ecriture_comptable:
            if e.move_id.state == state or e.move_id.state == 'posted':
                vals = {
                    'account_id': e.account_id.code,
                    'credit': e.credit,
                    'debit': e.debit,
                    'balance': e.balance,
                }
                liste_ecriture_comptable.append(vals)

        vente_de_marchandise = 0
        achat_de_marchandise = 0
        variation_de_stocks_de_marchandises = 0
        marge_commerciale = 0

        vente_de_produit_fabrique = 0
        travaux_services_vendus = 0
        produits_accessoires = 0
        chiffre_d_affaire = 0

        production_stockee_ou_destockage = 0
        production_immobilisee = 0
        subvention_d_exploitation = 0
        autres_produits = 0
        transferts_de_charges_d_exploitation = 0
        achat_de_matieres_premieres_et_fournitures_liees = 0
        variation_de_stocks_de_matieres_premieres_et_fournitures_liees = 0
        autres_achats = 0
        variation_de_stocks_d_autres_approvisionnements = 0
        transports = 0
        services_exterieurs = 0
        impots_et_taxes = 0
        autres_charges = 0
        valeur_ajoutee = 0

        charges_de_personnel = 0

        excedent_brut_d_exploitation = 0

        reprises_d_amortissements_de_provisions_et_depreciations = 0
        dotations_aux_amortissements_aux_provisions_et_depreciations = 0

        resultat_d_exploitation = 0

        revenus_financiers_et_assimiles = 0
        reprises_de_provisions_et_depreciations_financieres = 0
        transferts_de_charges_financieres = 0
        frais_financiers_et_charges_assimiles = 0
        dotations_aux_provisions_et_aux_depreciations_financieres = 0

        resultat_financier = 0
        resultat_des_activites_ordinaires = 0

        produits_des_cessions_d_immobilisations = 0
        autres_Produits_hao = 0
        valeurs_comptables_des_cessions_d_immobilisations = 0
        autres_charges_hao = 0

        resultat_hors_activite_ordinaire = 0

        participation_des_travailleurs = 0
        impot_sur_le_resultat = 0

        resultat_net = 0

        for ecriture in liste_ecriture_comptable:

            if re.match('^701', ecriture['account_id']):
                vente_de_marchandise += ecriture['balance']

            if re.match('^601', ecriture['account_id']):
                achat_de_marchandise += ecriture['balance']

            if re.match('^6031', ecriture['account_id']):
                variation_de_stocks_de_marchandises += ecriture['balance']

            if re.match('^702', ecriture['account_id']) or re.match('^703', ecriture['account_id']) or re.match('^704', ecriture['account_id']):
                vente_de_produit_fabrique += ecriture['balance']

            if re.match('^705', ecriture['account_id']) or re.match('^706', ecriture['account_id']):
                travaux_services_vendus += ecriture['balance']

            if re.match('^707', ecriture['account_id']):
                produits_accessoires += ecriture['balance']

            if re.match('^73', ecriture['account_id']):
                production_stockee_ou_destockage += ecriture['balance']

            if re.match('^72', ecriture['account_id']):
                production_immobilisee += ecriture['balance']

            if re.match('^71', ecriture['account_id']):
                subvention_d_exploitation += ecriture['balance']

            if re.match('^75', ecriture['account_id']):
                autres_produits += ecriture['balance']

            if re.match('^781', ecriture['account_id']):
                transferts_de_charges_d_exploitation += ecriture['balance']

            if re.match('^602', ecriture['account_id']):
                achat_de_matieres_premieres_et_fournitures_liees += ecriture['balance']

            if re.match('^6032', ecriture['account_id']):
                variation_de_stocks_de_matieres_premieres_et_fournitures_liees += ecriture['balance']

            if re.match('^604', ecriture['account_id']) or re.match('^605', ecriture['account_id']) or re.match('^608', ecriture['account_id']):
                autres_achats += ecriture['balance']

            if re.match('^6033', ecriture['account_id']):
                variation_de_stocks_d_autres_approvisionnements += ecriture['balance']

            if re.match('^61', ecriture['account_id']):
                transports += ecriture['balance']

            if re.match('^62', ecriture['account_id']) or re.match('^63', ecriture['account_id']):
                services_exterieurs += ecriture['balance']

            if re.match('^64', ecriture['account_id']):
                impots_et_taxes += ecriture['balance']

            if re.match('^65', ecriture['account_id']):
                autres_charges += ecriture['balance']

            if re.match('^66', ecriture['account_id']):
                charges_de_personnel += ecriture['balance']

            if re.match('^791', ecriture['account_id']) or re.match('^798', ecriture['account_id']) or re.match('^799', ecriture['account_id']):
                reprises_d_amortissements_de_provisions_et_depreciations += ecriture['balance']

            if re.match('^681', ecriture['account_id']) or re.match('^691', ecriture['account_id']):
                dotations_aux_amortissements_aux_provisions_et_depreciations += ecriture['balance']

            if re.match('^77', ecriture['account_id']):
                revenus_financiers_et_assimiles += ecriture['balance']

            if re.match('^797', ecriture['account_id']):
                reprises_de_provisions_et_depreciations_financieres += ecriture['balance']

            if re.match('^787', ecriture['account_id']):
                transferts_de_charges_financieres += ecriture['balance']

            if re.match('^67', ecriture['account_id']):
                frais_financiers_et_charges_assimiles += ecriture['balance']

            if re.match('^697', ecriture['account_id']):
                dotations_aux_provisions_et_aux_depreciations_financieres += ecriture['balance']

            if re.match('^82', ecriture['account_id']):
                produits_des_cessions_d_immobilisations += ecriture['balance']

            if re.match('^84', ecriture['account_id']) or re.match('^86', ecriture['account_id']) or re.match('^88', ecriture['account_id']):
                autres_Produits_hao += ecriture['balance']

            if re.match('^86', ecriture['account_id']):
                valeurs_comptables_des_cessions_d_immobilisations += ecriture['balance']

            if re.match('^83', ecriture['account_id']) or re.match('^83', ecriture['account_id']):
                autres_charges_hao += ecriture['balance']

            if re.match('^87', ecriture['account_id']):
                participation_des_travailleurs += ecriture['balance']

            if re.match('^89', ecriture['account_id']):
                impot_sur_le_resultat += ecriture['balance']

        # TOTAUX
        marge_commerciale = achat_de_marchandise + \
            vente_de_marchandise + variation_de_stocks_de_marchandises

        chiffre_d_affaire = vente_de_marchandise + \
            vente_de_produit_fabrique + travaux_services_vendus + produits_accessoires

        valeur_ajoutee = chiffre_d_affaire + achat_de_marchandise + variation_de_stocks_de_marchandises + production_stockee_ou_destockage + \
            production_immobilisee + subvention_d_exploitation + autres_produits + transferts_de_charges_d_exploitation + \
            achat_de_matieres_premieres_et_fournitures_liees + variation_de_stocks_de_matieres_premieres_et_fournitures_liees + autres_achats + \
            variation_de_stocks_d_autres_approvisionnements + transports + \
            services_exterieurs + impots_et_taxes + autres_charges

        excedent_brut_d_exploitation = valeur_ajoutee + charges_de_personnel

        resultat_d_exploitation = excedent_brut_d_exploitation + \
            reprises_d_amortissements_de_provisions_et_depreciations + \
            dotations_aux_amortissements_aux_provisions_et_depreciations

        resultat_financier = revenus_financiers_et_assimiles + reprises_de_provisions_et_depreciations_financieres + \
            transferts_de_charges_financieres + frais_financiers_et_charges_assimiles + \
            dotations_aux_provisions_et_aux_depreciations_financieres

        resultat_des_activites_ordinaires = resultat_d_exploitation + resultat_financier

        resultat_hors_activite_ordinaire = produits_des_cessions_d_immobilisations + \
            autres_Produits_hao + valeurs_comptables_des_cessions_d_immobilisations + autres_charges_hao

        resultat_net = resultat_des_activites_ordinaires + \
            resultat_hors_activite_ordinaire + \
            participation_des_travailleurs + impot_sur_le_resultat

        data['vente_de_marchandise'] = vente_de_marchandise
        data['achat_de_marchandise'] = achat_de_marchandise
        data['variation_de_stocks_de_marchandises'] = variation_de_stocks_de_marchandises
        data['marge_commerciale'] = marge_commerciale

        data['vente_de_produit_fabrique'] = vente_de_produit_fabrique
        data['travaux_services_vendus'] = travaux_services_vendus
        data['produits_accessoires'] = produits_accessoires
        data['chiffre_d_affaire'] = chiffre_d_affaire

        data['production_stockee_ou_destockage'] = production_stockee_ou_destockage
        data['production_immobilisee'] = production_immobilisee
        data['subvention_d_exploitation'] = subvention_d_exploitation
        data['autres_produits'] = autres_produits
        data['transferts_de_charges_d_exploitation'] = transferts_de_charges_d_exploitation
        data['achat_de_matieres_premieres_et_fournitures_liees'] = achat_de_matieres_premieres_et_fournitures_liees
        data['variation_de_stocks_de_matieres_premieres_et_fournitures_liees'] = variation_de_stocks_de_matieres_premieres_et_fournitures_liees
        data['autres_achats'] = autres_achats
        data['variation_de_stocks_d_autres_approvisionnements'] = variation_de_stocks_d_autres_approvisionnements
        data['transports'] = transports
        data['services_exterieurs'] = services_exterieurs
        data['impots_et_taxes'] = impots_et_taxes
        data['autres_charges'] = autres_charges
        data['valeur_ajoutee'] = valeur_ajoutee

        data['charges_de_personnel'] = charges_de_personnel

        data['excedent_brut_d_exploitation'] = excedent_brut_d_exploitation

        data['reprises_d_amortissements_de_provisions_et_depreciations'] = reprises_d_amortissements_de_provisions_et_depreciations
        data['dotations_aux_amortissements_aux_provisions_et_depreciations'] = dotations_aux_amortissements_aux_provisions_et_depreciations

        data['resultat_d_exploitation'] = resultat_d_exploitation

        data['revenus_financiers_et_assimiles'] = revenus_financiers_et_assimiles
        data['reprises_de_provisions_et_depreciations_financieres'] = reprises_de_provisions_et_depreciations_financieres
        data['transferts_de_charges_financieres'] = transferts_de_charges_financieres
        data['frais_financiers_et_charges_assimiles'] = frais_financiers_et_charges_assimiles
        data['dotations_aux_provisions_et_aux_depreciations_financieres'] = dotations_aux_provisions_et_aux_depreciations_financieres

        data['resultat_financier'] = resultat_financier
        data['resultat_des_activites_ordinaires'] = resultat_des_activites_ordinaires

        data['produits_des_cessions_d_immobilisations'] = produits_des_cessions_d_immobilisations
        data['autres_Produits_hao'] = autres_Produits_hao
        data['valeurs_comptables_des_cessions_d_immobilisations'] = valeurs_comptables_des_cessions_d_immobilisations
        data['autres_charges_hao'] = autres_charges_hao

        data['resultat_hors_activite_ordinaire'] = resultat_hors_activite_ordinaire
        data['participation_des_travailleurs'] = participation_des_travailleurs
        data['impot_sur_le_resultat'] = impot_sur_le_resultat

        data['resultat_net'] = resultat_net

        return self.env.ref('th_etats_syscohada_pdf.compte_resultat_pdf_view_report').report_action(self, data=data)
