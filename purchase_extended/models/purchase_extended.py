# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseExtended(models.Model):
    _inherit = 'purchase.order'
    _description = 'Class to modify the purchasing module'

    type = fields.Selection([
        ('national', 'National'),
        ('international', 'International')],
        string='Type'
    )

    project_id = fields.Many2one(
        'project.project', string='Project'
    )

    code = fields.Char(
        string='Code', default=lambda self: self.env['ir.sequence'].next_by_code('purchase.order.code') or self.env['ir.sequence'].next_by_code('purchase.order')
    )

    user_partner_id = fields.Many2one(
        'res.users', string='User Partner'
    )



