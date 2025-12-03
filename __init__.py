# -*- coding: utf-8 -*-

from . import models

def _restore_helpdesk(env):
    """
        This method restores original Enterprise Helpdesk
    """
    env.cr.execute("""UPDATE ir_rule SET domain_force = '[''|'',
                                            (''privacy_visibility'', ''!='', ''invited_internal''),
                                            (''message_partner_ids'', ''in'', [user.partner_id.id])
                                        ]'
                    WHERE name = 'Helpdesk User'""")
    env.cr.execute("""UPDATE ir_rule SET domain_force = '[''|'',
                                        ''|'',
                                            (''team_id.privacy_visibility'', ''!='', ''invited_internal''),
                                            (''team_id.message_partner_ids'', ''in'', [user.partner_id.id]),
                                            (''message_partner_ids'', ''in'', [user.partner_id.id]),
                                        ]'
                    WHERE name = 'Helpdesk Ticket User'""")
    print("Restored stock Helpdesk record rules!")