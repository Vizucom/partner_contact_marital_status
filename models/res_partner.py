# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    marital_status_id = fields.Many2one('partner_contact_marital_status.marital_status', 'Marital Status')
