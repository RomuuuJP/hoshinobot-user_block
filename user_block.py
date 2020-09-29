import os
import re

from datetime import timedelta
from hoshino.typing import CQEvent
from hoshino import Service, priv

#PRIV_TIP = f'群主={priv.OWNER} 群管={priv.ADMIN} 群员={priv.NORMAL} bot维护组={priv.SUPERUSER}'
sv = Service('user_block', manage_priv=priv.SUPERUSER, help_='.block1@123|.blockuid1@123456|.blockgid1@123456')

#最长拉黑时间
MAX_TIME = 999

@sv.on_prefix('.block')
async def block(bot, ev: CQEvent):
    raw_msg = ev['raw_message'].replace(" ", "")
    lig = re.search(r"(.block\d{1,4})",raw_msg)
    if lig:
        lig = lig.group(0).replace(".block", "").replace(" ", "")
    btype = 0
    if not lig:
        lig = re.search(r"(.blockuid\d{1,4})",raw_msg)
        if lig:
            lig = lig.group(0).replace(".blockuid", "").replace(" ", "")
        btype = 1
        if not lig:
            lig = re.search(r"(.blockgid\d{1,4})",raw_msg)
            if lig:
                lig = lig.group(0).replace(".blockgid", "").replace(" ", "")
            btype = 2
    if not lig:
        await bot.send(ev, f"指令不正确{lig}")
        return

    if ev.user_id not in bot.config.SUPERUSERS:
        return

    if int(lig) > MAX_TIME:
        block_time = MAX_TIME
    else:
        block_time = int(lig)

    print(block_time)
    print(btype)
    count = 0
    msg = ''
    #拉黑@用户
    if btype == 0:
        for m in ev.message:
            if m.type == 'at' and m.data['qq'] != 'all':
                uid = int(m.data['qq'])
                priv.set_block_user(uid,timedelta(hours=block_time))
                if block_time == 0:
                    msg = msg + f"已将用户{uid}解除拉黑\n"
                else:
                    msg = msg + f"已将用户{uid}列入黑名单{block_time}小时\n"
                count += 1
    #拉黑qq号
    elif btype == 1:
        block_msg = raw_msg.replace(".blockuid"+lig, "")
        block_ulst = block_msg.split("@")
        print (block_ulst)
        for buid in block_ulst:
            print('buid:'+buid)
            if not buid:
                continue
            uid = int(buid)
            priv.set_block_user(uid,timedelta(hours=block_time))
            if block_time == 0:
                msg = msg + f"已将用户{uid}解除拉黑\n"
            else:
                msg = msg + f"已将用户{uid}列入黑名单{block_time}小时\n"
            count += 1
    #拉黑群号
    elif btype == 2:
        block_msg = raw_msg.replace(".blockgid"+lig, "")
        block_glst = block_msg.split("@")
        print (block_glst)
        for bgid in block_glst:
            if not bgid:
                continue
            gid = int(bgid)
            priv.set_block_group(gid,timedelta(hours=block_time))
            if block_time == 0:
                msg = msg + f"已将群{gid}解除拉黑\n"
            else:
                msg = msg + f"已将群{gid}列入黑名单{block_time}小时\n"
            count += 1
    if count:
        await bot.send(ev, msg)
        
