import datetime
import dateutil
import math
from math import *

from odoo import models, api, fields


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    def _add_date_libs(self, localdict):
        localdict.update({
            'datetime': datetime,
            'dateutil': dateutil,
            'fields': fields,
			'floor':floor,
			'ceil':ceil,
            })
        return localdict

    @api.multi
    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the environement in which to compute the rule
        :return: returns a tuple build as the base/amount computed, the quantity and the rate
        :rtype: (float, float, float)
        """
        self.ensure_one()
        localdict = self._add_date_libs(localdict)
        return super(HrSalaryRule, self)._compute_rule(localdict)

    @api.multi
    def _satisfy_condition(self, localdict):
        """
        @param contract_id: id of hr.contract to be tested
        @return: returns True if the given rule match the condition for the given contract. Return False otherwise.
        """
        self.ensure_one()
        localdict = self._add_date_libs(localdict)
        return super(HrSalaryRule, self)._satisfy_condition(localdict)

