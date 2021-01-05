# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
import re


class PrintBilanWizards(models.TransientModel):
    _name = 'print.bilan'

    date_fin = fields.Date(
        string="A la date du",
        default=fields.date.today(),
    )
    est_comptabilise = fields.Boolean(
        string="Inclure les écritures non comptabilisées"
    )

    def imprimer_bilan(self):
        data = {}
        state = 'posted'
        if self.est_comptabilise == True:
            state = 'draft'
        liste_ecriture_comptable = []
        ecriture_comptable = self.env['account.move.line'].search(
            [('date', '<=', self.date_fin)])
        for e in ecriture_comptable:
            if e.move_id.state == state or e.move_id.state == 'posted':
                vals = {
                    'account_id': e.account_id.code,
                    'credit': e.credit,
                    'debit': e.debit,
                    'balance': e.balance,
                }
                liste_ecriture_comptable.append(vals)

        # Actif du bilan
        # immobilisations incorporelles
        immobilisation_incorporel = 0
        immobilisation_incorporel_amortissement = 0

        frais_de_developpement_et_de_prospection = 0
        frais_de_developpement_et_de_prospection_amortissement = 0

        brevets_licence_logiciel_et_droits_similaires = 0
        brevets_licence_logiciel_et_droits_similaires_amortissement = 0

        fonds_commercial_et_droit_au_bail = 0
        fonds_commercial_et_droit_au_bail_amortissement = 0

        autre_immobilisation_corporelles = 0
        autre_immobilisation_corporelles_amortissement = 0

        # immobilisations corporelles
        immobilisation_corporel = 0
        immobilisation_corporel_amortissement = 0

        terrains = 0
        terrains_amortissement = 0

        batiment = 0
        batiment_amortissement = 0

        amenagements_agencements_installations = 0
        amenagements_agencements_installations_amortissement = 0

        materiel_mobilier_et_actifs_biologiques = 0
        materiel_mobilier_et_actifs_biologiques_amortissement = 0

        materiel_de_transport = 0
        materiel_de_transport_amortissement = 0

        avance_et_acomptes_verse_sur_immobilisation = 0
        avance_et_acomptes_verse_sur_immobilisation_amortissement = 0

        # immobilisation financière
        immobilisation_financiere = 0
        immobilisation_financiere_amortissement = 0

        titre_de_participation = 0
        titre_de_participation_amortissement = 0

        autres_immobilisation_financiere = 0
        autres_immobilisation_financiere_amortissement = 0

        # actif ciculant
        actif_circulant_hao = 0
        actif_circulant_hao_amortissement = 0

        stock_et_en_cours = 0
        stock_et_en_cours_amortissement = 0
        #
        creances_et_emplois_assimiles = 0
        creances_et_emplois_assimiles_amortissement = 0

        fournisseurs_avances_versees = 0
        fournisseurs_avances_versees_amortissement = 0

        clients = 0
        clients_amortissement = 0

        autres_creances = 0
        autres_creances_amortissement = 0

        total_actif_cirulant = 0
        total_actif_cirulant_amortissement = 0

        # tresorerie actif
        titres_de_placement = 0
        titres_de_placement_amortissement = 0

        valeur_a_encaisser = 0
        valeur_a_encaisser_amortissement = 0

        banque_cheque_postaux_caisse_et_assimile = 0
        banque_cheque_postaux_caisse_et_assimile_amortissement = 0

        total_tresorerie_actif = 0
        total_tresorerie_actif_amortissement = 0

        # ecart_de_conversion_actif
        ecart_de_conversion_actif = 0

        # PASSIF DU BILAN
        # CAPRO RA
        capital = 0
        apporteurs_captial_non_appele = 0
        prime_liees_au_capital_social = 0
        ecarts_de_reevaluation = 0
        reserve_indisponible = 0
        reserve_libre = 0
        report_a_nouveau = 0
        resultat_net_de_exercice = 0
        subvention_investissement = 0
        provision_reglementees = 0
        total_capitaux_propres_et_ressources_assimilees = 0

        # DEFI RA
        emprunts_et_dettes_financieres_divers = 0
        dettes_de_location_acquisition = 0
        provisions_pour_risques_et_charges = 0
        total_dettes_financieres_et_ressources_assimilees = 0

        # Total resource stable
        total_ressources_stables = 0

        # PASSIF CIRCULANT
        dettes_circulantes_hao = 0
        clients_avance_recues = 0
        fournisseur_dexploitation = 0
        dettes_fiscales_et_sociales = 0
        autres_dettes = 0
        provision_pour_risque_a_court_terme = 0

        # Totla passif circulant
        total_passif_circulant = 0

        # tresorerie passif
        banque_credit_d_escompte = 0
        banque_etablissement_financier_et_credit_de_tresorerie = 0

        # total tresorerie passif
        total_tresorerie_passif = 0

        # ecart de converion passif
        ecart_de_converion_passif = 0

        # total general passif
        total_general_passif = 0

        for ecriture in liste_ecriture_comptable:
            # immobilisation incorporel
            # frais de developpement et de prospection 211, 2181, 2191
            if re.match('^211', ecriture['account_id']) or re.match('^2181', ecriture['account_id']) or re.match('^2191', ecriture['account_id']):
                frais_de_developpement_et_de_prospection += ecriture['balance']

             # amortissement
            if re.match('2811', ecriture['account_id']) or re.match('2818', ecriture['account_id']) or re.match('2911', ecriture['account_id']) or re.match('2918', ecriture['account_id']) or re.match('2919', ecriture['account_id']):
                frais_de_developpement_et_de_prospection_amortissement += ecriture['balance']

            if re.match('^212', ecriture['account_id']) or re.match('^213', ecriture['account_id']) or re.match('^214', ecriture['account_id']) or re.match('^2193', ecriture['account_id']):
                brevets_licence_logiciel_et_droits_similaires += ecriture['balance']

            # amortissment
            if re.match('2812', ecriture['account_id']) or re.match('2813', ecriture['account_id']) or re.match('2814', ecriture['account_id']) or re.match('2912', ecriture['account_id']) or re.match('2913', ecriture['account_id']) or re.match('2914', ecriture['account_id']) or re.match('2919', ecriture['account_id']):
                brevets_licence_logiciel_et_droits_similaires_amortissement += ecriture['balance']

            if re.match('^215', ecriture['account_id']) or re.match('^216', ecriture['account_id']):
                fonds_commercial_et_droit_au_bail += ecriture['balance']
            # amortissement
            if re.match('2815', ecriture['account_id']) or re.match('2816', ecriture['account_id']) or re.match('2915', ecriture['account_id']) or re.match('2916', ecriture['account_id']):
                fonds_commercial_et_droit_au_bail_amortissement += ecriture['balance']

            if re.match('^217', ecriture['account_id']) or re.match('^218', ecriture['account_id']) and not re.match('^2181', ecriture['account_id']) or re.match('^2198', ecriture['account_id']):
                autre_immobilisation_corporelles += ecriture['balance']
            # amortissement
            if re.match('2817', ecriture['account_id']) or re.match('2818', ecriture['account_id']) or re.match('2917', ecriture['account_id']) or re.match('2918', ecriture['account_id']) or re.match('2919', ecriture['account_id']):
                autre_immobilisation_corporelles_amortissement += ecriture['balance']

            # immobilisation corporel
            if re.match('^22', ecriture['account_id']):
                terrains += ecriture['balance']

            # amortissement
            if re.match('^282', ecriture['account_id']) or re.match('^292', ecriture['account_id']):
                terrains_amortissement += ecriture['balance']

            if re.match('^231', ecriture['account_id']) or re.match('^232', ecriture['account_id']) or re.match('^233', ecriture['account_id']) or re.match('^237', ecriture['account_id']) or re.match('^2391', ecriture['account_id']):
                batiment += ecriture['balance']
            # amortissement
            if re.match('^2831', ecriture['account_id']) or re.match('^2832', ecriture['account_id']) or re.match('^2833', ecriture['account_id']) or re.match('^2837', ecriture['account_id']) or re.match('^2931', ecriture['account_id']) or re.match('^2932', ecriture['account_id']) or re.match('^2933', ecriture['account_id']) or re.match('^2937', ecriture['account_id']) or re.match('^2939', ecriture['account_id']):
                batiment_amortissement += ecriture['balance']

            if re.match('^234', ecriture['account_id']) or re.match('^235', ecriture['account_id']) or re.match('^238', ecriture['account_id']) or re.match('^2392', ecriture['account_id']) or re.match('^2393', ecriture['account_id']):
                amenagements_agencements_installations += ecriture['balance']

            # amortissement
            if re.match('^2834', ecriture['account_id']) or re.match('^2835', ecriture['account_id']) or re.match('^2838', ecriture['account_id']) or re.match('^2934', ecriture['account_id']) or re.match('^2935', ecriture['account_id']) or re.match('^2938', ecriture['account_id']) or re.match('^2939', ecriture['account_id']):
                amenagements_agencements_installations_amortissement += ecriture['balance']

            if re.match('^24', ecriture['account_id']) and not re.match('^245', ecriture['account_id']) or re.match('^2495', ecriture['account_id']):
                materiel_mobilier_et_actifs_biologiques += ecriture['balance']
            # amortissement
            if re.match('^284', ecriture['account_id']) and not re.match('^2845', ecriture['account_id']) or re.match('^294', ecriture['account_id']) and not re.match('^2945', ecriture['account_id']) and not re.match('^2949', ecriture['account_id']) or re.match('^2949', ecriture['account_id']):
                materiel_mobilier_et_actifs_biologiques_amortissement += ecriture['balance']

            if re.match('^245', ecriture['account_id']) or re.match('^2495', ecriture['account_id']):
                materiel_de_transport += ecriture['balance']
            # amortissement
            if re.match('2845', ecriture['account_id']) or re.match('2945', ecriture['account_id']) or re.match('2949', ecriture['account_id']):
                materiel_de_transport_amortissement += ecriture['balance']

            if re.match('^251', ecriture['account_id']) or re.match('^252', ecriture['account_id']):
                avance_et_acomptes_verse_sur_immobilisation += ecriture['balance']
            # amortissement
            if re.match('^2951', ecriture['account_id']) or re.match('^2952', ecriture['account_id']):
                avance_et_acomptes_verse_sur_immobilisation_amortissement += ecriture['balance']

            # immobilisation financière
            if re.match('^26', ecriture['account_id']):
                titre_de_participation += ecriture['balance']

            # amortissement
            if re.match('^296', ecriture['account_id']):
                titre_de_participation_amortissement += ecriture['balance']

            if re.match('^27', ecriture['account_id']):
                autres_immobilisation_financiere += ecriture['balance']
            # amortissement
            if re.match('^297', ecriture['account_id']):
                autres_immobilisation_financiere_amortissement += ecriture['balance']

            # actif ciculant
            if re.match('^485', ecriture['account_id']) or re.match('^488', ecriture['account_id']):
                actif_circulant_hao += ecriture['balance']

            # amortissement
            if re.match('^498', ecriture['account_id']):
                actif_circulant_hao_amortissement += ecriture['balance']

            if re.match('^31', ecriture['account_id']) or re.match('^32', ecriture['account_id']) or re.match('^33', ecriture['account_id']) or re.match('^34', ecriture['account_id']) or re.match('^35', ecriture['account_id']) or re.match('^36', ecriture['account_id']) or re.match('^37', ecriture['account_id']) or re.match('^38', ecriture['account_id']):
                stock_et_en_cours += ecriture['balance']

            # amortissement
            if re.match('^39', ecriture['account_id']):
                stock_et_en_cours_amortissement += ecriture['balance']

            if re.match('^409', ecriture['account_id']):
                fournisseurs_avances_versees += ecriture['balance']

            # amortissement
            if re.match('^490', ecriture['account_id']):
                fournisseurs_avances_versees_amortissement += ecriture['balance']

            if re.match('^41', ecriture['account_id']) and not re.match('^419', ecriture['account_id']):
                clients += ecriture['balance']

            # amortissement
            if re.match('^491', ecriture['account_id']):
                clients_amortissement += ecriture['balance']

            if re.match('^185', ecriture['account_id']) and not re.match('^478', ecriture['account_id']) or re.match('^42', ecriture['account_id']) or re.match('^43', ecriture['account_id']) or re.match('^44', ecriture['account_id']) or re.match('^45', ecriture['account_id']) or re.match('^46', ecriture['account_id']) or re.match('^47', ecriture['account_id']):
                if ecriture['balance'] > 0:
                    autres_creances += ecriture['balance']

            # amortissement
            if re.match('^492', ecriture['account_id']) or re.match('^493', ecriture['account_id']) or re.match('^494', ecriture['account_id']) or re.match('^495', ecriture['account_id']) or re.match('^496', ecriture['account_id']) or re.match('^497', ecriture['account_id']):
                autres_creances_amortissement += ecriture['balance']

             # Total
            creances_et_emplois_assimiles = fournisseurs_avances_versees + \
                clients + autres_creances

            # amortissement
            creances_et_emplois_assimiles_amortissement = fournisseurs_avances_versees_amortissement + \
                clients_amortissement + autres_creances_amortissement

            # tresorerie actif
            if re.match('^50', ecriture['account_id']):
                titres_de_placement += ecriture['balance']

            # amortissement
            if re.match('^590', ecriture['account_id']):
                titres_de_placement_amortissement += ecriture['balance']

            if re.match('^51', ecriture['account_id']):
                valeur_a_encaisser += ecriture['balance']
            # amortissement
            if re.match('^591', ecriture['account_id']):
                valeur_a_encaisser_amortissement += ecriture['balance']

            if re.match('^52', ecriture['account_id']) or re.match('^57', ecriture['account_id']) or re.match('^53', ecriture['account_id']) or re.match('^54', ecriture['account_id']) or re.match('^55', ecriture['account_id']) or re.match('^581', ecriture['account_id']) or re.match('^582', ecriture['account_id']):
                if ecriture['balance'] > 0:
                    banque_cheque_postaux_caisse_et_assimile += ecriture['balance']
            # amortissement
            if re.match('^592', ecriture['account_id']) or re.match('^593', ecriture['account_id']) or re.match('^594', ecriture['account_id']):
                banque_cheque_postaux_caisse_et_assimile_amortissement += ecriture['balance']

            # total_tresorerie_actif
            total_tresorerie_actif = titres_de_placement + \
                valeur_a_encaisser + banque_cheque_postaux_caisse_et_assimile
            # amortissement
            total_tresorerie_actif_amortissement = titres_de_placement_amortissement + \
                valeur_a_encaisser_amortissement + \
                banque_cheque_postaux_caisse_et_assimile_amortissement

            if re.match('^478', ecriture['account_id']):
                ecart_de_conversion_actif += ecriture['balance']

            # PASSIF DU BILAN
            # CAPRO RA
            if re.match('^104', ecriture['account_id']) or re.match('^101', ecriture['account_id']):
                capital += ecriture['balance']

            if re.match('^109', ecriture['account_id']):
                apporteurs_captial_non_appele += ecriture['balance']

            if re.match('^105', ecriture['account_id']):
                prime_liees_au_capital_social += ecriture['balance']

            if re.match('^106', ecriture['account_id']):
                ecarts_de_reevaluation += ecriture['balance']

            if re.match('^111', ecriture['account_id']) or re.match('^112', ecriture['account_id']) or re.match('^113', ecriture['account_id']):
                reserve_indisponible += ecriture['balance']

            if re.match('^118', ecriture['account_id']):
                reserve_libre += ecriture['balance']

            if re.match('^12', ecriture['account_id']):
                report_a_nouveau += ecriture['balance']

            if re.match('^13', ecriture['account_id']):
                resultat_net_de_exercice += ecriture['balance']

            if re.match('^14', ecriture['account_id']):
                subvention_investissement += ecriture['balance']

            if re.match('^15', ecriture['account_id']):
                provision_reglementees += ecriture['balance']

            # DEFI RAA
            if re.match('^16', ecriture['account_id']) or re.match('^181', ecriture['account_id']) or re.match('^182', ecriture['account_id']) or re.match('^183', ecriture['account_id']) or re.match('^184', ecriture['account_id']):
                emprunts_et_dettes_financieres_divers += ecriture['balance']

            if re.match('^17', ecriture['account_id']):
                dettes_de_location_acquisition += ecriture['balance']

            if re.match('^19', ecriture['account_id']):
                provisions_pour_risques_et_charges += ecriture['balance']

            # PASSIF CIRCULANT

            if re.match('481', ecriture['account_id']) or re.match('482', ecriture['account_id']) or re.match('484', ecriture['account_id']) or re.match('4998', ecriture['account_id']):
                dettes_circulantes_hao += ecriture['balance']

            if re.match('^419', ecriture['account_id']):
                clients_avance_recues += ecriture['balance']

            if re.match('^40', ecriture['account_id']) and not re.match('^409', ecriture['account_id']):
                fournisseur_dexploitation += ecriture['balance']

            if re.match('^42', ecriture['account_id']) or re.match('^43', ecriture['account_id']) or re.match('^44', ecriture['account_id']):
                if ecriture['balance'] < 0:
                    dettes_fiscales_et_sociales += ecriture['balance']

            if re.match('^185', ecriture['account_id']) or re.match('^599', ecriture['account_id']) or re.match('^45', ecriture['account_id']) or re.match('^47', ecriture['account_id']) and not re.match('^479', ecriture['account_id']):
                if ecriture['balance'] < 0:
                    autres_dettes += ecriture['balance']

            if re.match('^499', ecriture['account_id']) or re.match('^45', ecriture['account_id']) and not re.match('^4998', ecriture['account_id']):
                provision_pour_risque_a_court_terme += ecriture['balance']

            if re.match('^564', ecriture['account_id']) or re.match('^565', ecriture['account_id']):
                banque_credit_d_escompte += ecriture['balance']

            if re.match('^52', ecriture['account_id']) or re.match('^53', ecriture['account_id']) or re.match('^561', ecriture['account_id']) or re.match('^566', ecriture['account_id']):
                if ecriture['balance'] < 0:
                    banque_etablissement_financier_et_credit_de_tresorerie += ecriture['balance']

            if re.match('^479', ecriture['account_id']):
                ecart_de_converion_passif += ecriture['balance']

        # Totaux
        # immobilisation incorporel
        immobilisation_incorporel = frais_de_developpement_et_de_prospection + \
            brevets_licence_logiciel_et_droits_similaires + \
            fonds_commercial_et_droit_au_bail + autre_immobilisation_corporelles

        # amortissement
        immobilisation_incorporel_amortissement = frais_de_developpement_et_de_prospection_amortissement + \
            brevets_licence_logiciel_et_droits_similaires_amortissement + \
            fonds_commercial_et_droit_au_bail_amortissement + \
            autre_immobilisation_corporelles_amortissement

        # immobilisation_corporel
        immobilisation_corporel = terrains + batiment + amenagements_agencements_installations + \
            materiel_mobilier_et_actifs_biologiques + materiel_de_transport + \
            avance_et_acomptes_verse_sur_immobilisation

        # amortissement
        immobilisation_corporel_amortissement = terrains_amortissement + batiment_amortissement + amenagements_agencements_installations_amortissement + \
            materiel_mobilier_et_actifs_biologiques_amortissement + materiel_de_transport_amortissement + \
            avance_et_acomptes_verse_sur_immobilisation_amortissement

        # immobilisation financière
        immobilisation_financiere = titre_de_participation + \
            autres_immobilisation_financiere

        immobilisation_financiere_amortissement = titre_de_participation_amortissement + \
            autres_immobilisation_financiere_amortissement

        # total actif immobilise
        total_actif_immobilise = immobilisation_incorporel + \
            immobilisation_corporel + immobilisation_financiere
        # amortissement
        total_actif_immobilise_amortissement = immobilisation_incorporel_amortissement + \
            immobilisation_corporel_amortissement + immobilisation_financiere_amortissement

        total_actif_cirulant = actif_circulant_hao + stock_et_en_cours + \
            fournisseurs_avances_versees+clients+autres_creances

        # amortissement
        total_actif_cirulant_amortissement = actif_circulant_hao_amortissement + stock_et_en_cours_amortissement + \
            fournisseurs_avances_versees_amortissement + \
            clients_amortissement + autres_creances_amortissement
        # total_general
        total_general = total_actif_immobilise + \
            total_actif_cirulant + total_tresorerie_actif

        # Amortissements
        total_general_amortissement = total_actif_immobilise_amortissement + \
            total_actif_cirulant_amortissement + total_tresorerie_actif_amortissement
        # Total CAPRO RA
        total_capitaux_propres_et_ressources_assimilees = capital + apporteurs_captial_non_appele + prime_liees_au_capital_social + ecarts_de_reevaluation + \
            reserve_indisponible + reserve_libre + report_a_nouveau + \
            resultat_net_de_exercice + subvention_investissement + provision_reglementees

        # TOTAL DEFIRA
        total_dettes_financieres_et_ressources_assimilees = emprunts_et_dettes_financieres_divers + \
            dettes_de_location_acquisition + provisions_pour_risques_et_charges

        # Total resource stable
        total_ressources_stables = total_capitaux_propres_et_ressources_assimilees + \
            total_dettes_financieres_et_ressources_assimilees

        # Total passif circulant
        total_passif_circulant = dettes_circulantes_hao + clients_avance_recues + fournisseur_dexploitation + \
            dettes_fiscales_et_sociales + autres_dettes + provision_pour_risque_a_court_terme

        # total tresorerie passif
        total_tresorerie_passif = banque_credit_d_escompte + \
            banque_etablissement_financier_et_credit_de_tresorerie

        # total general passif
        total_general_passif = total_ressources_stables + total_passif_circulant + \
            total_tresorerie_passif + ecart_de_converion_passif
        # date immobilisation_incorporel
        data['immobilisation_incorporel'] = immobilisation_incorporel
        data['immobilisation_incorporel_amortissement'] = immobilisation_incorporel_amortissement
        data['immobilisation_incorporel_net'] = immobilisation_incorporel + \
            immobilisation_incorporel_amortissement

        data['frais_de_developpement_et_de_prospection'] = frais_de_developpement_et_de_prospection
        data['frais_de_developpement_et_de_prospection_amortissement'] = frais_de_developpement_et_de_prospection_amortissement
        data['frais_de_developpement_et_de_prospection_net'] = frais_de_developpement_et_de_prospection + \
            frais_de_developpement_et_de_prospection_amortissement

        data['brevets_licence_logiciel_et_droits_similaires'] = brevets_licence_logiciel_et_droits_similaires
        data['brevets_licence_logiciel_et_droits_similaires_amortissement'] = brevets_licence_logiciel_et_droits_similaires_amortissement
        data['brevets_licence_logiciel_et_droits_similaires_net'] = brevets_licence_logiciel_et_droits_similaires + \
            brevets_licence_logiciel_et_droits_similaires_amortissement

        data['fonds_commercial_et_droit_au_bail'] = fonds_commercial_et_droit_au_bail
        data['fonds_commercial_et_droit_au_bail_amortissement'] = fonds_commercial_et_droit_au_bail_amortissement
        data['fonds_commercial_et_droit_au_bail_net'] = fonds_commercial_et_droit_au_bail + \
            fonds_commercial_et_droit_au_bail_amortissement

        data['autre_immobilisation_corporelles'] = autre_immobilisation_corporelles
        data['autre_immobilisation_corporelles_amortissement'] = autre_immobilisation_corporelles_amortissement
        data['autre_immobilisation_corporelles_net'] = autre_immobilisation_corporelles + \
            autre_immobilisation_corporelles_amortissement

        # data immobilisation_corporel
        data['immobilisation_corporel'] = immobilisation_corporel
        data['immobilisation_corporel_amortissement'] = immobilisation_corporel_amortissement
        data['immobilisation_corporel_net'] = immobilisation_corporel + \
            immobilisation_corporel_amortissement

        data['terrains'] = terrains
        data['terrains_amortissement'] = terrains_amortissement
        data['terrains_net'] = terrains + terrains_amortissement

        data['batiment'] = batiment
        data['batiment_amortissement'] = batiment_amortissement
        data['batiment_net'] = batiment + batiment_amortissement

        data['amenagements_agencements_installations'] = amenagements_agencements_installations
        data['amenagements_agencements_installations_amortissement'] = amenagements_agencements_installations_amortissement
        data['amenagements_agencements_installations_net'] = amenagements_agencements_installations + \
            amenagements_agencements_installations_amortissement

        data['materiel_mobilier_et_actifs_biologiques'] = materiel_mobilier_et_actifs_biologiques
        data['materiel_mobilier_et_actifs_biologiques_amortissement'] = materiel_mobilier_et_actifs_biologiques_amortissement
        data['materiel_mobilier_et_actifs_biologiques_net'] = materiel_mobilier_et_actifs_biologiques + \
            materiel_mobilier_et_actifs_biologiques_amortissement

        data['materiel_de_transport'] = materiel_de_transport
        data['materiel_de_transport_amortissement'] = materiel_de_transport_amortissement
        data['materiel_de_transport_net'] = materiel_de_transport + \
            materiel_de_transport_amortissement

        data['avance_et_acomptes_verse_sur_immobilisation'] = avance_et_acomptes_verse_sur_immobilisation
        data['avance_et_acomptes_verse_sur_immobilisation_amortissement'] = avance_et_acomptes_verse_sur_immobilisation_amortissement
        data['avance_et_acomptes_verse_sur_immobilisation_net'] = avance_et_acomptes_verse_sur_immobilisation + \
            avance_et_acomptes_verse_sur_immobilisation_amortissement

        # immobilisation financière
        data['immobilisation_financiere'] = immobilisation_financiere
        data['immobilisation_financiere_amortissement'] = immobilisation_financiere_amortissement
        data['immobilisation_financiere_net'] = immobilisation_financiere + \
            immobilisation_financiere_amortissement

        data['titre_de_participation'] = titre_de_participation
        data['titre_de_participation_amortissement'] = titre_de_participation_amortissement
        data['titre_de_participation_net'] = titre_de_participation + \
            titre_de_participation_amortissement

        data['autres_immobilisation_financiere'] = autres_immobilisation_financiere
        data['autres_immobilisation_financiere_amortissement'] = autres_immobilisation_financiere_amortissement
        data['autres_immobilisation_financiere_net'] = autres_immobilisation_financiere + \
            autres_immobilisation_financiere_amortissement

        data['total_actif_immobilise'] = total_actif_immobilise
        data['total_actif_immobilise_amortissement'] = total_actif_immobilise_amortissement
        data['total_actif_immobilise_net'] = total_actif_immobilise + \
            total_actif_immobilise_amortissement

        # actif ciculant
        data['actif_circulant_hao'] = actif_circulant_hao
        data['actif_circulant_hao_amortissement'] = actif_circulant_hao_amortissement
        data['actif_circulant_hao_net'] = actif_circulant_hao + \
            actif_circulant_hao_amortissement

        data['stock_et_en_cours'] = stock_et_en_cours
        data['stock_et_en_cours_amortissement'] = stock_et_en_cours_amortissement
        data['stock_et_en_cours_net'] = stock_et_en_cours + \
            stock_et_en_cours_amortissement

        data['creances_et_emplois_assimiles'] = creances_et_emplois_assimiles
        data['creances_et_emplois_assimiles_amortissement'] = creances_et_emplois_assimiles_amortissement
        data['creances_et_emplois_assimiles_net'] = creances_et_emplois_assimiles + \
            creances_et_emplois_assimiles_amortissement

        data['fournisseurs_avances_versees'] = fournisseurs_avances_versees
        data['fournisseurs_avances_versees_amortissement'] = fournisseurs_avances_versees_amortissement
        data['fournisseurs_avances_versees_net'] = fournisseurs_avances_versees + \
            fournisseurs_avances_versees_amortissement

        data['clients'] = clients
        data['clients_amortissement'] = clients_amortissement
        data['clients_net'] = clients + clients_amortissement

        data['autres_creances'] = autres_creances
        data['autres_creances_amortissement'] = autres_creances_amortissement
        data['autres_creances_net'] = autres_creances + \
            autres_creances_amortissement

        data['total_actif_cirulant'] = total_actif_cirulant
        data['total_actif_cirulant_amortissement'] = total_actif_cirulant_amortissement
        data['total_actif_cirulant_net'] = total_actif_cirulant + \
            total_actif_cirulant_amortissement

        # tresorerie actif
        data['titres_de_placement'] = titres_de_placement
        data['titres_de_placement_amortissement'] = titres_de_placement_amortissement
        data['titres_de_placement_net'] = titres_de_placement + \
            titres_de_placement_amortissement

        data['valeur_a_encaisser'] = valeur_a_encaisser
        data['valeur_a_encaisser_amortissement'] = valeur_a_encaisser_amortissement
        data['valeur_a_encaisser_net'] = valeur_a_encaisser + \
            valeur_a_encaisser_amortissement

        data['banque_cheque_postaux_caisse_et_assimile'] = banque_cheque_postaux_caisse_et_assimile
        data['banque_cheque_postaux_caisse_et_assimile_amortissement'] = banque_cheque_postaux_caisse_et_assimile_amortissement
        data['banque_cheque_postaux_caisse_et_assimile_net'] = banque_cheque_postaux_caisse_et_assimile + \
            banque_cheque_postaux_caisse_et_assimile_amortissement

        data['total_tresorerie_actif'] = total_tresorerie_actif
        data['total_tresorerie_actif_amortissement'] = total_tresorerie_actif_amortissement
        data['total_tresorerie_actif_net'] = total_tresorerie_actif + \
            total_tresorerie_actif_amortissement

        # ecart_de_conversion_actif
        data['ecart_de_conversion_actif'] = ecart_de_conversion_actif

        data['total_general'] = total_general
        data['total_general_amortissement'] = total_general_amortissement
        data['total_general_net'] = total_general + total_general_amortissement

        # PASSIF DU BILAN
        # CAPRO RA
        data['capital'] = capital
        data['apporteurs_captial_non_appele'] = apporteurs_captial_non_appele
        data['prime_liees_au_capital_social'] = prime_liees_au_capital_social
        data['ecarts_de_reevaluation'] = ecarts_de_reevaluation
        data['reserve_indisponible'] = reserve_indisponible
        data['reserve_libre'] = reserve_libre
        data['report_a_nouveau'] = report_a_nouveau
        data['resultat_net_de_exercice'] = resultat_net_de_exercice
        data['subvention_investissement'] = subvention_investissement
        data['provision_reglementees'] = provision_reglementees
        data['total_capitaux_propres_et_ressources_assimilees'] = total_capitaux_propres_et_ressources_assimilees

        # DEFI RA
        data['emprunts_et_dettes_financieres_divers'] = emprunts_et_dettes_financieres_divers
        data['dettes_de_location_acquisition'] = dettes_de_location_acquisition
        data['provisions_pour_risques_et_charges'] = provisions_pour_risques_et_charges
        data['total_dettes_financieres_et_ressources_assimilees'] = total_dettes_financieres_et_ressources_assimilees
        data['total_ressources_stables'] = total_ressources_stables

        # PASSIF CIRCULANT
        data['dettes_circulantes_hao'] = dettes_circulantes_hao
        data['clients_avance_recues'] = clients_avance_recues
        data['fournisseur_dexploitation'] = fournisseur_dexploitation
        data['dettes_fiscales_et_sociales'] = dettes_fiscales_et_sociales
        data['autres_dettes'] = autres_dettes
        data['provision_pour_risque_a_court_terme'] = provision_pour_risque_a_court_terme
        data['total_passif_circulant'] = total_passif_circulant
        data['banque_credit_d_escompte'] = banque_credit_d_escompte
        data['banque_etablissement_financier_et_credit_de_tresorerie'] = banque_etablissement_financier_et_credit_de_tresorerie
        data['total_tresorerie_passif'] = total_tresorerie_passif
        data['ecart_de_converion_passif'] = ecart_de_converion_passif

        data['total_general_passif'] = total_general_passif

        data['excercice'] = self.date_fin.year
        return self.env.ref('th_etats_syscohada_pdf.bilan_ohada_pdf_view_report').report_action(self, data=data)
