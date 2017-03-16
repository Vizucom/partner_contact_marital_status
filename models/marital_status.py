# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class MaritalStatus(models.Model):

    _name = 'partner_contact_marital_status.marital_status'
    _description = 'Marital status'

    name = fields.Char('Name', required=True, translate=True)
