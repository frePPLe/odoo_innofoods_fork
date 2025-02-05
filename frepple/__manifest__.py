# -*- coding: utf-8 -*-
{
    "name": "frepple",
    "version": "15.0.0",
    "category": "Manufacturing",
    "summary": "Advanced planning and scheduling",
    "author": "frePPLe",
    "website": "https://frepple.com",
    "license": "AGPL-3",
    "description": "Connector to frePPLe - finite capacity planning and scheduling",
    "depends": ["product", "purchase", "sale", "resource", "mrp"],
    "external_dependencies": {"python": ["jwt"]},
    "data": [
        "views/frepple_data.xml",
        "views/res_config_settings_views.xml",
        "views/mrp_skill.xml",
        "views/mrp_workcenter_inherit.xml",
        "views/mrp_workcenter_skill.xml",
        "views/mrp_routing_workcenter_inherit.xml",
        "views/product_supplierinfo_inherit.xml",
        "security/frepple_security.xml",
        "security/ir.model.access.csv",
    ],
    "test": [],
    "installable": True,
    "auto_install": False,
    "assets": {
        "web.assets_backend": [
            "frepple/static/src/js/frepple.js",
        ],
    },
}
