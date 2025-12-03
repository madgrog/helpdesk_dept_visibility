from odoo import models, fields, _


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.team"

    department_id = fields.Many2one('hr.department', string='Department', help="The Department of the Team.")