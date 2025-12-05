import os, sys, glob, pytz,
from datetime import date, datetime 
from aiohttp import web
from web import web_server, check_expired_premium
from web.server import Webavbot
from utils import temp, ping_server
from asyncio, logging, importlib
from pathlib import Path
from pyrogram import idle

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

logging.basicConfig(
    level= web.server.clients import initialize_clients

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

ppath = "plugins/*.py"
files = glob.glob(pplogging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(ath)
Webavbot.start()
loop = asyncio.get_event_loop()

async def startmessage)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await Webavbot.get_me()
    await initialize_clients()
    for name in files:
        ("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
 
from info import *
from typing import Union, Optional, AsyncGenerator
from Script import scriptwith open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_ 
from datetime import date, datetime 
from aiohttp import web
from web import web_server,name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load check_expired_premium
from web.server import Webavbot
from utils import temp, ping_server
 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(from web.server.clients import initialize_clients

#Dont Remove My Credit @AV_BOTz_UPDATE load)
            sys.modules["plugins." + plugin_name] = load
            print("Imported =>
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

ppath = "plugins/*.py"
files = glob.glob(ppath)
Webavbot.start()
loop = asyncio.get_event_loop()

async def " + plugin_name)

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info =_SUPPORT_GROUP
    
    if ON_HEROKU:
        asyncio.create_task( await Webavbot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_ping_server())
    me = await Webavbot.get_me()
    temp.BOT = Webname = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            specavbot
    temp.ME = me.id
    temp.U_NAME = me.username
     = importlib.util.spec_from_file_location(import_path, plugins_dir)
            temp.B_NAME = me.first_name
    tz = pytz.timezone('Africa/Mogadload = importlib.util.module_from_spec(spec)
            spec.loader.exec_moduleishu')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime(load)
            sys.modules["plugins." + plugin_name] = load
            print("Imported("%H:%M:%S %p")
    Webavbot.loop.create_task(check_expired => " + plugin_name)

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @_premium(Webavbot))
    
    # --- FIX START: Waxaan halkan ku darnay 'try/exceptAV_SUPPORT_GROUP
    
    if ON_HEROKU:
        asyncio.create_task' si uusan bot-ka u istaagin haddii fariinta la diri waayo ---
    try:
(ping_server())
    me = await Webavbot.get_me()
    temp.BOT = Webavbot
    temp.ME = me.id
    temp.U_NAME = me.username
        await Webavbot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART    temp.B_NAME = me.first_name
    tz = pytz.timezone('Africa/M_TXT.format(today, time))
    except Exception:
        pass

    try:
        awaitogadishu')
    today = date.today()
    now = datetime.now(tz)
    time Webavbot.send_message(chat_id=ADMINS[0] ,text='<b>ʙᴏᴛ = now.strftime("%H:%M:%S %p")
    Webavbot.loop.create_task ʀᴇsᴛᴀʀᴛᴇᴅ !!</b>')
    except Exception:
        pass

    try(check_expired_premium(Webavbot))
    
    # -------------------------------------------------------------
    #:
        await Webavbot.send_message(chat_id=SUPPORT_GROUP, text=f" Qeybtan ayaan hagaajiyay: Waxaan galiyay try/except si uusan u cilado<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>")
    except Exceptionobin
    try:
        await Webavbot.send_message(chat_id=LOG_CHANNEL,:
        pass
    # --- FIX END ---

    app = web.AppRunner(await web_server text=script.RESTART_TXT.format(today, time))
        await Webavbot.send_message(chat_id=ADMINS[0] ,text='<b>ʙᴏᴛ ʀᴇsᴛᴀ())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

ʀᴛᴇᴅ !!</b>')
        await Webavbot.send_message(chat_id=SUPPORT_#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNERGROUP, text=f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    </b>")
    except Exception as e:
        print(f"Failed to send restart message: {e}")
        # Halkan wuu dhaafayaa haddii fariinta la diido, bot-kuna wexcept KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
