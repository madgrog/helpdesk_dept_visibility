# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Department Visibility",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose
    """,
    "author": "Luigi Lamorte",
    "website": "https://github.com/madgrog/helpdesk_dept_visibility",
    "category": "Services/Helpdesk",
    'version': '0.1',
    'depends': ['helpdesk', 'hr'],
    'data': [
        'security/helpdesk_security.xml',
        'views/helpdesk_team_views.xml',
    ],
    "uninstall_hook": "_restore_helpdesk",
}

