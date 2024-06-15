from odoo import fields, models

class MyModel(models.Model):
    _name = "mo.model"

    name = fields.Char(string='name')
    amount = fields.Float(string='amount')