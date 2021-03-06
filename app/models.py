from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from app import db

from sqlalchemy import Integer, String, DateTime, Text, Binary, Column

class DDotty(db.Model):
    __tablename__ = 'ddotty_log'
    id = Column(Integer, autoincrement=True, primary_key=True)
    time = Column('datemodified', TIMESTAMP,
       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    img = Column(String(255))
    content = Column(Text)

    def __init__(self, img, contnet):
        self.img = img
        self.content = contnet

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    googleId = Column(String(255))
    name = Column(String(255))
    img = Column(String(255))
    lastlogindate = Column(DateTime)
    createdtime = Column(DateTime)
    deviceid = Column(String(200))
    def __init__(self, name, googleId,lastlogindate, createdtime, deviceid):
        self.name = name
        self.googleId = googleId
        self.img =""
	self.lastlogindate = lastlogindate
	self.createdtime = createdtime
	self.deviceid = deviceid

class Favorite_video(db.Model):
    __tablename__ = 'favorite_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    video_id = Column(String(255))

    def __init__(self, user_id, video_id):
        self.user_id = user_id
        self.video_id = video_id

class Favorite_playlist(db.Model):
    __tablename__ = 'favorite_playlist'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    playlist_id = Column(String(255))

    def __init__(self, user_id, playlist_id):
        self.user_id = user_id
        self.playlist_id = playlist_id

class Recommend_video(db.Model):
    __tablename__ = 'recommend_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    playlist_id = Column(String(255))

    def __init__(self, play_list):
        self.playlist_id = play_list

class Recommend_cover(db.Model):
    __tablename__ = 'recommend_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))

    def __init__(self, video_id):
        self.video_id = video_id


class Home_cover(db.Model):
    __tablename__ = 'video_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))
    video_name = "dfsdfdf"
    video_date="1900-3-4"

    def __init__(self, video_id):
        self.video_id = video_id





#other app
class H_DDotty(db.Model):
    __tablename__ = 'h_ddotty_log'
    id = Column(Integer, autoincrement=True, primary_key=True)
    time = Column('datemodified', TIMESTAMP,
       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    img = Column(String(255))
    content = Column(Text)

    def __init__(self, img, contnet):
        self.img = img
        self.content = contnet

class H_User(db.Model):
    __tablename__ = 'h_users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    googleId = Column(String(255))
    name = Column(String(255))
    img = Column(String(255))

    def __init__(self, name, googleId):
        self.name = name;
        self.googleId = googleId;
        self.img =""


class H_Favorite_video(db.Model):
    __tablename__ = 'h_favorite_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    video_id = Column(String(255))

    def __init__(self, user_id, video_id):
        self.user_id = user_id
        self.video_id = video_id

class H_Favorite_playlist(db.Model):
    __tablename__ = 'h_favorite_playlist'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    playlist_id = Column(String(255))

    def __init__(self, user_id, playlist_id):
        self.user_id = user_id
        self.playlist_id = playlist_id

class H_Recommend_video(db.Model):
    __tablename__ = 'h_recommend_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    playlist_id = Column(String(255))

    def __init__(self, play_list):
        self.playlist_id = play_list

class H_Recommend_cover(db.Model):
    __tablename__ = 'h_recommend_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))

    def __init__(self, video_id):
        self.video_id = video_id


class H_Home_cover(db.Model):
    __tablename__ = 'h_video_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))
    video_name = "dfsdfdf"
    video_date="1900-3-4"

    def __init__(self, video_id):
        self.video_id = video_id
