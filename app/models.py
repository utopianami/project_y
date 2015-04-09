from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from app.db import Base

from sqlalchemy import Integer, String, Text, Binary, Column

class DDotty(Base):
    __tablename__ = 'ddotty_log'
    id = Column(Integer, autoincrement=True, primary_key=True)
    time = Column('datemodified', TIMESTAMP,
       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    img = Column(String(255))
    content = Column(Text)

    def __init__(self, img, contnet):
        self.img = img
        self.content = contnet

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    googleId = Column(String(255))
    name = Column(String(255))
    img = Column(String(255))
 
    def __init__(self, name, googleId):
        self.name = name;
        self.googleId = googleId;
        self.img =""


class Comment_like(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    comment_id = Column(String(255))

    def __init__(self, user_id, comment_id):
        self.user_id = user_id
        self.comment_id = comment_id

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    video_id = Column(String(255))
    like_count = Column(Integer)
    comment = Column(String(255))
    comment_time = Column('datemodified', TIMESTAMP,
       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, user_id, video_id, comment ):
        self.user_id = user_id
        self.video_id = video_id
        self.like_count = 0
        self.comment = comment

class Favorite_video(Base):
    __tablename__ = 'favorite_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    video_id = Column(String(255))

    def __init__(self, user_id, video_id):
        self.user_id = user_id
        self.video_id = video_id

class Favorite_playlist(Base):
    __tablename__ = 'favorite_playlist'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    playlist_id = Column(String(255))

    def __init__(self, user_id, playlist_id):
        self.user_id = user_id
        self.playlist_id = playlist_id

class Recommend_video(Base):
    __tablename__ = 'recommend_video'

    id = Column(Integer, autoincrement=True, primary_key=True)
    playlist_id = Column(String(255))

    def __init__(self, play_list):
        self.playlist_id = play_list

class Recommend_cover(Base):
    __tablename__ = 'recommend_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))

    def __init__(self, video_id):
        self.video_id = video_id


class Home_cover(Base):
    __tablename__ = 'video_cover'

    id = Column(Integer, autoincrement=True, primary_key=True)
    video_id = Column(String(255))

    def __init__(self, video_id):
        self.video_id = video_id

# class Dotty_log(Base):
#     __tablename__ = 'dotty_log'
