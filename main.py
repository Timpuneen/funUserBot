from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client(
    "my_account",
    api_id=2951287,
    api_hash="ea357fcceeba62e7e025521b25fb9515"
)

@app.on_message(filters.command("timeD", prefixes=".") & filters.me)
def timeD(_, msg):
    secunds = 61
    orig_text = msg.text.split(".timeD ", maxsplit=1)[1]
    text = orig_text
    if('|' in text):
        secunds = int(text.split('|')[1])
        secunds +=1
        text = text.split('|')[0]

    while(secunds!=0):
        try:
            secunds-=1
            msg.edit('сообщение будет удалено через: '+ str(secunds)+'\n'+text)
            sleep(1)
 
        except FloodWait as e:
            sleep(e.x) 
    if(secunds==0):
        msg.delete()              
        


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" 
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) 
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    dobav = False
    perc = 0

    if('|' in msg.text):
        dobav = True
        yourText = msg.text.split('|')[1]
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных  ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных  ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
    if(dobav == False): 
        msg.edit("🦖 Найдены данные о существовании динозавров на земле! ")
    else:
        msg.edit("0_0 Найдены данные о "+ yourText)    
 
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
try:
    app.run()
except Exception as eror:
    print(eror)