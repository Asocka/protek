# -*- coding: utf-8 -*- 
import linepy
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl


riant = LINE('EytAFQoYDUSwvPtR58G6.XLWvdVf+xVnxyEg1KVcnPG.MwkbwbZLOyq182bnbbWKQ54xjtyokcGn6QlWjMgkjtQ=')
riant.log("Auth Token : " + str(riant.authToken))
channelToken = riant.getChannelResult()
riant.log("Channel Token : " + str(channelToken))

dr1 = LINE('EyW6RFXDm0AxGy0gxIj4.EGHvOVoKk2zQr/MhO/5HLa.dtFxxD9TDiBf+yd8Jh/n75X4SLE83QNSme/KULYfteI=')
dr1.log("Auth Token : " + str(dr1.authToken))
channelToken = dr1.getChannelResult()
dr1.log("Channel Token : " + str(channelToken))

dr2 = LINE('Ex7sIYpZ0RVzau5FDkBa.cm937zz1BxB3ajFrH3wQ/G.+xUgM3nQ9Uu6rpMkm9kEfgSfnaQFVLlojy4z00LCzlI=')
dr2.log("Auth Token : " + str(dr2.authToken))
channelToken = dr2.getChannelResult()
dr2.log("Channel Token : " + str(channelToken))

dr3 = LINE('EyTqjwM3lfQFcfcHiFc2.NJbfHG8RbOI8hLonI3plaG.97W6fezxvNkmBBYeNkxNRhwJFcKWcf6/7Q8BTW/Er+w=')
dr3.log("Auth Token : " + str(dr3.authToken))
channelToken = dr3.getChannelResult()
dr3.log("Channel Token : " + str(channelToken))

dr4 = LINE('Ey81S3dNyAdFft88fSs7.GjnWi37jqx5If3bluZ0KHW.hhGcQWgAPS6jdfRA6YXSid4xtqUUkHRPIfotCeLwDzg=')
dr4.log("Auth Token : " + str(dr4.authToken))
channelToken = dr4.getChannelResult()
dr4.log("Channel Token : " + str(channelToken))

dr5 = LINE('Exe4hdYWg8EAkh26I5G0.Off/7pOSESVtRu08aFZXOa.xwoqUqCJfHXFUU7K9IlUyB62H3uuaKWClhXVmazlfoE=')
dr5.log("Auth Token : " + str(dr5.authToken))
channelToken = dr5.getChannelResult()
dr5.log("Channel Token : " + str(channelToken))

dr6 = LINE('EyCjAFIH9yvweLp3X3c9.sPs0YZatV7IrzJC/dlVoQq.IisDqjck4tkghO5LeJM0gwQmFH0r2IvcodT7huSscIw=')
dr6.log("Auth Token : " + str(dr6.authToken))
channelToken = dr6.getChannelResult()
dr6.log("Channel Token : " + str(channelToken))

dr7 = LINE('Eyf2MuitGCk3PeBXPUke.wGL8Y6Cvm9wdpDuLWCS1hG.ts4GZagz1CG8AtWoSncYFXCJEWw4aygDitHIcQIUpx0=')
dr7.log("Auth Token : " + str(dr7.authToken))
channelToken = dr7.getChannelResult()
dr7.log("Channel Token : " + str(channelToken))

dr8 = LINE('EySv6Q1lfSjQyl7hfH41.vq0P1OQNQwBCA6u08aS2uq.ZWKr0jpGgShNxltXRjWPf73ZNQWEng2L+8TP1cChROY=')
dr8.log("Auth Token : " + str(dr8.authToken))
channelToken = dr8.getChannelResult()
dr8.log("Channel Token : " + str(channelToken))

dr9 = LINE('ExKatkF6Pfot9CFBBtw7.iKnTPOBAVcWCu62NNDt9TW.LmwHSvVkgMulkryW2RSkUx4PSE0U1z23MkWpHFAgXhA=')
dr9.log("Auth Token : " + str(dr9.authToken))
channelToken = dr9.getChannelResult()
dr9.log("Channel Token : " + str(channelToken))

dr10 = LINE('ExY0Iy5Qpw2wBtxQiSzc.id6jviSE5wifDgdNI5VGVa./KozMEWshvGKl8W2I8Cb3nE/end1ztRjZiIWwY7HXzI=')
dr10.log("Auth Token : " + str(dr10.authToken))
channelToken = dr10.getChannelResult()
dr10.log("Channel Token : " + str(channelToken))

dr11 = LINE('ExqNzhzV1XTNVzqtXIC6.YLgK5kBRjOO/2ZExCubWTG.asyxIM8eer8mWQEEJ3ysod40U1Mbh4p4j3Y9Lrl/CtA=')#kicker ini yang jaga di luar bro
dr11.log("Auth Token : " + str(dr11.authToken))
channelToken = dr11.getChannelResult()
dr11.log("Channel Token : " + str(channelToken))

dr12 = LINE('ExfOn1VYHB8Yi9uk9fU9.WLFAUrcCAcQUDW9YOnx9sq.PEOegczwjivIbajR/9pYuFWAvtjZDdZG6KzOmzrrUVU=')#kicker ini yang jaga di luar bro
dr12.log("Auth Token : " + str(dr12.authToken))
channelToken = dr12.getChannelResult()
dr12.log("Channel Token : " + str(channelToken))

satpam = LINE('ExSCs4iTeJidXWasaUN3.EzMh7ZcBnm81B7Mb4xdrSW.cl1kB0NtCUEYigQ9A1R+rr82HBVfRMml40gtAE8BOsM=')#AKUN INI WAJIB ADA DI ROOM
satpam.log("Auth Token : " + str(satpam.authToken))
channelToken = satpam.getChannelResult()
satpam.log("Channel Token : " + str(channelToken))




helpMessage ="""
━━ೋ•🚱 •ೋ━━━┓
      DR-BOT    
┗━━ೋ• 🚱•ೋ━━━

🚯 🚳 🚱 🔞 📵 🚭
 🔜
 🔜  ME
 🔜  MY MID
 🔜  BERSIHKAN
 🔜  CEKBOT
 🔜  RIANT OUT
 🔜  RIANT BYE
 🔜  MASUK
 🔜  SP
 🔜  BANLIST
 🔜  GINFO
 🔜  SA
 🔜  BELAI
 🔜  TUKIMIN
 🔜  DR1 IN
 🔜  DR2 IN
 🔜  DR3 IN
 🔜  DR4 IN
 🔜  HELPBOT
 🔜  UNDANG
 🔜  CLEANSE
 🔜  BUKA QR
 🔜  TUTUP QR
 🔜  RIANT BYE
 ━━ೋ•🚱 •ೋ━━━┓
   DR-BOT    
┗━━ೋ• 🚱•ೋ━━━ 
 🔜  COMMAND PROTECT🔜 
 🔜  MODE ON/OFF
 🔜  OFF/ON JOINPRO
 🔜  OFF/ON CANCELPRO
 🔜  
╚══════════════╝
━━ೋ•🚱 •ೋ━━━┓
PROTECT ALAYBOT-DR    
┗━━ೋ• 🚱•ೋ━━━
"""
oepoll = OEPoll(riant)
KAC=[riant,dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8,dr9,dr10]
DEF=[satpam]
mid = riant.getProfile().mid
Amid = dr1.getProfile().mid
Bmid = dr2.getProfile().mid
Cmid = dr3.getProfile().mid
Dmid = dr4.getProfile().mid
Emid = dr5.getProfile().mid
Fmid = dr6.getProfile().mid
Gmid = dr7.getProfile().mid
Hmid = dr8.getProfile().mid
Imid = dr9.getProfile().mid
Jmid = dr10.getProfile().mid
Kmid = satpam.getProfile().mid


responsename = riant.getProfile().displayName
responsename1 = dr1.getProfile().displayName
responsename2 = dr2.getProfile().displayName
responsename3 = dr3.getProfile().displayName
responsename4 = dr4.getProfile().displayName
responsename5 = dr5.getProfile().displayName
responsename6 = dr6.getProfile().displayName
responsename7 = dr7.getProfile().displayName
responsename8 = dr8.getProfile().displayName
responsename9 = dr9.getProfile().displayName
responsename10 = dr10.getProfile().displayName


Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,"u43e02f888bfa5dad92a07b94a454b76f","u2eee52d1c65aa29c09a05e1328183f60","ue88d5265192c3888bdc1750c9d27b58c"]
admin=["ua7a65295f36751c9ff07f432f22073c9","uae65bf02566258685a194fc0bbb9b56d","u03858028f62170f7c412f503c35f18c1","u43e02f888bfa5dad92a07b94a454b76f","u2eee52d1c65aa29c09a05e1328183f60","ue88d5265192c3888bdc1750c9d27b58c"]

Owner=["ua7a65295f36751c9ff07f432f22073c9","uae65bf02566258685a194fc0bbb9b56d","u03858028f62170f7c412f503c35f18c1","u43e02f888bfa5dad92a07b94a454b76f","u2eee52d1c65aa29c09a05e1328183f60","ue88d5265192c3888bdc1750c9d27b58c"]
creator=["u5b5d2c21900195bbca7e590da3ad4e1e"]
wait = {
    'contact':False,
    'joingc':"😂",
    'leftgc':" 😂😂😂",
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"TERIMA KASIH TELANAMBAHKAN SAYA \nSALAM PERSAHABATAN \nᴄʀᴇᴀᴛᴏʀ line.me/ti/p/JYrhtHx832",
    "lang":"JP",
    "comment":"TERIMA KASIH TELANAMBAHKAN SAYA \nSALAM PERSAHABATAN \nᴄʀᴇᴀᴛᴏʀ line.me/ti/p/JYrhtHx832",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "wcOn":False,
    "leftOn":True,
    "cName":"BOT DR ",
    "cName2":"BOT DR ",
    "cName3":"BOT DR ",
    "cName4":"BOT DR ",
    "cName5":"BOT DR ",
    "cName6":"BOT DR ",
    "cName7":"BOT DR ",
    "cName8":"BOT DR ",
    "cName9":"BOT DR ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":True,
    "ProtectJoin":True,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "spamer":{},
    "CloseQR":True,
    "Protectguest":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True,
    "invite":{},
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = riant.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
        
def sendMentionV10(to, text,name, url, iconlink):
    riant.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        riant.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                riant.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    riant.sendText(op.param1,str(wait["message"]))

	#--------Qr Kick Start--------------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	#X = dna5.getGroup(op.param1)
                 	#X.preventedJoinByTicket = False
                 	#dna5.updateGroup(X)
                 	Ticket = satpam.reissueGroupTicket(op.param1)
                 	dr12.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dr12.kickoutFromGroup(op.param1,[op.param2])
                 	dr12.leaveGroup(op.param1)
                 	X = random.choice(KAC).getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	random.choice(KAC).updateGroup(X)
        if op.type == 11:
            if not op.param2 in Bots:
                if wait["CloseQR"] == True:
                  try:
                      kpist=[riant,dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8,dr9,dr10]
                      puck=random.choice(kpist)
                      G = puck.getGroup(op.param1)
                      G.preventJoinByTicket = True
                      puck.updateGroup(G)
                  except Exception as e:
                      print(e)
        #----------------------#
        if op.type == 17:
            if wait["ProtectJoin"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	X = dr8.getGroup(op.param1)
                 	X.preventedJoinByTicket = False
                 	dr8.updateGroup(X)
                 	Ticket = satpam.reissueGroupTicket(op.param1)
                 	dr11.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dr11.kickoutFromGroup(op.param1,[op.param2])
                 	dr11.leaveGroup(op.param1)
                 	X = dr1.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	dr1.updateGroup(X)
        if op.type == 13:
            G = dr1.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:
                    klist=[dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8,dr9,dr10]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.sendText(op.param1,"jagoan nih si jablay ...")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        kicker.sendMessage(c)
	#-----------------------#
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        riant.acceptGroupInvitation(op.param1)
                        ginfo = riant.getGroup(op.param1)
                    else:
                        riant.acceptGroupInvitation(op.param1)
                        ginfo = riant.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr1.acceptGroupInvitation(op.param1)
                        ginfo = dr1.getGroup(op.param1)
                    else:
                        dr1.acceptGroupInvitation(op.param1)
                        ginfo = dr1.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr2.acceptGroupInvitation(op.param1)
                        ginfo = dr2.getGroup(op.param1)
                    else:
                        dr2.acceptGroupInvitation(op.param1)
                        ginfo = dr2.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr3.acceptGroupInvitation(op.param1)
                        ginfo = dr3.getGroup(op.param1)
                    else:
                        dr3.acceptGroupInvitation(op.param1)
                        ginfo = dr3.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr4.acceptGroupInvitation(op.param1)
                        ginfo = dr4.getGroup(op.param1)
                    else:
                        dr4.acceptGroupInvitation(op.param1)
                        ginfo = dr4.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr5.acceptGroupInvitation(op.param1)
                        ginfo = dr5.getGroup(op.param1)
                    else:
                        dr5.acceptGroupInvitation(op.param1)
                        ginfo = dr5.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr6.acceptGroupInvitation(op.param1)
                        ginfo = dr6.getGroup(op.param1)
                    else:
                        dr6.acceptGroupInvitation(op.param1)
                        ginfo = dr6.getGroup(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr7.acceptGroupInvitation(op.param1)
                        ginfo = dr7.getGroup(op.param1)
                    else:
                        dr7.acceptGroupInvitation(op.param1)
                        ginfo = dr7.getGroup(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr8.acceptGroupInvitation(op.param1)
                        ginfo = dr8.getGroup(op.param1)
                    else:
                        dr8.acceptGroupInvitation(op.param1)
                        ginfo = dr8.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr9.acceptGroupInvitation(op.param1)
                        ginfo = dr9.getGroup(op.param1)
                    else:
                        dr9.acceptGroupInvitation(op.param1)
                        ginfo = dr9.getGroup(op.param1)
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dr10.acceptGroupInvitation(op.param1)
                        ginfo = dr10.getGroup(op.param1)
                    else:
                        dr10.acceptGroupInvitation(op.param1)
                        ginfo = dr10.getGroup(op.param1)
            if Kmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        satpam.acceptGroupInvitation(op.param1)
                        ginfo = satpam.getGroup(op.param1)
                    else:
                        satpam.acceptGroupInvitation(op.param1)
                        ginfo = satpam.getGroup(op.param1)

        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("KICKER AKTIF")
                 else:
                    pass

        if op.type == 19:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                  try:
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      try:
                          random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                          random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      except:
                          print ("MEMBER KICK")
        
	#--------Invite User Kick Start-----------#
        if op.type == 32:
            if wait["Protectcancel"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                    try:
                        group = riant.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            riant.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = dr1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                dr1.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = dr2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    dr2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = dr3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        dr3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = dr4.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            dr4.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = dr5.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                dr5.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = dr6.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    dr6.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                try:
                                                    group = dr7.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        dr7.cancelGroupInvitation(op.param1,[_mid])
                                                except:
                                                    try:
                                                        group = dr8.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            dr8.cancelGroupInvitation(op.param1,[_mid])
                                                    except:
                                                        try:
                                                            group = dr9.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                dr9.cancelGroupInvitation(op.param1,[_mid])
                                                        except:
                                                            try:
                                                                group = dr10.getGroup(op.param1)
                                                                gMembMids = [contact.mid for contact in group.invitee]
                                                                for _mid in gMembMids:
                                                                    dr10.cancelGroupInvitation(op.param1,[_mid])
                                                            except:
                                                                pass
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            dr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                dr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    dr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        dr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            dr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                dr6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    dr7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        dr8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            dr9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                dr10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    riant.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                pass
                return
        
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr5.kickoutFromGroup(op.param1,[op.param2])
                        dr1.findAndAddContactsByMid(op.param3)
                        dr1.inviteIntoGroup(op.param1,[op.param3])
                        riant.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr4.kickoutFromGroup(op.param1,[op.param2])
                            dr2.findAndAddContactsByMid(op.param3)
                            dr2.inviteIntoGroup(op.param1,[op.param3])
                            riant.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr3.kickoutFromGroup(op.param1,[op.param2])
                                dr5.findAndAddContactsByMid(op.param3)
                                dr5.inviteIntoGroup(op.param1,[op.param3])
                                riant.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr1.kickoutFromGroup(op.param1,[op.param2])
                                    dr2.findAndAddContactsByMid(op.param3)
                                    dr2.inviteIntoGroup(op.param1,[op.param3])
                                    riant.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return         
              
        if op.type == 19:
            if Amid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr10.kickoutFromGroup(op.param1,[op.param2])
                        dr10.findAndAddContactsByMid(op.param3)
                        dr10.inviteIntoGroup(op.param1,[op.param3])
                        dr1.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr9.kickoutFromGroup(op.param1,[op.param2])
                            dr9.findAndAddContactsByMid(op.param3)
                            dr9.inviteIntoGroup(op.param1,[op.param3])
                            dr1.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr8.kickoutFromGroup(op.param1,[op.param2])
                                dr8.findAndAddContactsByMid(op.param3)
                                dr8.inviteIntoGroup(op.param1,[op.param3])
                                dr1.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr7.kickoutFromGroup(op.param1,[op.param2])
                                    dr7.findAndAddContactsByMid(op.param3)
                                    dr7.inviteIntoGroup(op.param1,[op.param3])
                                    dr7.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return         
              
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr9.kickoutFromGroup(op.param1,[op.param2])
                        dr9.findAndAddContactsByMid(op.param3)
                        dr9.inviteIntoGroup(op.param1,[op.param3])
                        dr2.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr8.kickoutFromGroup(op.param1,[op.param2])
                            dr8.findAndAddContactsByMid(op.param3)
                            dr8.inviteIntoGroup(op.param1,[op.param3])
                            dr2.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr7.kickoutFromGroup(op.param1,[op.param2])
                                dr7.findAndAddContactsByMid(op.param3)
                                dr7.inviteIntoGroup(op.param1,[op.param3])
                                dr2.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr6.kickoutFromGroup(op.param1,[op.param2])
                                    dr6.findAndAddContactsByMid(op.param3)
                                    dr6.inviteIntoGroup(op.param1,[op.param3])
                                    dr2.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr5.kickoutFromGroup(op.param1,[op.param2])
                                        dr5.findAndAddContactsByMid(op.param3)
                                        dr5.inviteIntoGroup(op.param1,[op.param3])
                                        dr2.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return         
              
        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr8.kickoutFromGroup(op.param1,[op.param2])
                        dr8.findAndAddContactsByMid(op.param3)
                        dr8.inviteIntoGroup(op.param1,[op.param3])
                        dr8.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr7.kickoutFromGroup(op.param1,[op.param2])
                            dr7.findAndAddContactsByMid(op.param3)
                            dr7.inviteIntoGroup(op.param1,[op.param3])
                            dr3.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr6.kickoutFromGroup(op.param1,[op.param2])
                                dr6.findAndAddContactsByMid(op.param3)
                                dr6.inviteIntoGroup(op.param1,[op.param3])
                                dr3.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr5.kickoutFromGroup(op.param1,[op.param2])
                                    dr5.findAndAddContactsByMid(op.param3)
                                    dr5.inviteIntoGroup(op.param1,[op.param3])
                                    dr3.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr4.kickoutFromGroup(op.param1,[op.param2])
                                        dr4.findAndAddContactsByMid(op.param3)
                                        dr4.inviteIntoGroup(op.param1,[op.param3])
                                        dr3.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return

        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr7.kickoutFromGroup(op.param1,[op.param2])
                        dr7.findAndAddContactsByMid(op.param3)
                        dr7.inviteIntoGroup(op.param1,[op.param3])
                        dr4.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr6.kickoutFromGroup(op.param1,[op.param2])
                            dr6.findAndAddContactsByMid(op.param3)
                            dr6.inviteIntoGroup(op.param1,[op.param3])
                            dr4.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr5.kickoutFromGroup(op.param1,[op.param2])
                                dr5.findAndAddContactsByMid(op.param3)
                                dr5.inviteIntoGroup(op.param1,[op.param3])
                                dr4.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr3.kickoutFromGroup(op.param1,[op.param2])
                                    dr3.findAndAddContactsByMid(op.param3)
                                    dr3.inviteIntoGroup(op.param1,[op.param3])
                                    dr4.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr2.kickoutFromGroup(op.param1,[op.param2])
                                        dr2.findAndAddContactsByMid(op.param3)
                                        dr2.inviteIntoGroup(op.param1,[op.param3])
                                        dr4.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return
        
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr6.kickoutFromGroup(op.param1,[op.param2])
                        dr6.findAndAddContactsByMid(op.param3)
                        dr6.inviteIntoGroup(op.param1,[op.param3])
                        dr5.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr4.kickoutFromGroup(op.param1,[op.param2])
                            dr4.findAndAddContactsByMid(op.param3)
                            dr4.inviteIntoGroup(op.param1,[op.param3])
                            dr5.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr3.kickoutFromGroup(op.param1,[op.param2])
                                dr3.findAndAddContactsByMid(op.param3)
                                dr3.inviteIntoGroup(op.param1,[op.param3])
                                dr5.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr2.kickoutFromGroup(op.param1,[op.param2])
                                    dr2.findAndAddContactsByMid(op.param3)
                                    dr2.inviteIntoGroup(op.param1,[op.param3])
                                    dr5.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr1.kickoutFromGroup(op.param1,[op.param2])
                                        dr1.findAndAddContactsByMid(op.param3)
                                        dr1.inviteIntoGroup(op.param1,[op.param3])
                                        dr5.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return

        if op.type == 19:
            if Fmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr5.kickoutFromGroup(op.param1,[op.param2])
                        dr5.findAndAddContactsByMid(op.param3)
                        dr5.inviteIntoGroup(op.param1,[op.param3])
                        dr6.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr4.kickoutFromGroup(op.param1,[op.param2])
                            dr4.findAndAddContactsByMid(op.param3)
                            dr4.inviteIntoGroup(op.param1,[op.param3])
                            dr6.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr3.kickoutFromGroup(op.param1,[op.param2])
                                dr3.findAndAddContactsByMid(op.param3)
                                dr3.inviteIntoGroup(op.param1,[op.param3])
                                dr6.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr2.kickoutFromGroup(op.param1,[op.param2])
                                    dr2.findAndAddContactsByMid(op.param3)
                                    dr2.inviteIntoGroup(op.param1,[op.param3])
                                    dr6.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return         
              
        if op.type == 19:
            if Gmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr4.kickoutFromGroup(op.param1,[op.param2])
                        dr4.findAndAddContactsByMid(op.param3)
                        dr4.inviteIntoGroup(op.param1,[op.param3])
                        dr7.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr3.kickoutFromGroup(op.param1,[op.param2])
                            dr3.findAndAddContactsByMid(op.param3)
                            dr3.inviteIntoGroup(op.param1,[op.param3])
                            dr7.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr2.kickoutFromGroup(op.param1,[op.param2])
                                dr2.findAndAddContactsByMid(op.param3)
                                dr2.inviteIntoGroup(op.param1,[op.param3])
                                dr7.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr1.kickoutFromGroup(op.param1,[op.param2])
                                    dr1.findAndAddContactsByMid(op.param3)
                                    dr1.inviteIntoGroup(op.param1,[op.param3])
                                    dr7.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).findAndAddContactsByMid(op.param3)
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        dr7.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return         
              
        if op.type == 19:
            if Hmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr3.kickoutFromGroup(op.param1,[op.param2])
                        dr3.findAndAddContactsByMid(op.param3)
                        dr3.inviteIntoGroup(op.param1,[op.param3])
                        dr8.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr2.kickoutFromGroup(op.param1,[op.param2])
                            dr2.findAndAddContactsByMid(op.param3)
                            dr2.inviteIntoGroup(op.param1,[op.param3])
                            dr8.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr1.kickoutFromGroup(op.param1,[op.param2])
                                dr1.findAndAddContactsByMid(op.param3)
                                dr1.inviteIntoGroup(op.param1,[op.param3])
                                dr8.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr10.kickoutFromGroup(op.param1,[op.param2])
                                    dr10.findAndAddContactsByMid(op.param3)
                                    dr10.inviteIntoGroup(op.param1,[op.param3])
                                    dr8.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr9.kickoutFromGroup(op.param1,[op.param2])
                                        dr9.findAndAddContactsByMid(op.param3)
                                        dr9.inviteIntoGroup(op.param1,[op.param3])
                                        dr8.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return

        if op.type == 19:
            if Imid in op.param3:
                if op.param2 not in Bots:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).findAndAddContactsByMid(op.param3)
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        dr9.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            riant.kickoutFromGroup(op.param1,[op.param2])
                            riant.findAndAddContactsByMid(op.param3)
                            riant.inviteIntoGroup(op.param1,[op.param3])
                            dr9.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr8.kickoutFromGroup(op.param1,[op.param2])
                                dr8.findAndAddContactsByMid(op.param3)
                                dr8.inviteIntoGroup(op.param1,[op.param3])
                                dr9.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr7.kickoutFromGroup(op.param1,[op.param2])
                                    dr7.findAndAddContactsByMid(op.param3)
                                    dr7.inviteIntoGroup(op.param1,[op.param3])
                                    dr9.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr6.kickoutFromGroup(op.param1,[op.param2])
                                        dr6.findAndAddContactsByMid(op.param3)
                                        dr6.inviteIntoGroup(op.param1,[op.param3])
                                        dr9.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return
        
        if op.type == 19:
            if Jmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        riant.kickoutFromGroup(op.param1,[op.param2])
                        riant.findAndAddContactsByMid(op.param3)
                        riant.inviteIntoGroup(op.param1,[op.param3])
                        dr10.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr7.kickoutFromGroup(op.param1,[op.param2])
                            dr7.findAndAddContactsByMid(op.param3)
                            dr7.inviteIntoGroup(op.param1,[op.param3])
                            dr10.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr6.kickoutFromGroup(op.param1,[op.param2])
                                dr6.findAndAddContactsByMid(op.param3)
                                dr6.inviteIntoGroup(op.param1,[op.param3])
                                dr10.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dr5.kickoutFromGroup(op.param1,[op.param2])
                                    dr5.findAndAddContactsByMid(op.param3)
                                    dr5.inviteIntoGroup(op.param1,[op.param3])
                                    dr10.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dr4.kickoutFromGroup(op.param1,[op.param2])
                                        dr4.findAndAddContactsByMid(op.param3)
                                        dr4.inviteIntoGroup(op.param1,[op.param3])
                                        dr10.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return

        if op.type == 19:
            if Kmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dr8.kickoutFromGroup(op.param1,[op.param2])
                        dr8.findAndAddContactsByMid(op.param3)
                        dr8.inviteIntoGroup(op.param1,[op.param3])
                        random.choice(DEF).acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dr9.kickoutFromGroup(op.param1,[op.param2])
                            dr9.findAndAddContactsByMid(op.param3)
                            dr9.inviteIntoGroup(op.param1,[op.param3])
                            random.choice(DEF).acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dr10.kickoutFromGroup(op.param1,[op.param2])
                                dr10.findAndAddContactsByMid(op.param3)
                                dr10.inviteIntoGroup(op.param1,[op.param3])
                                random.choice(DEF).acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    riant.kickoutFromGroup(op.param1,[op.param2])
                                    riant.findAndAddContactsByMid(op.param3)
                                    riant.inviteIntoGroup(op.param1,[op.param3])
                                    random.choice(DEF).acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).findAndAddContactsByMid(op.param3)
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(DEF).acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return
       
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr1.inviteIntoGroup(op.param1,[op.param3])
                        riant.acceptGroupInvitation(op.param1)
                        dr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr2.inviteIntoGroup(op.param1,[op.param3])
                            riant.acceptGroupInvitation(op.param1)
                            dr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr3.inviteIntoGroup(op.param1,[op.param3])
                                riant.acceptGroupInvitation(op.param1)
                                dr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dr4.inviteIntoGroup(op.param1,[op.param3])
                                    riant.acceptGroupInvitation(op.param1)
                                    dr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dr5.inviteIntoGroup(op.param1,[op.param3])
                                        riant.acceptGroupInvitation(op.param1)
                                        dr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dr1.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dr1.updateGroup(G)
                                            Ticket = dr1.reissueGroupTicket(op.param1)
                                            riant.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dr1.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dr1.updateGroup(G)
                                            Ticket = dr1.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dr1.inviteIntoGroup(op.param1,[op.param3])
                                                riant.acceptGroupInvitation(op.param1)
                                                dr1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dr2.inviteIntoGroup(op.param1,[op.param3])
                                                    riant.acceptGroupInvitation(op.param1)
                                                    dr2.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr2.inviteIntoGroup(op.param1,[op.param3])
                        dr1.acceptGroupInvitation(op.param1)
                        dr2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr3.inviteIntoGroup(op.param1,[op.param3])
                            dr1.acceptGroupInvitation(op.param1)
                            dr3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr4.inviteIntoGroup(op.param1,[op.param3])
                                dr1.acceptGroupInvitation(op.param1)
                                dr4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dr5.inviteIntoGroup(op.param1,[op.param3])
                                    dr1.acceptGroupInvitation(op.param1)
                                    dr5.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        riant.inviteIntoGroup(op.param1,[op.param3])
                                        dr1.acceptGroupInvitation(op.param1)
                                        riant.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dr2.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dr2.updateGroup(G)
                                            Ticket = dr2.reissueGroupTicket(op.param1)
                                            riant.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dr2.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dr2.updateGroup(G)
                                            Ticket = dr2.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dr2.inviteIntoGroup(op.param1,[op.param3])
                                                dr1.acceptGroupInvitation(op.param1)
                                                dr2.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dr3.inviteIntoGroup(op.param1,[op.param3])
                                                    dr1.acceptGroupInvitation(op.param1)
                                                    dr3.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr3.inviteIntoGroup(op.param1,[op.param3])
                        dr2.acceptGroupInvitation(op.param1)
                        dr3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr4.inviteIntoGroup(op.param1,[op.param3])
                            dr2.acceptGroupInvitation(op.param1)
                            dr4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr5.inviteIntoGroup(op.param1,[op.param3])
                                dr2.acceptGroupInvitation(op.param1)
                                dr5.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    riant.inviteIntoGroup(op.param1,[op.param3])
                                    dr2.acceptGroupInvitation(op.param1)
                                    riant.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dr1.inviteIntoGroup(op.param1,[op.param3])
                                        dr2.acceptGroupInvitation(op.param1)
                                        dr1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dr3.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dr3.updateGroup(G)
                                            Ticket = dr3.reissueGroupTicket(op.param1)
                                            riant.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dr3.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dr3.updateGroup(G)
                                            Ticket = dr3.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                                dr2.acceptGroupInvitation(op.param1)
                                                dr3.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dr4.inviteIntoGroup(op.param1,[op.param3])
                                                    dr2.acceptGroupInvitation(op.param1)
                                                    dr4.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr4.inviteIntoGroup(op.param1,[op.param3])
                        dr3.acceptGroupInvitation(op.param1)
                        dr4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr5.inviteIntoGroup(op.param1,[op.param3])
                            dr3.acceptGroupInvitation(op.param1)
                            dr5.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                riant.inviteIntoGroup(op.param1,[op.param3])
                                dr3.acceptGroupInvitation(op.param1)
                                riant.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dr1.inviteIntoGroup(op.param1,[op.param3])
                                    dr3.acceptGroupInvitation(op.param1)
                                    dr1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dr2.inviteIntoGroup(op.param1,[op.param3])
                                        dr3.acceptGroupInvitation(op.param1)
                                        dr2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dr4.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dr4.updateGroup(G)
                                            Ticket = dr4.reissueGroupTicket(op.param1)
                                            riant.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dr4.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dr3.updateGroup(G)
                                            Ticket = dr4.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dr4.inviteIntoGroup(op.param1,[op.param3])
                                                dr3.acceptGroupInvitation(op.param1)
                                                dr4.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dr5.inviteIntoGroup(op.param1,[op.param3])
                                                    dr3.acceptGroupInvitation(op.param1)
                                                    dr5.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr5.inviteIntoGroup(op.param1,[op.param3])
                        dr4.acceptGroupInvitation(op.param1)
                        dr5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            riant.inviteIntoGroup(op.param1,[op.param3])
                            dr4.acceptGroupInvitation(op.param1)
                            riant.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr1.inviteIntoGroup(op.param1,[op.param3])
                                dr4.acceptGroupInvitation(op.param1)
                                dr1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dr2.inviteIntoGroup(op.param1,[op.param3])
                                    dr4.acceptGroupInvitation(op.param1)
                                    dr2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dr3.inviteIntoGroup(op.param1,[op.param3])
                                        dr4.acceptGroupInvitation(op.param1)
                                        dr3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dr5.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dr5.updateGroup(G)
                                            Ticket = dr5.reissueGroupTicket(op.param1)
                                            riant.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dr5.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dr5.updateGroup(G)
                                            Ticket = dr5.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dr5.inviteIntoGroup(op.param1,[op.param3])
                                                dr4.acceptGroupInvitation(op.param1)
                                                dr5.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    riant.inviteIntoGroup(op.param1,[op.param3])
                                                    dr4.acceptGroupInvitation(op.param1)
                                                    riant.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        riant.inviteIntoGroup(op.param1,[op.param3])
                        dr5.acceptGroupInvitation(op.param1)
                        riant.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr1.inviteIntoGroup(op.param1,[op.param3])
                            dr5.acceptGroupInvitation(op.param1)
                            dr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr2.inviteIntoGroup(op.param1,[op.param3])
                                dr5.acceptGroupInvitation(op.param1)
                                dr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dr3.inviteIntoGroup(op.param1,[op.param3])
                                    dr5.acceptGroupInvitation(op.param1)
                                    dr3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dr4.inviteIntoGroup(op.param1,[op.param3])
                                        dr5.acceptGroupInvitation(op.param1)
                                        dr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = riant.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            riant.updateGroup(G)
                                            Ticket = riant.reissueGroupTicket(op.param1)
                                            dr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = riant.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            riant.updateGroup(G)
                                            Ticket = riant.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                riant.inviteIntoGroup(op.param1,[op.param3])
                                                dr5.acceptGroupInvitation(op.param1)
                                                riant.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dr1.inviteIntoGroup(op.param1,[op.param3])
                                                    dr5.acceptGroupInvitation(op.param1)
                                                    dr1.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        riant.findAndAddContactsByMid(op.param1,admin)
                        riant.inviteIntoGroup(op.param1,admin)
                        riant.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr1.findAndAddContactsByMid(op.param1,admin)
                            dr1.inviteIntoGroup(op.param1,admin)
                            dr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr2.findAndAddContactsByMid(op.param1,admin)
                                dr2.inviteIntoGroup(op.param1,admin)
                                dr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if creator in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dr1.findAndAddContactsByMid(op.param1,staff)
                        dr1.inviteIntoGroup(op.param1,staff)
                        dr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dr2.findAndAddContactsByMid(op.param1,staff)
                            dr2.inviteIntoGroup(op.param1,staff)
                            dr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dr3.findAndAddContactsByMid(op.param1,staff)
                                dr3.inviteIntoGroup(op.param1,staff)
                                dr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return
        #--------------------Kick Auto Bl-------#
        

        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = riant.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            riant.rejectGroupInvitation(op.param1)
                        else:
                            riant.acceptGroupInvitation(op.param1)
                    else:
                        riant.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        riant.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    riant.cancelGroupInvitation(op.param1, matched_list)
                  
            
        if op.type == 13:
            if mid in op.param3:
                G = riant.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            riant.rejectGroupInvitation(op.param1)
                        else:
                            riant.acceptGroupInvitation(op.param1)
                    else:
                        riant.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        riant.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    riant.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                riant.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                riant.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
	#-------------------------------------#
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg._from
                if msg._from == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            riant.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = riant.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            riant.updateGroup(X)
                        except:
                            riant.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    riant.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                riant.like(url[25:58], url[66:], likeType=1001)
#============================================================#
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = riant.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            riant.sendText(msg.to, _name + " Sudah DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                riant.findAndAddContactsByMid(target)
                                riant.inviteIntoGroup(msg.to,[target])
                                riant.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    riant.sendText(msg.to,'Error')
                                    wait["invite"] = False
                                    break
            else:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = dr1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            dr1.sendText(msg.to, _name + "Sudah di Group")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                dr1.findAndAddContactsByMid(target)
                                dr1.inviteIntoGroup(msg.to,[target])
                                dr1.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    dr1.sendText(msg.to,'Error')
                                    wait["invite"] = False
                                    break
#============================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        riant.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        riant.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        riant.sendText(msg.to,"hapus")
                        dr1.sendText(msg.to,"hapus")
                        dr2.sendText(msg.to,"hapus")
                        dr3.sendText(msg.to,"hapus")
                        dr4.sendText(msg.to,"hapus")
                        dr5.sendText(msg.to,"hapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        riant.sendText(msg.to,"tidak ada yang di backlist")
                        dr1.sendText(msg.to,"tidak ada yang di backlist")
                        dr2.sendText(msg.to,"tidak ada yang di backlist")
                        dr3.sendText(msg.to,"tidak ada yang di backlist")
                        dr4.sendText(msg.to,"tidak ada yang di backlist")
                        dr5.sendText(msg.to,"tidak ada yang di backlist")

                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        riant.sendText(msg.to,"siapkan")
                        dr1.sendText(msg.to,"siapkan")
                        dr2.sendText(msg.to,"siapkan")
                        dr3.sendText(msg.to,"siapkan")
                        dr4.sendText(msg.to,"siapkan")
                        dr5.sendText(msg.to,"siapkan")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        riant.sendText(msg.to,"aded")
                        dr1.sendText(msg.to,"aded")
                        dr2.sendText(msg.to,"aded")
                        dr3.sendText(msg.to,"aded")
                        dr4.sendText(msg.to,"aded")
                        dr5.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        riant.sendText(msg.to,"hapus")
                        dr1.sendText(msg.to,"hapus")
                        dr2.sendText(msg.to,"hapus")
                        dr3.sendText(msg.to,"hapus")
                        dr4.sendText(msg.to,"hapus")
                        dr5.sendText(msg.to,"hapus")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        riant.sendText(msg.to,"tidak ada yang di backlist")
                        dr1.sendText(msg.to,"tidak ada yang di backlist")
                        dr2.sendText(msg.to,"tidak ada yang di backlist")
                        dr3.sendText(msg.to,"tidak ada yang di backlist")
                        dr4.sendText(msg.to,"tidak ada yang di backlist")
                        dr5.sendText(msg.to,"tidak ada yang di backlist")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    riant.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = riant.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = riant.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        riant.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = riant.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = riant.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        riant.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    riant.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Helpbot"]:
                if wait["lang"] == "JP":
                    riant.sendText(msg.to,helpMessage)
                else:
                    riant.sendText(msg.to,helpt)
            elif ("Gn: " in msg.text):
               if msg._from in admin:
                if msg.toType == 2:
                    X = riant.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    riant.updateGroup(X)
                else:
                    riant.sendText(msg.to,"ᴵᵀ ᶜᴬᴺ'ᵀ ᴮᴱ ᵁˢᴱᴰ ᴮᴱˢᴵᴰᴱˢ ᵀᴴᴱ ᴳᴿᴼᵁᴾ")
            elif "Invitemid " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Invitemid ","")
                riant.findAndAddContactsByMid(midd)
                riant.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Undang"]:
               if msg._from in admin:
                wait["invite"] = True
                riant.sendText(msg.to,"✵ᴷᴵᴿᴵᴹ ᶜᴼᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ✵")
            elif msg.text in ["Daftar group"]:
               if msg._from in Owner:
                  dr1.sendText(msg.to,"ˢᴱᴰᴬᴺᴳ ᴹᴱᴺᴬᴹᴾᴵᴸᴷᴬᴺ")
                  gid = riant.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "║○%s\n" % (riant.getGroup(i).name+"\n║ANGGOTA "+str(len(riant.getGroup(i).members)))
                  riant.sendText(msg.to,"╔═════¤|{ DAFTARLIST }|¤═════\n" + h + "╠═══════[  JUMLAH  ]════════\n║" + str(len(gid)) + "\n╚════════════════════")
            elif msg.text in ["Reboot system"]:
               if msg._from in Owner:
                  riant.sendText(msg.to, "ᵂ ᴬ ᴵ ᵀ ᴵ ᴺ ᴳ ...")
                  restart_program()
                  print ("Restart")
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                if msg.toType == 2:
                    X = riant.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        riant.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            riant.sendText(msg.to,"No one is inviting")
                        else:
                            riant.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Can not be used outside the group")
                    else:
                        riant.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ourl","ourl"]:
               if msg._from in admin:
               	if msg.toType == 2:
                    X = riant.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    riant.updateGroup(X)
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Done")
                    else:
                        riant.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Can not be used outside the group")
                    else:
                        riant.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = riant.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    riant.updateGroup(X)
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"QR Sudah Di Tutup")
                    else:
                        riant.sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Can not be used outside the group")
                    else:
                        riant.sendText(msg.to,"Not for use less than group")
              else:
                  riant.sendText(msg.to,"Perintah Ditolak.")
                  riant.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text == "Ginfo":
               if msg._from in admin:
                if msg.toType == 2:
                    ginfo = riant.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventedJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        riant.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        riant.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Can not be used outside the group")
                    else:
                        riant.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                riant.sendText(msg.to,msg.to)
            elif msg.text in ["My mid"]:
                riant.sendText(msg.to,msg._from)
            elif msg.text in ["Me"]:
                dr1.sendContact(msg.to,msg._from)
                dr2.sendContact(msg.to,msg._from)
                dr3.sendContact(msg.to,msg._from)
                dr4.sendContact(msg.to,msg._from)
                dr5.sendContact(msg.to,msg._from)
                dr6.sendContact(msg.to,msg._from)
                dr7.sendContact(msg.to,msg._from)
                dr8.sendContact(msg.to,msg._from)
                dr9.sendContact(msg.to,msg._from)
                dr10.sendContact(msg.to,msg._from)
            elif msg.text in ["Virus"]:
            	riant.sendContact(to, "u43e02f888bfa5dad92a07b94a454b76f")
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                riant.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+riant.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = riant.getProfile()
                    profile.displayName = string
                    riant.updateProfile(profile)
                    riant.sendText(msg.to,"Update Names " + string)
            elif "Mybio " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 100000000000000:
                    profile = riant.getProfile()
                    profile.statusMessage = string
                    riant.updateProfile(profile)
                    riant.sendText(msg.to,"()Rubah menjadi→" + string + "←")
            elif msg.text in ["On cancelpro"]:
               if msg._from in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Cancel On")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"cancel On")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off cancelpro"]:
               if msg._from in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Cancel Off")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                         riant.sendText(msg.to,"cancel  Off")
                    else:
                         riant.sendText(msg.to,"done")
            elif msg.text in ["On block"]:
               if msg._from in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Blockinvite  ON")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Blockinvite  ON")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off block"]:
               if msg._from in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Blockinvite  OFF")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                         riant.sendText(msg.to,"Blockinvite  OFF")
                    else:
                         riant.sendText(msg.to,"done")
            elif msg.text in ["On qr"]:
               if msg._from in admin:
                if wait["CloseQR"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Closed QR On")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Closed QR ON")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off qr"]:
               if msg._from in admin:
                if wait["CloseQR"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"QR Off")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"QR Off")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["On joinpro"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ   ON")
                    else:
                        riant.sendText(msg.to,"Done")
                else:
                    wait["ProtectJoin"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ   ON")
                    else:
                        riant.sendText(msg.to,"Done")
            elif msg.text in ["Off joinpro"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ ᴰᴵ ᴹᴬᵀᴵᴷᴬᴺ")
                    else:
                        riant.sendText(msg.to,"Done")
                else:
                    wait["ProtectJoin"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ ᴰᴵ ᴹᴬᵀᴵᴷᴬᴺ")
                    else:
                        riant.sendText(msg.to,"Done")
            elif msg.text in ["On qr"]:
               if msg._from in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ ᴬᴷᵀᴵᶠ")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ ᴬᴷᵀᴵᶠ")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off qr"]:
               if msg._from in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ non ᴬᴷᵀᴵᶠ")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ non ᴬᴷᵀᴵᶠ")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["On k"]:
               if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off k"]:
               if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["On join"]:
               if msg._from in Owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Off join"]:
               if msg._from in Owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
               if msg._from in Owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            riant.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            riant.sendText(msg.to,"Invitation refused turned off")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            riant.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            riant.sendText(msg.to,strnum + "people and below decided to automatically refuse invitation")
                except:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Value is wrong")
                    else:
                        riant.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["On leave"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"done")
                    else:
                        riant.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"done")
                    else:
                        riant.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg._from in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"done")
                    else:
                        riant.sendText(msg.to,"Ready")
            elif msg.text in ["Off share"]:
               if msg._from in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"SUCSESS")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"SUCSESS")
                    else:
                        riant.sendText(msg.to,"DONE")
            elif msg.text in ["Set"]:
               if msg._from in admin:
                md = ""
                if wait["Protectcancel"] == True: md+=" Respon Cancel : on\n"
                else: md+=" Respon Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Link QR	    : on\n"
                else: md+=" Link QR	 : off\n"
                if wait["CloseQR"] == True: md+=" Tutup QR : on\n"
                else: md+=" Tutup QR   : off\n"
                if wait["Protectguest"] == True: md+=" BlockInvite : on\n"
                else: md+=" BlockInvite : off\n"
                if wait["contact"] == True: md+=" Countact : on\n"
                else: md+=" Countact : off\n"
                if wait["autoJoin"] == True: md+=" Respon Autojoin : on\n"
                else: md +=" Respon Autojoin : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Gcancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Gcancel : off\n"
                if wait["leaveRoom"] == True: md+=" Autoleave : on\n"
                else: md+=" Autoleave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Autoadd : on\n"
                else:md+=" Autoadd : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                riant.sendText(msg.to,md)
                riant.sendText(msg.to,md)
                riant.sendText(msg.to,md)
            elif msg.text in ["Group id"]:
               if msg._from in Owner:
                gid = riant.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (riant.getGroup(i).name,i)
                riant.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                gid = riant.getGroupIdsInvited()
                for i in gid:
                    riant.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    riant.sendText(msg.to,"All invitations have been refused")
                else:
                    riant.sendText(msg.to,"All invitations have been refused")
            elif msg.text in ["On add"]:
               if msg._from in Owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already on")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"done")
                    else:
                        riant.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Off add"]:
               if msg._from in Owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"already off")
                    else:
                        riant.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"done")
                    else:
                        riant.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = riant.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    riant.updateGroup(X)
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        riant.sendText(msg.to,"Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        riant.sendText(msg.to,"Can not be used outside the group")
                    else:
                        riant.sendText(msg.to,"Not for use less than group")
              else:
                  riant.sendText(msg.to,"ᴹᴬᴬᶠ ᴬᴺᴰᴬ ᴮᵁᴷᴬᴺ ᴬᴰᴹᴵᴺ")
                  riant.sendText(msg.to,"ᶜᴼᴹᴹᴬᴺᴰ ᴴᴬᴺᵞᴬ ᵁᴺᵀᵁᴷ ᴬᴰᴹᴵᴺ")
#-------------------------------- Lurking ---------------------------------#
            elif msg.text in ["Setpro on"]:
                    if msg._from in Owner:
                        wait["Protectguest"] = True
                        wait["ProtectQR"] = True
                        wait["Protectcancel"] = True
                        wait["ProtectJoin"] = True
                        dr1.sendMessage(msg.to,"Link Nikung ON 🤔")
                        dr2.sendMessage(msg.to,"On QR buat Nikung Active 🤔")
                        dr3.sendMessage(msg.to,"Protect tikungan ikut On 🤔")
                        dr4.sendMessage(msg.to,"Invite Tikungan On jugak 🤔")
                        dr5.sendMessage(msg.to,"Batalin Tikungan terpaksa ON 🤔")
                        dr6.sendMessage(msg.to,"Gak berani nikung\n  dalam pengawasan bojo  😒😒😒")
                        		            
            elif msg.text in ["Setpro off"]:
                    if msg._from in Owner:
                        wait["Protectguest"] = False
                        wait["ProtectQR"] = False
                        wait["Protectcancel"] = False
                        wait["ProtectJoin"] = False
                        dr1.sendMessage(msg.to,"off kan link buat nikung 🤔")
                        dr2.sendMessage(msg.to,"naaa aim ikut ug QR nikungnya 🤔")
                        dr3.sendMessage(msg.to,"terpaksa deh cancl tikungan ku off 🤔")
                        dr4.sendMessage(msg.to,"ikut az off buat invite tikungan 🤔")
                        dr5.sendMessage(msg.to,"hayoo di oof smw dah 🤔")
                        dr6.sendMessage(msg.to,"Gak berani napa2\n  bojo datang bulan\n agak sensi  😒😒😒")

#-------------------------------- Lurking ---------------------------------#
            elif msg.text in ["On lurk"]:
                tz = pytz.timezone("Asia/Makassar")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if receiver in read['readPoint']:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    riant.sendMessage(receiver,"Lurking telah diaktifkan")
                else:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    riant.sendMessage(receiver,"Set reading point : \n" + readTime)
                    
            elif msg.text in ["Lurking off"]:
                tz = pytz.timezone("Asia/Makassar")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if receiver not in read['readPoint']:
                    riant.sendMessage(receiver,"Lurking telah dinonaktifkan")
                else:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    riant.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
            elif msg.text in ["Lurking reset"]:
                tz = pytz.timezone("Asia/Makassar")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to in read["readPoint"]:
                    try:
                        del read["readPoint"][msg.to]
                        del read["readMember"][msg.to]
                        del read["setTime"][msg.to]
                        del read["ROM"][msg.to]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    riant.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                else:
                    riant.sendMessage(msg.to, "aktif az belom kok di reset")
#-----------------------------------------------
            elif msg.text in ["On read"]:
                if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                            try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                            except:
                                pass
                            wait2['readPoint'][msg.to] = msg.id
                            wait2['readMember'][msg.to] = ""
                            wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            wait2['ROM'][msg.to] = {}
                            with open('sider.json', 'w') as fp:
                             json.dump(wait2, fp, sort_keys=True, indent=4)
                             riant.sendText(msg.to,"Setpoint already on")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         riant.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
    
                        
            elif msg.text in ["Off read"]:
                if msg._from in admin:
                    if msg.to not in wait2['readPoint']:
                        riant.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        riant.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                                             
              
            elif msg.text in ["View","view"]:
                if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             riant.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])                       
                            cmem = riant.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        msg.contentMetadata = lol
                        try:
                          riant.sendMessage(msg)
                        except Exception as error:
                          pass
                        else:
                            riant.sendText(msg.to, "Lurking has not been set.")
#-----------------------------------------------
            elif msg.text in ["Tagall","Cintah"]:
                group = riant.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                k = len(nama)//100
                for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*100 : (a+1)*100]:
                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                        s += 7
                        txt += u'@Alin \n'
                    riant.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    riant.sendMessage(msg.to, "Total {} Mention".format(str(len(nama))))
                    
#----------------------------------------------------------------#
            elif msg.text in ["Tentang"]:
                try:
                    arr = []
                    owner = "u43e02f888bfa5dad92a07b94a454b76f"
                    creator = riant.getContact(owner)
                    contact = riant.getContact(mid)
                    grouplist = riant.getGroupIdsJoined()
                    contactlist = riant.getAllContactIds()
                    blockedlist = riant.getBlockedContactIds()
                    ret_ = "╔══[ About me ]"
                    ret_ += "\n╠ Line : {}".format(contact.displayName)
                    ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                    ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                    ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                    ret_ += "\n╠══[ About Alaybot-DR ]"
                    ret_ += "\n╠ Version : PY3"
                    ret_ += "\n╠ Creator : {}".format(creator.displayName)
                    ret_ += "\n╚══[ Don't be Remake :P ]"
                    riant.sendContact(msg.to, "u43e02f888bfa5dad92a07b94a454b76f")
                    riant.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    riant.sendMessage(msg.to, str(e))                    
#-------------------------------------------------------------------------------      
            elif msg.text in ["Daftar owner"]:
                try:
                    arr = []
                    owner = "u43e02f888bfa5dad92a07b94a454b76f"
                    creator = riant.getContact(owner)
                    ret_ = "╔════════════════\n╠✺ ➣  ✤ BOT DR ✤"
                    ret_ += "\n╠══✺〘Owner  List〙✺═══"
                    ret_ += "\n╠✺ Ownerlist : {}".format(creator.displayName)
                    ret_ += "\n╠════════════════"
                    ret_ += "\n╠✺〘 line.me/ti/p/ppgIZ0JLDW 〙"
                    ret_ += "\n╚════════════════"
                    riant.sendContact(msg.to, "u43e02f888bfa5dad92a07b94a454b76f")
                    riant.sendMessage(msg.to,"waiting ...")
                    riant.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    riant.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
            elif msg.text in ["Daftar admin"]:
                if msg._from in Owner:
                    if admin == []:
                        riant.sendMessage(msg.to,"daftar admin kosong")
                    else:
                        riant.sendMessage(msg.to,"waiting ...")
                        mc = "╔════════════════\n╠✺➣  ✤ BOT DR ✤\n╠══✺    ADMIN BOT  ✺═══\n"
                        for mi_d in admin:
                            mc += "╠✺ " +riant.getContact(mi_d).displayName + "\n"
                        riant.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/JYrhtHx832 〙\n╚════════════════")
                    
#----------------------------------Panggil Semua Bot------------------------------#
            elif msg.text in ["Masuk"]: 
              if msg._from in Owner:
                G = riant.getGroup(msg.to)
                G.preventedJoinByTicket = False
                riant.updateGroup(G)
                invsend = 0
                Ticket = riant.reissueGroupTicket(msg.to)
                dr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr5.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr6.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr7.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr8.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr9.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dr10.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = riant.getGroup(msg.to)
                ginfo = riant.getGroup(msg.to)
                G.preventedJoinByTicket = True
                riant.updateGroup(G)

            elif msg.text in ["Dr1 in"]:
	       #if msg._from in admin:
                G = riant.getGroup(msg.to)
                ginfo = riant.getGroup(msg.to)
                G.preventJoinByTicket = False
                riant.updateGroup(G)
                invsend = 0
                Ticket = riant.reissueGroupTicket(msg.to)
                dr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dr1.updateGroup(G)
            elif msg.text in ["Dr2 in"]:
	       #if msg._from in admin:
                G = riant.getGroup(msg.to)
                ginfo = riant.getGroup(msg.to)
                G.preventJoinByTicket = False
                riant.updateGroup(G)
                invsend = 0
                Ticket = riant.reissueGroupTicket(msg.to)
                dr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dr2.updateGroup(G)
            elif msg.text in ["Dr3 in"]:
	       #if msg._from in admin:
                G = riant.getGroup(msg.to)
                ginfo = riant.getGroup(msg.to)
                G.preventJoinByTicket = False
                riant.updateGroup(G)
                invsend = 0
                Ticket = riant.reissueGroupTicket(msg.to)
                dr3.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dr3.updateGroup(G)
            elif msg.text in ["Dr4 in"]:
	       #if msg._from in admin:
                G = riant.getGroup(msg.to)
                ginfo = riant.getGroup(msg.to)
                G.preventJoinByTicket = False
                riant.updateGroup(G)
                invsend = 0
                Ticket = riant.reissueGroupTicket(msg.to)
                dr4.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dr4.updateGroup(G)
		
#----------------Semua Bot Ninggalin Group Kecuali Bot Induk----------------------------#
            elif msg.text in ["Riant bye"]:
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = riant.getGroup(msg.to)
                    try:
                        dr1.leaveGroup(msg.to)
                        dr2.leaveGroup(msg.to)
                        dr3.leaveGroup(msg.to)
                        dr4.leaveGroup(msg.to)
                        dr5.leaveGroup(msg.to)
                        dr6.leaveGroup(msg.to)
                        dr7.leaveGroup(msg.to)
                        dr8.leaveGroup(msg.to)
                        dr9.leaveGroup(msg.to)
                        dr10.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------Bot Ninggalin Group termasuk Bot Induk----------------------------#
            elif msg.text in ["Riant out"]:
              if msg._from in Owner:
                if msg.toType == 2:
                    ginfo = riant.getGroup(msg.to)
                    try:
                        dr1.leaveGroup(msg.to)
                        dr2.leaveGroup(msg.to)
                        dr3.leaveGroup(msg.to)
                        dr4.leaveGroup(msg.to)
                        dr5.leaveGroup(msg.to)
                        dr6.leaveGroup(msg.to)
                        dr7.leaveGroup(msg.to)
                        dr8.leaveGroup(msg.to)
                        dr9.leaveGroup(msg.to)
                        dr10.leaveGroup(msg.to)
                        riant.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------Group Bc Start-------------------------------------#
            elif "Gbc " in msg.text:
               if msg._from in Owner:
                  bctxt = msg.text.replace("Gbc ", "")
                  a = riant.getGroupIdsJoined()
                  for manusia in a:
                    riant.sendText(manusia, (bctxt))
#--------------------------Group Bc Finish------------------------------------#                      
            elif "Tukimin " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Tukimin ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = dr1.getGroup(msg.to)
                       ginfo = dr1.getGroup(msg.to)
                       gs.preventedJoinByTicket = False
                       dr1.updateGroup(gs)
                       invsend = 0
                       Ticket = dr1.reissueGroupTicket(msg.to)
                       dr11.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                          sendMessage(msg.to,"user does not exist")
                          pass
                       else:
                          for target in targets:
                             try:
                               dr1.sendText(msg.to,"tha..tha..")
                               dr6.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                             except:
                               dr11.leaveGroup(msg.to)
                               gs = dr1.getGroup(msg.to)
                               gs.preventedJoinByTicket = True
                               dr1.updateGroup(gs)
                               gs.preventedJoinByTicket(gs)
                               dr1.updateGroup(gs)             
            elif "Belai " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Belai ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = riant.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8,dr9,dr10]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    dr1.sendText(msg.to,"Bye")
            elif "Bc @ " in msg.text:
               if msg._from in admin:
                _name = msg.text.replace("Bc @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = dr10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            riant.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    riant.sendText(msg.to,"Succes Cv")
                                except:
                                    riant.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Ban]ok")
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = riant.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        riant.sendText(msg.to,"ᵀᴬᴿᴳᴱᵀ ᵀᴵᴰᴬᴷ ᴬᴰᴬ")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                riant.sendText(msg.to,"Target Siap")
                            except:
                                riant.sendText(msg.to,"Berhasil")
            elif "Unban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Unban]ok")
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = riant.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        riant.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                riant.sendText(msg.to,"Succes Cv")
                            except:
                                riant.sendText(msg.to,"Succes Cv")
#----------------------------------------------------------------------------#
            elif msg.text in ["sa"]:
                if msg._from in admin:            	
                    dr1.sendMessage(msg.to,responsename1)
                    dr2.sendMessage(msg.to,responsename2)
                    dr3.sendMessage(msg.to,responsename3)
                    dr4.sendMessage(msg.to,responsename4)
                    dr5.sendMessage(msg.to,responsename5)
                    dr6.sendMessage(msg.to,responsename6)
                    dr7.sendMessage(msg.to,responsename7)
                    dr8.sendMessage(msg.to,responsename8)
                    dr9.sendMessage(msg.to,responsename9)
                    dr10.sendMessage(msg.to,responsename10)

#----------------------------------------------------------------------------#
            elif msg.text in ["Cekbot"]:
                if msg._from in admin:
                    dr1.sendContact(msg.to, Amid)
                    dr2.sendContact(msg.to, Bmid)
                    dr3.sendContact(msg.to, Cmid)
                    dr4.sendContact(msg.to, Dmid)
                    dr5.sendContact(msg.to, Emid)
                    dr6.sendContact(msg.to, Fmid)
                    dr7.sendContact(msg.to, Gmid)
                    dr8.sendContact(msg.to, Hmid)
                    dr9.sendContact(msg.to, Imid)
                    dr10.sendContact(msg.to, Jmid)
#-----------------------------------------------------------------------------
            
#---------------------------------------------------------------------
            elif msg.text in ["Sp","Speed"]:
               if msg._from in admin:
                start = time.time()
                print("Speed")
                elapsed_time = time.time() - start
                contact = riant.getProfile()
                mids = [contact.mid]
                name = "{}".format(str(contact.displayName))
                url = 'https://line.me/ti/p/JYrhtHx832'
                iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                text = "😂 my countact for add 😂\n       ALAYBOT-DR "
                sendMentionV10(msg.to, str(text), str(name), str(url), str(iconlink))
                riant.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
#------------------------------------------------------------------
            elif msg.text in ["Runtime"]:
               if msg._from in admin:
                runtime = time.time()-startBot
                elapsed_time = format_timespan(time.time()-startBot)
                riant.sendText(msg.to,"Running in %s" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
               if msg._from in admin:
                wait["wblacklist"] = True
                riant.sendText(msg.to,"ᴷᴵᴿᴵᴹ ᶜᴼᵁᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ")
            elif msg.text in ["Unban"]:
               if msg._from in admin:
                wait["dblacklist"] = True
                riant.sendText(msg.to,"ᴷᴵᴿᴵᴹ ᶜᴼᵁᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ")
            elif msg.text in ["Banlist"]:
               if msg._from in admin:
                if wait["blacklist"] == {}:
                    riant.sendText(msg.to,"nothing")
                else:
                    riant.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +riant.getContact(mi_d).displayName + "\n"
                    riant.sendText(msg.to,mc)
            elif msg.text in ["Cekban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = riant.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    riant.sendText(msg.to,cocoa + "")
            elif msg.text in ["Bersihkan"]:
                if msg._from in admin:
                    wait["blacklist"] = {}
                    riant.sendText(msg.to,"ˢᵁᶜˢᴱˢˢ")
            elif msg.text in ["Killban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = riant.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        riant.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        riant.kickoutFromGroup(msg.to,[jj])
                    riant.sendText(msg.to,"usir azah")
            elif msg.text in ["Cleanse"]:
               if msg._from in Owner:
                if msg.toType == 2:
                    group = riant.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        riant.cancelGroupInvitation(msg.to,[_mid])
                    riant.sendText(msg.to,"ᴵ ᴾᴿᴱᵀᴱᴺᴰᴱᴰ ᵀᴼ ᶜᴬᴺᶜᴱᴸ ᴬᴺᴰ ᶜᴬᴺᶜᴱᴸᴱᴰ.")
#------------------------------------------------------------#

#-----------------------------------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = riant.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              riant.sendText
          except:
             pass
#-----------------------------------#
        if op.type == 59:
            print(op)


    except Exception as error:
        print(error)


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = riant.getProfile()
                profile.displayName = wait["cName"]
                riant.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        ops = oepoll.singleTrace(count=100)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)

