# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 by frePPLe bv
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from odoo import models, fields


class RoutingWorkcenterInherit(models.Model):
    _inherit = "mrp.routing.workcenter"

    skill = fields.Many2one("mrp.skill", "Skill", required=False)
    search_mode = fields.Selection(
        [
            ("PRIORITY", "priority"),
            ("MINCOST", "minimum cost"),
            ("MINPENALTY", "minimum penalty"),
            ("MINCOSTPENALTY", "minimum cost plus penalty"),
        ],
        string="Search Mode",
        required=False,
        default="PRIORITY",
    )
    priority = fields.Integer("priority", default=1)
