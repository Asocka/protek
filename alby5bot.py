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

riant = LINE('EyhgXI1q8HRIdVxJMPNe.RXVMBw0rl9fXOSQ2G/tX7G.YOpcYEHsy+gcpoDn1vAYgDogkMlvQsIQbJSkrBk5FTU=')#masukan akun utama mu bro
riant.log("Auth Token : " + str(riant.authToken))
channelToken = riant.getChannelResult()
riant.log("Channel Token : " + str(channelToken))


ririn = LINE('EyQLGQVo9awNN3hVWJs6.O7tk+ZOoW3+BZ48s7qdUnG.yWIric/hlnp24AcVXqyxpoLUFqAASlD82lQlmIhlxHU=')
ririn.log("Auth Token : " + str(ririn.authToken))
channelToken = ririn.getChannelResult()
ririn.log("Channel Token : " + str(channelToken))

dna1 = LINE('EyrqQjVpD2NYICM7v1t0./Flq6VqVBW0YIvLdm6lyOa.eYF0F/LmxyH5qPmvTBOJghDkmzQlbC3gn5ZWgF3KInU=')
dna1.log("Auth Token : " + str(dna1.authToken))
channelToken = dna1.getChannelResult()
dna1.log("Channel Token : " + str(channelToken))

dna2 = LINE('EyUY03eADNgNoMnMDu92./zcYHLlBA7s2VxAlWFJquG.KLJUA0BGJ3NuwxGzCrH4SM7LCKojPPGfUfHYqr2oXVU=')
dna2.log("Auth Token : " + str(dna2.authToken))
channelToken = dna2.getChannelResult()
dna2.log("Channel Token : " + str(channelToken))

dna3 = LINE('Eydua8jhYdQFFpvj2xJ0.DPBU4zUFd2HACxT67xlpia.aoM1kM6lLmHOaXbao+x3kfZ2uOpBzKFY8pO0bj6z5e0=')
dna3.log("Auth Token : " + str(dna3.authToken))
channelToken = dna3.getChannelResult()
dna3.log("Channel Token : " + str(channelToken))

dna4 = LINE('EywFB0QbdyUTwB9KoGo5.bpYj/o2nMFT8mvFgM+K69q.n0Tbdb3INzHqtIdE19JL8tGI9u7d3tD81YAcDX+sdOk=')
dna4.log("Auth Token : " + str(dna4.authToken))
channelToken = dna4.getChannelResult()
dna4.log("Channel Token : " + str(channelToken))

dna5 = LINE('Eyx0AwQzkfiVlSCITNI4.LqnCtNWt/LpdnighLTCsXa.TbH/6VJtL3cUSkGaPC//DGddYlEoN28BgbA02A4On6o=')
dna5.log("Auth Token : " + str(dna5.authToken))
channelToken = dna4.getChannelResult()
dna5.log("Channel Token : " + str(channelToken))

dna6 = LINE('Ey5yHCkCbGn7XgJLJjSf.7cNpbuPkRvQRw9wFFHG4VW.KooAF1vNeLjXm34377KGONglZtQ8zob3+2NUy4wMRZk=')#kicker
dna6.log("Auth Token : " + str(dna6.authToken))
channelToken = dna3.getChannelResult()
dna6.log("Channel Token : " + str(channelToken))

dna7 = LINE('EyMm6HEYUMjwCQitWA29.bW8OePfd1ZZzEQ+yV9Nzkq.zI1N/Riuvz5qethLArfo3tg1ZCY6UPNKqHDZ7U9cAB8=')#kicker
dna7.log("Auth Token : " + str(dna7.authToken))
channelToken = dna4.getChannelResult()
dna7.log("Channel Token : " + str(channelToken))

dna8 = LINE('EyurcIEBmaMHmrtVUXW2.CqA0Tb76CIullIy0JTMiWG.UYtri4MVhVv96C28JxruzmuLkxxcZlbgDbvf3mceWuM=')#kicker
dna8.log("Auth Token : " + str(dna8.authToken))
channelToken = dna4.getChannelResult()
dna8.log("Channel Token : " + str(channelToken))





helpMessage ="""
━━ೋ•🚱 •ೋ━━━┓
      
┗━━ೋ• 🚱•ೋ━━━
🔜 🚯 🚳 🚱 🔞 📵 🚭
🔜
🔜  ME
🔜  MODE ON/OFF
🔜  BERSIHKAN
🔜  DR OP
🔜  /DR OUT
🔜  /BYE DR
🔜  HELPBOT
╚══════════════╝
"""
oepoll = OEPoll(ririn)
KAC=[ririn,dna1,dna2,dna3,dna4,dna5]
mid = ririn.getProfile().mid
Amid = dna1.getProfile().mid
Bmid = dna2.getProfile().mid
Cmid = dna3.getProfile().mid
Dmid = dna4.getProfile().mid
Emid = dna5.getProfile().mid
Fmid = riant.getProfile().mid



responsename = ririn.getProfile().displayName
responsename2 = dna1.getProfile().displayName
responsename3 = dna2.getProfile().displayName
responsename4 = dna3.getProfile().displayName
responsename5 = dna4.getProfile().displayName
responsename6 = dna5.getProfile().displayName
responsename7 = dna6.getProfile().displayName
responsename8 = dna7.getProfile().displayName
responsename9 = dna8.getProfile().displayName


Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,"uae65bf02566258685a194fc0bbb9b56d","u5b5d2c21900195bbca7e590da3ad4e1e","u7a6d2813820c7c62b1216afb633d7368"]
admin=["u43e02f888bfa5dad92a07b94a454b76f","u5b5d2c21900195bbca7e590da3ad4e1e","uae65bf02566258685a194fc0bbb9b56d","u7a6d2813820c7c62b1216afb633d7368"]
Owner=["u43e02f888bfa5dad92a07b94a454b76f","u5b5d2c21900195bbca7e590da3ad4e1e","uae65bf02566258685a194fc0bbb9b56d","u7a6d2813820c7c62b1216afb633d7368"]
creator=["uae65bf02566258685a194fc0bbb9b56d"]
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
    "cName":"BOT ALBY ",
    "cName2":"BOT ALBY ",
    "cName3":"BOT ALBY ",
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
            Name = ririn.getContact(op.param2).displayName
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
    ririn.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ririn.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ririn.sendText(op.param1,str(wait["message"]))

	#--------Open Qr Kick Start--------------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	#X = dna5.getGroup(op.param1)
                 	#X.preventedJoinByTicket = False
                 	#dna5.updateGroup(X)
                 	Ticket = riant.reissueGroupTicket(op.param1)
                 	dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dna8.kickoutFromGroup(op.param1,[op.param2])
                 	dna8.leaveGroup(op.param1)
                 	X = dna1.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	dna1.updateGroup(X)
        #--------Open Qr Kick Start--------------#
        if op.type == 13:
            if wait["Protectguest"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	X = dna5.getGroup(op.param1)
                 	X.preventedJoinByTicket = False
                 	dna5.updateGroup(X)
                 	Ticket = riant.reissueGroupTicket(op.param1)
                 	dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dna7.kickoutFromGroup(op.param1,[op.param2])
                 	dna7.leaveGroup(op.param1)
                 	X = dna3.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	dna3.updateGroup(X)
	#--------Backup blockinvite--------------#
        #--------Backup autocancel--------------#
        if op.type == 17:
            if wait["ProtectJoin"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	X = dna4.getGroup(op.param1)
                 	X.preventedJoinByTicket = False
                 	dna4.updateGroup(X)
                 	Ticket = riant.reissueGroupTicket(op.param1)
                 	dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dna6.kickoutFromGroup(op.param1,[op.param2])
                 	dna6.leaveGroup(op.param1)
                 	X = ririn.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	ririn.updateGroup(X)
        if op.type == 13:
            G = ririn.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:
                    klist=[dna1,dna2,dna3,dna4,dna5]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        dna1.sendText(op.param1,"jagoan nih si jablay ...")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        dna1.sendMessage(c)
	#--------Open Qr Auto Close---------------#
        if op.type == 11:
            if not op.param2 in Bots:
                if wait["CloseQR"] == True:
                  try:
                      kpist=[ririn,dna1,dna2,dna3,dna4,dna5]
                      puck=random.choice(kpist)
                      G = puck.getGroup(op.param1)
                      G.preventJoinByTicket = True
                      puck.updateGroup(G)
                  except Exception as e:
                      print(e)
	#--------Open Qr Auto Close---------------#
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        ririn.acceptGroupInvitation(op.param1)
                        ginfo = ririn.getGroup(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                        ginfo = ririn.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dna1.acceptGroupInvitation(op.param1)
                        ginfo = dna1.getGroup(op.param1)
                    else:
                        dna1.acceptGroupInvitation(op.param1)
                        ginfo = dna1.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dna2.acceptGroupInvitation(op.param1)
                        ginfo = dna2.getGroup(op.param1)
                    else:
                        dna2.acceptGroupInvitation(op.param1)
                        ginfo = dna2.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dna3.acceptGroupInvitation(op.param1)
                        ginfo = dna3.getGroup(op.param1)
                    else:
                        dna3.acceptGroupInvitation(op.param1)
                        ginfo = dna3.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dna4.acceptGroupInvitation(op.param1)
                        ginfo = dna4.getGroup(op.param1)
                    else:
                        dna4.acceptGroupInvitation(op.param1)
                        ginfo = dna4.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        dna5.acceptGroupInvitation(op.param1)
                        ginfo = dna5.getGroup(op.param1)
                    else:
                        dna5.acceptGroupInvitation(op.param1)
                        ginfo = dna5.getGroup(op.param1)

            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        riant.acceptGroupInvitation(op.param1)
                        ginfo = dna5.getGroup(op.param1)
                    else:
                        riant.acceptGroupInvitation(op.param1)
                        ginfo = riant.getGroup(op.param1)

        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Kick Auto BL------------------------#
        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
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
                          print ("User Kick")
	#--------Invite User Kick Start-----------#
        if op.type == 13:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    try:
                        group = ririn.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            ririn.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = dna1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                dna1.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = dna2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    dna2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = dna3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        dna3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = dna5.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            dna4.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = dna5.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                dna5.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            pass
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            dna1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                dna2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    dna3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        dna4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            dna5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                ririn.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
        
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        dna1.findAndAddContactsByMid(op.param3)
                        dna1.inviteIntoGroup(op.param1,[op.param3])
                        ririn.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna3.kickoutFromGroup(op.param1,[op.param2])
                            dna2.findAndAddContactsByMid(op.param3)
                            dna2.inviteIntoGroup(op.param1,[op.param3])
                            ririn.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dna2.kickoutFromGroup(op.param1,[op.param2])
                                dna3.findAndAddContactsByMid(op.param3)
                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                ririn.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dna1.kickoutFromGroup(op.param1,[op.param2])
                                    dna4.findAndAddContactsByMid(op.param3)
                                    dna4.inviteIntoGroup(op.param1,[op.param3])
                                    ririn.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return         
              
        if op.type == 19:
            if Amid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dna5.kickoutFromGroup(op.param1,[op.param2])
                        dna5.findAndAddContactsByMid(op.param3)
                        dna5.inviteIntoGroup(op.param1,[op.param3])
                        dna1.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna4.kickoutFromGroup(op.param1,[op.param2])
                            dna4.findAndAddContactsByMid(op.param3)
                            dna4.inviteIntoGroup(op.param1,[op.param3])
                            dna1.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dna3.kickoutFromGroup(op.param1,[op.param2])
                                dna3.findAndAddContactsByMid(op.param3)
                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                dna1.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dna2.kickoutFromGroup(op.param1,[op.param2])
                                    dna2.findAndAddContactsByMid(op.param3)
                                    dna2.inviteIntoGroup(op.param1,[op.param3])
                                    dna1.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return         
              
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        dna4.findAndAddContactsByMid(op.param3)
                        dna4.inviteIntoGroup(op.param1,[op.param3])
                        dna2.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna3.kickoutFromGroup(op.param1,[op.param2])
                            dna3.findAndAddContactsByMid(op.param3)
                            dna3.inviteIntoGroup(op.param1,[op.param3])
                            dna2.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ririn.kickoutFromGroup(op.param1,[op.param2])
                                ririn.findAndAddContactsByMid(op.param3)
                                ririn.inviteIntoGroup(op.param1,[op.param3])
                                dna2.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dna1.kickoutFromGroup(op.param1,[op.param2])
                                    dna1.findAndAddContactsByMid(op.param3)
                                    dna1.inviteIntoGroup(op.param1,[op.param3])
                                    dna2.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return          
              
        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        ririn.findAndAddContactsByMid(op.param3)
                        ririn.inviteIntoGroup(op.param1,[op.param3])
                        dna3.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna1.kickoutFromGroup(op.param1,[op.param2])
                            dna1.findAndAddContactsByMid(op.param3)
                            dna1.inviteIntoGroup(op.param1,[op.param3])
                            dna3.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dna2.kickoutFromGroup(op.param1,[op.param2])
                                dna2.findAndAddContactsByMid(op.param3)
                                dna2.inviteIntoGroup(op.param1,[op.param3])
                                dna3.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dna1.kickoutFromGroup(op.param1,[op.param2])
                                    dna1.findAndAddContactsByMid(op.param3)
                                    dna1.inviteIntoGroup(op.param1,[op.param3])
                                    dna3.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        dna5.kickoutFromGroup(op.param1,[op.param2])
                                        dna5.findAndAddContactsByMid(op.param3)
                                        dna5.inviteIntoGroup(op.param1,[op.param3])
                                        dna3.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return

        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                        dna1.findAndAddContactsByMid(op.param3)
                        dna1.inviteIntoGroup(op.param1,[op.param3])
                        dna4.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna2.kickoutFromGroup(op.param1,[op.param2])
                            dna2.findAndAddContactsByMid(op.param3)
                            dna2.inviteIntoGroup(op.param1,[op.param3])
                            dna4.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dna3.kickoutFromGroup(op.param1,[op.param2])
                                dna3.findAndAddContactsByMid(op.param3)
                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                dna4.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    dna5.kickoutFromGroup(op.param1,[op.param2])
                                    dna5.findAndAddContactsByMid(op.param3)
                                    dna5.inviteIntoGroup(op.param1,[op.param3])
                                    dna4.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ririn.kickoutFromGroup(op.param1,[op.param2])
                                        ririn.findAndAddContactsByMid(op.param3)
                                        ririn.inviteIntoGroup(op.param1,[op.param3])
                                        dna4.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True  
                                    except:
                                        pass
                return
        
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 not in Bots:
                    try:
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                        dna2.findAndAddContactsByMid(op.param3)
                        dna2.inviteIntoGroup(op.param1,[op.param3])
                        dna5.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            dna3.kickoutFromGroup(op.param1,[op.param2])
                            dna3.findAndAddContactsByMid(op.param3)
                            dna3.inviteIntoGroup(op.param1,[op.param3])
                            dna5.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                dna4.kickoutFromGroup(op.param1,[op.param2])
                                dna4.findAndAddContactsByMid(op.param3)
                                dna4.inviteIntoGroup(op.param1,[op.param3])
                                dna5.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    ririn.kickoutFromGroup(op.param1,[op.param2])
                                    ririn.findAndAddContactsByMid(op.param3)
                                    ririn.inviteIntoGroup(op.param1,[op.param3])
                                    dna5.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).findAndAddContactsByMid(op.param3)
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        dna5.acceptGroupInvitation(op.param1)
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
                        dna1.inviteIntoGroup(op.param1,[op.param3])
                        ririn.acceptGroupInvitation(op.param1)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna2.inviteIntoGroup(op.param1,[op.param3])
                            ririn.acceptGroupInvitation(op.param1)
                            dna2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                ririn.acceptGroupInvitation(op.param1)
                                dna3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dna4.inviteIntoGroup(op.param1,[op.param3])
                                    ririn.acceptGroupInvitation(op.param1)
                                    dna4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dna5.inviteIntoGroup(op.param1,[op.param3])
                                        ririn.acceptGroupInvitation(op.param1)
                                        dna5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dna1.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dna1.updateGroup(G)
                                            Ticket = dna1.reissueGroupTicket(op.param1)
                                            ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dna1.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dna1.updateGroup(G)
                                            Ticket = dna1.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna1.inviteIntoGroup(op.param1,[op.param3])
                                                ririn.acceptGroupInvitation(op.param1)
                                                dna1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dna2.inviteIntoGroup(op.param1,[op.param3])
                                                    ririn.acceptGroupInvitation(op.param1)
                                                    dna2.kickoutFromGroup(op.param1,[op.param2])
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
                        dna2.inviteIntoGroup(op.param1,[op.param3])
                        dna1.acceptGroupInvitation(op.param1)
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna3.inviteIntoGroup(op.param1,[op.param3])
                            dna1.acceptGroupInvitation(op.param1)
                            dna3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna4.inviteIntoGroup(op.param1,[op.param3])
                                dna1.acceptGroupInvitation(op.param1)
                                dna4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dna5.inviteIntoGroup(op.param1,[op.param3])
                                    dna1.acceptGroupInvitation(op.param1)
                                    dna5.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ririn.inviteIntoGroup(op.param1,[op.param3])
                                        dna1.acceptGroupInvitation(op.param1)
                                        ririn.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dna2.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dna2.updateGroup(G)
                                            Ticket = dna2.reissueGroupTicket(op.param1)
                                            ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dna2.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dna2.updateGroup(G)
                                            Ticket = dna2.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna2.inviteIntoGroup(op.param1,[op.param3])
                                                dna1.acceptGroupInvitation(op.param1)
                                                dna2.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dna3.inviteIntoGroup(op.param1,[op.param3])
                                                    dna1.acceptGroupInvitation(op.param1)
                                                    dna3.kickoutFromGroup(op.param1,[op.param2])
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
                        dna3.inviteIntoGroup(op.param1,[op.param3])
                        dna2.acceptGroupInvitation(op.param1)
                        dna3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna4.inviteIntoGroup(op.param1,[op.param3])
                            dna2.acceptGroupInvitation(op.param1)
                            dna4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna5.inviteIntoGroup(op.param1,[op.param3])
                                dna2.acceptGroupInvitation(op.param1)
                                dna5.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ririn.inviteIntoGroup(op.param1,[op.param3])
                                    dna2.acceptGroupInvitation(op.param1)
                                    ririn.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dna1.inviteIntoGroup(op.param1,[op.param3])
                                        dna2.acceptGroupInvitation(op.param1)
                                        dna1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dna3.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dna3.updateGroup(G)
                                            Ticket = dna3.reissueGroupTicket(op.param1)
                                            ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dna3.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dna3.updateGroup(G)
                                            Ticket = dna3.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna3.inviteIntoGroup(op.param1,[op.param3])
                                                dna2.acceptGroupInvitation(op.param1)
                                                dna3.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dna4.inviteIntoGroup(op.param1,[op.param3])
                                                    dna2.acceptGroupInvitation(op.param1)
                                                    dna4.kickoutFromGroup(op.param1,[op.param2])
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
                        dna4.inviteIntoGroup(op.param1,[op.param3])
                        dna3.acceptGroupInvitation(op.param1)
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna5.inviteIntoGroup(op.param1,[op.param3])
                            dna3.acceptGroupInvitation(op.param1)
                            dna5.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ririn.inviteIntoGroup(op.param1,[op.param3])
                                dna3.acceptGroupInvitation(op.param1)
                                ririn.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dna1.inviteIntoGroup(op.param1,[op.param3])
                                    dna3.acceptGroupInvitation(op.param1)
                                    dna1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dna2.inviteIntoGroup(op.param1,[op.param3])
                                        dna3.acceptGroupInvitation(op.param1)
                                        dna2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dna4.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dna4.updateGroup(G)
                                            Ticket = dna4.reissueGroupTicket(op.param1)
                                            ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dna4.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dna3.updateGroup(G)
                                            Ticket = dna4.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna4.inviteIntoGroup(op.param1,[op.param3])
                                                dna3.acceptGroupInvitation(op.param1)
                                                dna4.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dna5.inviteIntoGroup(op.param1,[op.param3])
                                                    dna3.acceptGroupInvitation(op.param1)
                                                    dna5.kickoutFromGroup(op.param1,[op.param2])
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
                        dna5.inviteIntoGroup(op.param1,[op.param3])
                        dna4.acceptGroupInvitation(op.param1)
                        dna5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ririn.inviteIntoGroup(op.param1,[op.param3])
                            dna4.acceptGroupInvitation(op.param1)
                            ririn.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna1.inviteIntoGroup(op.param1,[op.param3])
                                dna4.acceptGroupInvitation(op.param1)
                                dna1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dna2.inviteIntoGroup(op.param1,[op.param3])
                                    dna4.acceptGroupInvitation(op.param1)
                                    dna2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dna3.inviteIntoGroup(op.param1,[op.param3])
                                        dna4.acceptGroupInvitation(op.param1)
                                        dna3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = dna5.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            dna5.updateGroup(G)
                                            Ticket = dna5.reissueGroupTicket(op.param1)
                                            ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = dna5.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            dna5.updateGroup(G)
                                            Ticket = dna5.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                dna5.inviteIntoGroup(op.param1,[op.param3])
                                                dna4.acceptGroupInvitation(op.param1)
                                                dna5.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ririn.inviteIntoGroup(op.param1,[op.param3])
                                                    dna4.acceptGroupInvitation(op.param1)
                                                    ririn.kickoutFromGroup(op.param1,[op.param2])
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
                        ririn.inviteIntoGroup(op.param1,[op.param3])
                        dna5.acceptGroupInvitation(op.param1)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna1.inviteIntoGroup(op.param1,[op.param3])
                            dna5.acceptGroupInvitation(op.param1)
                            dna1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna2.inviteIntoGroup(op.param1,[op.param3])
                                dna5.acceptGroupInvitation(op.param1)
                                dna2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    dna3.inviteIntoGroup(op.param1,[op.param3])
                                    dna5.acceptGroupInvitation(op.param1)
                                    dna3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        dna4.inviteIntoGroup(op.param1,[op.param3])
                                        dna5.acceptGroupInvitation(op.param1)
                                        dna4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ririn.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ririn.updateGroup(G)
                                            Ticket = ririn.reissueGroupTicket(op.param1)
                                            dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ririn.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ririn.updateGroup(G)
                                            Ticket = ririn.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ririn.inviteIntoGroup(op.param1,[op.param3])
                                                dna5.acceptGroupInvitation(op.param1)
                                                ririn.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    dna1.inviteIntoGroup(op.param1,[op.param3])
                                                    dna5.acceptGroupInvitation(op.param1)
                                                    dna1.kickoutFromGroup(op.param1,[op.param2])
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
                        ririn.findAndAddContactsByMid(op.param1,admin)
                        ririn.inviteIntoGroup(op.param1,admin)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna1.findAndAddContactsByMid(op.param1,admin)
                            dna1.inviteIntoGroup(op.param1,admin)
                            dna1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna2.findAndAddContactsByMid(op.param1,admin)
                                dna2.inviteIntoGroup(op.param1,admin)
                                dna2.kickoutFromGroup(op.param1,[op.param2])
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
                        dna1.findAndAddContactsByMid(op.param1,staff)
                        dna1.inviteIntoGroup(op.param1,staff)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dna2.findAndAddContactsByMid(op.param1,staff)
                            dna2.inviteIntoGroup(op.param1,staff)
                            dna2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dna3.findAndAddContactsByMid(op.param1,staff)
                                dna3.inviteIntoGroup(op.param1,staff)
                                dna3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return



        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Kick Auto BL------------------------#
        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
                 else:
                    pass
        #--------------------Kick Auto Bl-------#
        

        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)
                  
            
        if op.type == 13:
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
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
                            ririn.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ririn.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ririn.updateGroup(X)
                        except:
                            ririn.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ririn.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ririn.like(url[25:58], url[66:], likeType=1001)
#============================================================#
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ririn.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ririn.sendText(msg.to, _name + " Sudah DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ririn.findAndAddContactsByMid(target)
                                ririn.inviteIntoGroup(msg.to,[target])
                                ririn.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    ririn.sendText(msg.to,'Error')
                                    wait["invite"] = False
                                    break
            else:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = dna1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            dna1.sendText(msg.to, _name + "Sudah di Group")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                dna1.findAndAddContactsByMid(target)
                                dna1.inviteIntoGroup(msg.to,[target])
                                dna1.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    dna1.sendText(msg.to,'Error')
                                    wait["invite"] = False
                                    break
#============================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ririn.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ririn.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"hapus")
                        dna1.sendText(msg.to,"hapus")
                        dna2.sendText(msg.to,"hapus")
                        dna3.sendText(msg.to,"hapus")
                        dna4.sendText(msg.to,"hapus")
                        dna5.sendText(msg.to,"hapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ririn.sendText(msg.to,"tidak ada yang di backlist")
                        dna1.sendText(msg.to,"tidak ada yang di backlist")
                        dna2.sendText(msg.to,"tidak ada yang di backlist")
                        dna3.sendText(msg.to,"tidak ada yang di backlist")
                        dna4.sendText(msg.to,"tidak ada yang di backlist")
                        dna5.sendText(msg.to,"tidak ada yang di backlist")

                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ririn.sendText(msg.to,"siapkan")
                        dna1.sendText(msg.to,"siapkan")
                        dna2.sendText(msg.to,"siapkan")
                        dna3.sendText(msg.to,"siapkan")
                        dna4.sendText(msg.to,"siapkan")
                        dna5.sendText(msg.to,"siapkan")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ririn.sendText(msg.to,"aded")
                        dna1.sendText(msg.to,"aded")
                        dna2.sendText(msg.to,"aded")
                        dna3.sendText(msg.to,"aded")
                        dna4.sendText(msg.to,"aded")
                        dna5.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"hapus")
                        dna1.sendText(msg.to,"hapus")
                        dna2.sendText(msg.to,"hapus")
                        dna3.sendText(msg.to,"hapus")
                        dna4.sendText(msg.to,"hapus")
                        dna5.sendText(msg.to,"hapus")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ririn.sendText(msg.to,"tidak ada yang di backlist")
                        dna1.sendText(msg.to,"tidak ada yang di backlist")
                        dna2.sendText(msg.to,"tidak ada yang di backlist")
                        dna3.sendText(msg.to,"tidak ada yang di backlist")
                        dna4.sendText(msg.to,"tidak ada yang di backlist")
                        dna5.sendText(msg.to,"tidak ada yang di backlist")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    ririn.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ririn.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Helpbot"]:
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,helpMessage)
                else:
                    ririn.sendText(msg.to,helpt)
            elif ("Gn: " in msg.text):
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    ririn.updateGroup(X)
                else:
                    ririn.sendText(msg.to,"ᴵᵀ ᶜᴬᴺ'ᵀ ᴮᴱ ᵁˢᴱᴰ ᴮᴱˢᴵᴰᴱˢ ᵀᴴᴱ ᴳᴿᴼᵁᴾ")
            elif "Invitemid " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Invitemid ","")
                ririn.findAndAddContactsByMid(midd)
                ririn.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Undang"]:
               if msg._from in admin:
                wait["invite"] = True
                ririn.sendText(msg.to,"✵ᴷᴵᴿᴵᴹ ᶜᴼᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ✵")
            elif msg.text in ["Daftar group"]:
               if msg._from in Owner:
                  dna1.sendText(msg.to,"ˢᴱᴰᴬᴺᴳ ᴹᴱᴺᴬᴹᴾᴵᴸᴷᴬᴺ")
                  gid = ririn.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "║○%s\n" % (ririn.getGroup(i).name+"\n║ANGGOTA "+str(len(ririn.getGroup(i).members)))
                  ririn.sendText(msg.to,"╔═════¤|{ DAFTARLIST }|¤═════\n" + h + "╠═══════[  JUMLAH  ]════════\n║" + str(len(gid)) + "\n╚════════════════════")
            elif msg.text in ["Reboot system"]:
               if msg._from in Owner:
                  ririn.sendText(msg.to, "ᵂ ᴬ ᴵ ᵀ ᴵ ᴺ ᴳ ...")
                  restart_program()
                  print ("Restart")
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ririn.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"No one is inviting")
                        else:
                            ririn.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print ririn.getGroup(msg.to)
                ##ririn.sendMessage(msg)
            elif msg.text in ["Ourl","ourl"]:
               if msg._from in admin:
               	if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Done")
                    else:
                        ririn.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        ririn.sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"Perintah Ditolak.")
                  ririn.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text == "Ginfo":
               if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
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
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                ririn.sendText(msg.to,msg.to)
            elif msg.text in ["My mid"]:
                ririn.sendText(msg.to,msg._from)
            elif msg.text in ["Me"]:
                dna1.sendContact(msg.to,msg._from)
                dna2.sendContact(msg.to,msg._from)
                dna3.sendContact(msg.to,msg._from)
                dna4.sendContact(msg.to,msg._from)
                dna5.sendContact(msg.to,msg._from)
            elif msg.text in ["Virus"]:
            	ririn.sendContact(to, "u43e02f888bfa5dad92a07b94a454b76f',")
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                ririn.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ririn.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ririn.getProfile()
                    profile.displayName = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"Update Names " + string)
            elif "Mybio " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 100000000000000:
                    profile = ririn.getProfile()
                    profile.statusMessage = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"()Rubah menjadi→" + string + "←")
            elif msg.text in ["On cancelpro"]:
               if msg._from in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off cancelpro"]:
               if msg._from in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Cancel Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"cancel  Off")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["On block"]:
               if msg._from in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Blockinvite  ON")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Blockinvite  ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off block"]:
               if msg._from in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Blockinvite  OFF")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"Blockinvite  OFF")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["On qr"]:
               if msg._from in admin:
                if wait["CloseQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off qr"]:
               if msg._from in admin:
                if wait["CloseQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["On joinpro"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ   ON")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["ProtectJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ   ON")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["Off joinpro"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ ᴰᴵ ᴹᴬᵀᴵᴷᴬᴺ")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["ProtectJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴹᴼᴰᴱ ᴶᴼᴵᴺ ᴰᴵ ᴹᴬᵀᴵᴷᴬᴺ")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["On qr"]:
               if msg._from in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ ᴬᴷᵀᴵᶠ")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ ᴬᴷᵀᴵᶠ")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off qr"]:
               if msg._from in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ non ᴬᴷᵀᴵᶠ")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴸᴵᴺᴷ ᵟᴿ non ᴬᴷᵀᴵᶠ")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["On k"]:
               if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off k"]:
               if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["On join"]:
               if msg._from in Owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Off join"]:
               if msg._from in Owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
               if msg._from in Owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            ririn.sendText(msg.to,"Invitation refused turned off")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            ririn.sendText(msg.to,strnum + "people and below decided to automatically refuse invitation")
                except:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Value is wrong")
                    else:
                        ririn.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["On leave"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg._from in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"Ready")
            elif msg.text in ["Off share"]:
               if msg._from in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"SUCSESS")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"SUCSESS")
                    else:
                        ririn.sendText(msg.to,"DONE")
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
                ririn.sendText(msg.to,md)
                ririn.sendText(msg.to,md)
                ririn.sendText(msg.to,md)
            elif msg.text in ["Group id"]:
               if msg._from in Owner:
                gid = ririn.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ririn.getGroup(i).name,i)
                ririn.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsInvited()
                for i in gid:
                    ririn.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,"All invitations have been refused")
                else:
                    ririn.sendText(msg.to,"All invitations have been refused")
            elif msg.text in ["On add"]:
               if msg._from in Owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Off add"]:
               if msg._from in Owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        ririn.sendText(msg.to,"Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"ᴹᴬᴬᶠ ᴬᴺᴰᴬ ᴮᵁᴷᴬᴺ ᴬᴰᴹᴵᴺ")
                  ririn.sendText(msg.to,"ᶜᴼᴹᴹᴬᴺᴰ ᴴᴬᴺᵞᴬ ᵁᴺᵀᵁᴷ ᴬᴰᴹᴵᴺ")
#-------------------------------- Lurking ---------------------------------#
            elif msg.text in ["Mod on"]:
                    if msg._from in Owner:
                        wait["Protectguest"] = True
                        wait["ProtectQR"] = True
                        wait["Protectcancel"] = True
                        wait["ProtectJoin"] = True
                        wait["protectionOn"] = True
                        dna1.sendMessage(msg.to,"Link Nikung ON 🤔")
                        dna2.sendMessage(msg.to,"On QR buat Nikung Active 🤔")
                        dna3.sendMessage(msg.to,"Protect tikungan ikut On 🤔")
                        dna4.sendMessage(msg.to,"Invite Tikungan On jugak 🤔")
                        dna5.sendMessage(msg.to,"Batalin Tikungan terpaksa ON 🤔")
                        dna6.sendMessage(msg.to,"Gak berani nikung\n  dalam pengawasan bojo  😒😒😒")
                        		            
            elif msg.text in ["Mod off"]:
                    if msg._from in Owner:
                        wait["Protectguest"] = False
                        wait["ProtectQR"] = False
                        wait["Protectcancel"] = False
                        wait["ProtectJoin"] = False
                        wait["protectionOn"] = False
                        dna1.sendMessage(msg.to,"off kan link buat nikung 🤔")
                        dna2.sendMessage(msg.to,"naaa aim ikut ug QR nikungnya 🤔")
                        dna3.sendMessage(msg.to,"terpaksa deh cancl tikungan ku off 🤔")
                        dna4.sendMessage(msg.to,"ikut az off buat invite tikungan 🤔")
                        dna5.sendMessage(msg.to,"hayoo di oof smw dah 🤔")
                        dna6.sendMessage(msg.to,"Gak berani napa2\n  bojo datang bulan\n agak sensi  😒😒😒")

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
                    ririn.sendMessage(receiver,"Lurking telah diaktifkan")
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
                    ririn.sendMessage(receiver,"Set reading point : \n" + readTime)
                    
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
                    ririn.sendMessage(receiver,"Lurking telah dinonaktifkan")
                else:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    ririn.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
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
                    ririn.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                else:
                    ririn.sendMessage(msg.to, "aktif az belom kok di reset")
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
                             ririn.sendText(msg.to,"Setpoint already on")
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
                         ririn.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
    
                        
            elif msg.text in ["Off read"]:
                if msg._from in admin:
                    if msg.to not in wait2['readPoint']:
                        ririn.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        ririn.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                                             
              
            elif msg.text in ["View","view"]:
                if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             ririn.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])                       
                            cmem = ririn.getContacts(chiya)
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
                          ririn.sendMessage(msg)
                        except Exception as error:
                          pass
                        else:
                            ririn.sendText(msg.to, "Lurking has not been set.")
#-----------------------------------------------
            elif msg.text in ["Tagall","Cintah"]:
                group = ririn.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                if jml <= 20:
                    mentionMembers(msg.to, nama)
                if jml > 20 and jml < 40:
                    for i in range (0, 20):
                        nm1 += [nama[i]]
                    mentionMembers(msg.to, nm1)
                    for j in range (20, len(nama)-1):
                        nm2 += [nama[j]]
                    mentionMembers(msg.to, nm2)
                if jml > 40 and jml < 60:
                    for i in range (0, 20):
                        nm1 += [nama[i]]
                    mentionMembers(msg.to, nm1)
                    for j in range (20, 40):
                        nm2 += [nama[j]]
                    mentionMembers(msg.to, nm2)
                    for k in range (40, len(nama)-1):
                        nm3 += [nama[k]]
                    mentionMembers(msg.to, nm3)
                if jml > 60 and jml < 80:
                    for i in range (0, 20):
                        nm1 += [nama[i]]
                    mentionMembers(msg.to, nm1)
                    for j in range (20, 40):
                        nm2 += [nama[j]]
                    mentionMembers(msg.to, nm2)
                    for k in range (40, 60):
                        nm3 += [nama[k]]
                    mentionMembers(msg.to, nm3)
                    for l in range (80, len(nama)-1):
                        nm4 += [nama[l]]
                    mentionMembers(msg.to, nm4)
                if jml > 80 and jml < 100:
                    for i in range (0, 20):
                        nm1 += [nama[i]]
                    mentionMembers(msg.to, nm1)
                    for j in range (20, 40):
                       nm2 += [nama[j]]
                    mentionMembers(msg.to, nm2)
                    for k in range (40, 60):
                        nm3 += [nama[k]]
                    mentionMembers(msg.to, nm3)
                    for l in range (60, 80):
                        nm4 += [nama[l]]
                    mentionMembers(msg.to, nm4)
                    for m in range (80, len(nama)-1):
                        nm5 += [nama[m]]
                    mentionMembers(msg.to, nm4)
                    
#----------------------------------------------------------------#
            elif msg.text in ["Tentang"]:
                try:
                    arr = []
                    owner = "u43e02f888bfa5dad92a07b94a454b76f"
                    creator = ririn.getContact(owner)
                    contact = ririn.getContact(mid)
                    grouplist = ririn.getGroupIdsJoined()
                    contactlist = ririn.getAllContactIds()
                    blockedlist = ririn.getBlockedContactIds()
                    ret_ = "╔══[ About me ]"
                    ret_ += "\n╠ Line : {}".format(contact.displayName)
                    ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                    ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                    ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                    ret_ += "\n╠══[ About Alaybot-DR ]"
                    ret_ += "\n╠ Version : PY3"
                    ret_ += "\n╠ Creator : {}".format(creator.displayName)
                    ret_ += "\n╚══[ Don't be Remake :P ]"
                    ririn.sendContact(msg.to, "u43e02f888bfa5dad92a07b94a454b76f")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))                    
#-------------------------------------------------------------------------------      
            elif msg.text in ["Daftar owner"]:
                try:
                    arr = []
                    owner = "u43e02f888bfa5dad92a07b94a454b76f"
                    creator = ririn.getContact(owner)
                    ret_ = "╔════════════════\n╠✺ ➣  ✤ BOT DR ✤"
                    ret_ += "\n╠══✺〘Owner  List〙✺═══"
                    ret_ += "\n╠✺ Ownerlist : {}".format(creator.displayName)
                    ret_ += "\n╠════════════════"
                    ret_ += "\n╠✺〘 line.me/ti/p/ppgIZ0JLDW 〙"
                    ret_ += "\n╚════════════════"
                    ririn.sendContact(msg.to, "u43e02f888bfa5dad92a07b94a454b76f")
                    ririn.sendMessage(msg.to,"waiting ...")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
            elif msg.text in ["Daftar admin"]:
                if msg._from in Owner:
                    if admin == []:
                        ririn.sendMessage(msg.to,"daftar admin kosong")
                    else:
                        ririn.sendMessage(msg.to,"waiting ...")
                        mc = "╔════════════════\n╠✺➣  ✤ BOT DR ✤\n╠══✺    ADMIN BOT  ✺═══\n"
                        for mi_d in admin:
                            mc += "╠✺ " +ririn.getContact(mi_d).displayName + "\n"
                        ririn.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/JYrhtHx832 〙\n╚════════════════")
                    
#----------------------------------Panggil Semua Bot------------------------------#
            elif msg.text in ["Dr op"]: 
              if msg._from in Owner:
                G = ririn.getGroup(msg.to)
                #ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna5.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = True
                ririn.updateGroup(G)

            elif msg.text in ["Dr1 in"]:
	       #if msg._from in admin:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna1.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dna1.updateGroup(G)
            elif msg.text in ["Dr2 in"]:
	       #if msg._from in admin:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna2.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dna2.updateGroup(G)
            elif msg.text in ["Dr3 in"]:
	       #if msg._from in admin:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna3.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dna3.updateGroup(G)
            elif msg.text in ["Dr4 in"]:
	       #if msg._from in admin:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna4.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                dna4.updateGroup(G)
		
#----------------Semua Bot Ninggalin Group Kecuali Bot Induk----------------------------#
            elif msg.text in ["/bye dr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        dna1.leaveGroup(msg.to)
                        dna2.leaveGroup(msg.to)
                        dna3.leaveGroup(msg.to)
                        dna4.leaveGroup(msg.to)
                        dna5.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------Bot Ninggalin Group termasuk Bot Induk----------------------------#
            elif msg.text in ["/dr out"]:
              if msg._from in Owner:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        dna1.leaveGroup(msg.to)
                        dna2.leaveGroup(msg.to)
                        dna3.leaveGroup(msg.to)
                        dna4.leaveGroup(msg.to)
                        dna5.leaveGroup(msg.to)
                        ririn.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------Group Bc Start-------------------------------------#
            elif "Gbc " in msg.text:
               if msg._from in Owner:
                  bctxt = msg.text.replace("Gbc ", "")
                  a = ririn.getGroupIdsJoined()
                  for manusia in a:
                    ririn.sendText(manusia, (bctxt))
#--------------------------Group Bc Finish------------------------------------#                      
            elif "Tukimin " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Tukimin ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ririn.getGroup(msg.to)
                       ginfo = ririn.getGroup(msg.to)
                       gs.preventedJoinByTicket = False
                       ririn.updateGroup(gs)
                       invsend = 0
                       Ticket = ririn.reissueGroupTicket(msg.to)
                       dna6.acceptGroupInvitationByTicket(msg.to,Ticket)
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
                               dna1.sendText(msg.to,"tha..tha..")
                               dna6.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                             except:
                               dna6.leaveGroup(msg.to)
                               gs = dna1.getGroup(msg.to)
                               gs.preventedJoinByTicket = True
                               dna1.updateGroup(gs)
                               gs.preventedJoinByTicket(gs)
                               dna1.updateGroup(gs)             
            elif "Belai " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Belai ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ririn.getGroup(msg.to)
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
                                    klist=[ririn,dna1,dna2,dna3,dna4,dna5]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    dna1.sendText(msg.to," nahh")
            elif "Bc @ " in msg.text:
               if msg._from in admin:
                _name = msg.text.replace("Bc @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = dna12.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ririn.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ririn.sendText(msg.to,"Succes Cv")
                                except:
                                    ririn.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Ban]ok")
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"ᵀᴬᴿᴳᴱᵀ ᵀᴵᴰᴬᴷ ᴬᴰᴬ")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Target Siap")
                            except:
                                ririn.sendText(msg.to,"Berhasil")
            elif "Unban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Unban]ok")
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Succes Cv")
                            except:
                                ririn.sendText(msg.to,"Succes Cv")
#----------------------------------------------------------------------------#
            elif msg.text in ["Sa"]:
                if msg._from in admin:            	
                    ririn.sendMessage(msg.to,responsename)
                    dna1.sendMessage(msg.to,responsename2)
                    dna2.sendMessage(msg.to,responsename3)
                    dna3.sendMessage(msg.to,responsename4)
                    dna4.sendMessage(msg.to,responsename5)
                    dna5.sendMessage(msg.to,responsename6)

#----------------------------------------------------------------------------#
            elif msg.text in ["Cekbot"]:
                if msg._from in admin:
                    ririn.sendContact(msg.to, mid)
                    dna1.sendContact(msg.to, Amid)
                    dna2.sendContact(msg.to, Bmid)
                    dna3.sendContact(msg.to, Cmid)
                    dna4.sendContact(msg.to, Dmid)
                    dna5.sendContact(msg.to, Emid)
#-----------------------------------------------------------------------------
#---------------------------------------------------------------------
            elif msg.text in ["Sp","Speed"]:
                start = time.time()
                print("Speed")
                elapsed_time = time.time() - start
                contact = ririn.getProfile()
                mids = [contact.mid]
                name = "{}".format(str(contact.displayName))
                url = 'https://line.me/ti/p/JYrhtHx832'
                iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                text = "😂 my countact for add 😂\n       ALAYBOT-DR "
                sendMentionV10(msg.to, str(text), str(name), str(url), str(iconlink))
                ririn.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
#------------------------------------------------------------------
            elif msg.text in ["Runtime"]:
               if msg._from in admin:
                runtime = time.time()-startBot
                elapsed_time = format_timespan(time.time()-startBot)
                ririn.sendText(msg.to,"Running in %s" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Admin on "]:
               if msg._from in admin:
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                  for target in targets:
                          try:
                              admin.append(target)
                              ririn.sendMessage(msg.to,"menambahkan admin")
                          except:
                              pass
            elif msg.text in ["Ban"]:
               if msg._from in admin:
                wait["wblacklist"] = True
                ririn.sendText(msg.to,"ᴷᴵᴿᴵᴹ ᶜᴼᵁᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ")
            elif msg.text in ["Unban"]:
               if msg._from in admin:
                wait["dblacklist"] = True
                ririn.sendText(msg.to,"ᴷᴵᴿᴵᴹ ᶜᴼᵁᴺᵀᴬᶜᵀ ᴷᴱ ᴳᴿᴼᵁᴾ")
            elif msg.text in ["Banlist"]:
               if msg._from in admin:
                if wait["blacklist"] == {}:
                    ririn.sendText(msg.to,"nothing")
                else:
                    ririn.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ririn.getContact(mi_d).displayName + "\n"
                    ririn.sendText(msg.to,mc)
            elif msg.text in ["Cekban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    ririn.sendText(msg.to,cocoa + "")
            elif msg.text in ["Bersihkan"]:
                if msg._from in admin:
                    wait["blacklist"] = {}
                    ririn.sendText(msg.to,"ˢᵁᶜˢᴱˢˢ")
            elif msg.text in ["Killban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ririn.kickoutFromGroup(msg.to,[jj])
                    ririn.sendText(msg.to,"usir azah")
            elif msg.text in ["Cleanse"]:
               if msg._from in Owner:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ririn.cancelGroupInvitation(msg.to,[_mid])
                    ririn.sendText(msg.to,"ᴵ ᴾᴿᴱᵀᴱᴺᴰᴱᴰ ᵀᴼ ᶜᴬᴺᶜᴱᴸ ᴬᴺᴰ ᶜᴬᴺᶜᴱᴸᴱᴰ.")
#------------------------------------------------------------#

#----------------Fungsi Cek Sider-------------------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = ririn.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              ririn.sendText
          except:
             pass
#----------------Fungsi Cek Sider-------------------#
        if op.type == 59:
            print(op)


    except Exception as error:
        print(error)


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","60","70","80","90","100","00"]:
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
                profile = ririn.getProfile()
                profile.displayName = wait["cName"]
                ririn.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
