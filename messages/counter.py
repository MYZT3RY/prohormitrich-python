from configs import dbConfig
from db import dbconnect

def messageCounter(message):
    #print(message)
    tgChatId = message.chat_id
    tgUserId = message.from_user.id
    tgUsername = message.from_user.username

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
        if message.text != None or len(message.entities) != 0: # Text messages
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
	                            , c.messages = c.messages + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.voice != None: # Audio voice messages
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.voices = u.voices + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.voices = c.voices + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.video != None: # Video files
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.videos = u.videos + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.videos = c.videos + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.audio != None: # Audio files
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.audios = u.audios + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.audios = c.audios + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif len(message.photo) != 0: # Photo files
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.photos = u.photos + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.photos = c.photos + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.document != None: # Documents
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.documents = u.documents + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.documents = c.documents + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.sticker != None: # Stickers
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.stickers = u.stickers + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.stickers = c.stickers + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))
        elif message.video_note != None: # Video messages
            cursor.execute("update \
	                            {0} u \
		                            left join {1} c on c.id = u.chatid \
                            set \
	                            u.messages = u.messages + '1' \
                                , u.videovoices = u.videovoices + '1' \
	                            , c.messages = c.messages + '1' \
                                , c.videovoices = c.videovoices + '1' \
                            where \
	                            u.userid = '{2}' \
	                            and c.id = '{3}' \
            ".format(dbConfig.tblUsers, dbConfig.tblChats, tgUserId, tgChatId))

    # closing database connection
    db.commit()
    cursor.close()
    db.close()

def messageEditCounter(message):
    tgChatId = message.chat_id
    tgUserId = message.from_user.id

    # connecting to database
    db = dbconnect.dbConnect()
    cursor = db.cursor()

    if message.text != None or len(message.entities) != 0: # Text messages
        cursor.execute("update`{0}`set`edited_messages`=`edited_messages`+'1'where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
        cursor.execute("update`{0}`set`edited_messages`=`edited_messages`+'1'where`id`='{1}'".format(dbConfig.tblChats,tgChatId))

    # closing database connection
    db.commit()
    cursor.close()
    db.close()