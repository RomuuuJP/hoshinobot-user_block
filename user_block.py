import os
import re

from datetime import timedelta
from hoshino.typing import CQEvent
from hoshino import Service, priv

#PRIV_TIP = f'群主={priv.OWNER} 群管={priv.ADMIN} 群员={priv.NORMAL} bot维护组={priv.SUPERUSER}'
sv = Service('user_block', manage_priv=priv.SUPERUSER, help_='.block@')

@sv.on_prefix('.block')
async def block(bot, ev: CQEvent):
    lig = re.search(r"(.block\d{1,4})",ev['raw_message']).group(0).replace(".block", "").replace(" ", "")
    if len(lig) > 3:
        block_time = 999
    else:
        block_time = int(lig)
    if ev.user_id not in bot.config.SUPERUSERS:
        return
    count = 0
    msg = ''
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            uid = int(m.data['qq'])
            priv.set_block_user(uid,timedelta(hours=block_time))
            if block_time == 0:
                msg = msg + f"已将{uid}解除拉黑\n"
            else:
                msg = msg + f"已将{uid}列入黑名单{block_time}小时\n"
            print(msg)
            count += 1
    if count:
        await bot.send(ev, msg)
