import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID, ALIVE

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
fffff = STRING14
fifth = STRING15


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""



que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@DARKV2SUPPORT"))
            await idk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await ydk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await wdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await hdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await sdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await adk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await bdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await cdk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await ddk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await edk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await vkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await kkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await lkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if fffff:
        session_name = str(fffff)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            await mkk(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@DARK5_SPAM_BOT"))
            await sid(functions.channels.JoinChannelRequest(channel="@DARK5_SPAMMER"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = yukki[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.eplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🇵 🇴 🇳 🇬 !\n`{ms}` 𝗺𝘀")

           

        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗮𝗹𝗶𝘃𝗲\n\nCommand:\n\n.alive <Username of User>\n\n.alive <send alive msg>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "LEGENDRY OF DARKXBOT"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "LEGENDRY OF DARKXBOT"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
     

    
        
text = """

😍😍😍 DARK BOT OP 😈😈😈😈
❤️❤️❤️❤️❤️ DARK OP ☠️☠️☠️☠️☠️"""

print(text)
print("")
print("CONGRATULATIONS! 🥳🥳🍾🎉..UR SPAM BOT IS READY..NOW ENJOY 🥳🥳.")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
