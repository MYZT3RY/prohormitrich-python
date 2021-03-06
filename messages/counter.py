from configs import dbConfig
from db import dbconnect

def messageCounter(update):
    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id
    tgUsername = update.message.from_user.username

    # connecting to database
    db = dbconnect.dbConnect()
    cursor = db.cursor()

    # check if chat row exist in table
    cursor.execute("select`id`from`{0}`where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
    cursor.fetchall()

    if cursor.rowcount == 0: # if not exist then create
        cursor.execute("insert into`{0}`(`id`)values('{1}')".format(dbConfig.tblChats,tgChatId))

    # check if user row exist in table
    cursor.execute("select`id`from`{0}`where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
    cursor.fetchall()

    if cursor.rowcount == 0: # if not exist then create
        cursor.execute("insert into`{0}`(`userid`,`username`,`chatid`)values('{1}','{2}','{3}')".format(dbConfig.tblUsers,tgUserId,tgUsername,tgChatId))
    else: # else updating info
        if update.message.text != None or len(update.message.entities) != 0: # Text messages
            cursor.execute("update`{0}`set`messages`=`messages`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.voice != None: # Audio voice messages
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`voices`=`voices`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`voices`=`voices`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.video != None: # Video files
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`videos`=`videos`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`videos`=`videos`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.audio != None: # Audio files
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`audios`=`audios`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`audios`=`audios`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif len(update.message.photo) != 0: # Photo files
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`photos`=`photos`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`photos`=`photos`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.document != None: # Documents
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`documents`=`documents`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`documents`=`documents`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.sticker != None: # Stickers
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`stickers`=`stickers`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`stickers`=`stickers`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
        elif update.message.video_note != None: # Video messages
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`videovoices`=`videovoices`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            cursor.execute("update`{0}`set`messages`=`messages`+'1',`videovoices`=`videovoices`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))

    # closing database connection
    db.commit()
    cursor.close()
    db.close()