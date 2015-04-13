#-*- coding: utf-8 -*-
from flask import jsonify, render_template
from flask import Flask, request

from app.db import init_db
from app.db import db_session
from app.models import *
from app.upload import upload

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='gogogogogogogogogogogogogogo',
    USERNAME='dbtest',
    PASSWORD='dkagh123'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app = Flask(__name__)



@app.route('/get_ddottylog')
def get_ddottylog():

    try:
        DDotty_query = db_session.query(DDotty).order_by("id desc")
        entries = [dict(date=log.time, img_path=log.img, content=log.content) for log in DDotty_query]
        return jsonify(success = True, result = entries)
    except:
        return jsonify(success = False, result = "")


@app.route('/ddottylog')
def ddottylog():
    return render_template('ddottylog.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = request.form['content']

    try:
        img_path = upload(file)
        print img_path
        log = DDotty(img_path, content)
        db_session.add(log)
        db_session.commit()

        return "success"
    except:
        return "fail"

@app.route('/')
def hello_world():
    lista= [1,2,3,4,5]
    a = {1:3,4:6,"ㅁ":1234}
    return jsonify( success = True, data = lista, test = a)

#Write
@app.route('/signup', methods = ['GET'])
def sign_up():
    try:
        user_name = request.args.get('user_name')
        googleId = request.args.get('google_id')
        count = db_session.query(User).filter(User.googleId ==googleId).count()
        if count == 0:
            user = User(user_name, googleId)
            db_session.add(user)
            db_session.commit()

        user = db_session.query(User).filter(User.googleId == googleId).first()

        return jsonify( success = True, user_id=user.id, user_name = user.name, user_googleId= user.googleId)
    except:
        return jsonify( success = False, user_id=0)

@app.route('/user_update', methods = ['GET'])
def user_update():
    try:
        id = request.args.get('user_id')
        name = request.args.get('name')

        user = db_session.query(User).filter(User.id==id).first()
        user.name = name

        db_session.commit()
        return jsonify( success = True, user_id=id)
    except:
        return jsonify( success = False, user_id="")



#Write
#댓글작성
@app.route('/write_comment', methods = ['POST'])
def write_comment():

    try:
        user_id = request.args.get('user_id')
        video_id = request.args.get('video_id')
        comment = request.args.get('comment')

        comment = Comment(user_id ,video_id, comment)
        db_session.add(comment)
        db_session.commit()

        return "success"

    except:
        return "fail"

#Send
#댓글 불러오기
@app.route('/get_comment', methods = ['GET'])
def send_comment():
    try:
        video_id = request.args.get('video_id')
        comment_list = db_session.query(Comment, User).join(User, Comment.user_id==User.id).filter(Comment.video_id == video_id ).order_by("comment.id desc")

        result = [dict(comment_id = result[0].id, user_name=result[1].name, user_img=result[1].img, comment=result[0].comment, like_count = result[0].like_count, comment_time = result[0].comment_time) for result in comment_list]

        return jsonify( success = True, comment = result)
    except:
        return jsonify( success = False, comment = "")

# #Send
# #bset 댓글 불러오기
@app.route('/get_best_comment', methods = ['GET'])
def send_best_comment():
    try:
        video_id = request.args.get('video_id')
        comment_list = db_session.query(Comment, User).join(User, Comment.user_id==User.id).filter(Comment.video_id == video_id ).order_by("comment.like_count desc")

        result = [dict(comment_id = result[0].id, user_name=result[1].name, user_img=result[1].img, comment=result[0].comment, like_count = result[0].like_count, comment_time = result[0].comment_time) for result in comment_list]

        return jsonify( success = True, comment = result)
    except:
        return jsonify( success = False, comment = "")

#Write
#댓글 좋야요
@app.route('/like_comment', methods = ['GET'])
def like_comment():
    try:
        comment_id = request.args.get('comment_id')
        user_id = request.args.get('user_id')

        count = db_session.query(Comment_like).filter(Comment_like.user_id == user_id,
                                                   Comment_like.comment_id ==comment_id).count()
        if count == 0:
            video_comment = db_session.query(Comment).filter(Comment.id == comment_id ).first()
            video_comment.like_count += 1

            i = Comment_like(user_id,comment_id)
            db_session.add(i)
            db_session.commit()
            return "success"
        else:
            return "duplication"

    except:
        return "fail"

#Write
@app.route('/check_favorite_video', methods = ['GET'])
def check_favorite_video():

    try:
        user_id = request.args.get('user_id')
        video_id = request.args.get('video_id')

        video = db_session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
                                                   Favorite_video.video_id ==video_id)
        count = video.count()
        if count == 0:
            return jsonify( result = False)
        else:
            return jsonify( result = True)
    except:
        return "fail"

#Write
@app.route('/check_favorite_playlist', methods = ['GET'])
def check_favorite_playlist():
    try:
        user_id = request.args.get('user_id')
        playlist_id = request.args.get('video_id')

        playlist = db_session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
                                                   Favorite_playlist.playlist_id ==playlist_id)
        count = playlist.count()

        if count == 0:
            return jsonify( result = False)
        else:
            return jsonify( result = True)
    except:
        return "fail"



#Write
@app.route('/add_favorite_video', methods = ['GET'])
def add_favorite_video():

    try:
        user_id = request.args.get('user_id')
        video_id = request.args.get('video_id')

        video = db_session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
                                                   Favorite_video.video_id ==video_id)
        count = video.count()
        if count == 0:
            i = Favorite_video(user_id ,video_id)
            db_session.add(i)
            db_session.commit()
            return "success"
        else:
            db_session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
                                                   Favorite_video.video_id ==video_id).delete()
            db_session.commit()
            return "duplication"

        return "success"
    except:
        return "fail"

#Write
@app.route('/add_favorite_playlist', methods = ['GET'])
def add_favorite_playlist():
    try:
        user_id = request.args.get('user_id')
        playlist_id = request.args.get('video_id')

        playlist = db_session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
                                                   Favorite_playlist.playlist_id ==playlist_id)
        count = playlist.count()

        if count == 0:
            i = Favorite_playlist(user_id, playlist_id)
            db_session.add(i)
            db_session.commit()
            return "success"
        else:
            db_session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
                                                   Favorite_playlist.playlist_id ==playlist_id).delete()
            db_session.commit()
            return "duplication"

    except:
        return "fail"


#Send
@app.route('/get_favorite_videolist', methods = ['GET'])
def send_favorite_video():
    user_id = request.args.get('user_id')
    try:
        favorite_video_query = db_session.query(Favorite_video).filter(Favorite_video.user_id==user_id).order_by("id desc")
        list_items =""
        for i in favorite_video_query:
            list_items += i.video_id +","

        return jsonify( success = True, video_list = list_items)

    except:
        return jsonify( success = False, video_list="")


#Send
@app.route('/get_favorite_playlist', methods = ['GET'])
def send_favorite_playlist():
    user_id = request.args.get('user_id')
    try:
        Favorite_playlist_query = db_session.query(Favorite_playlist).filter(Favorite_playlist.user_id==user_id).order_by("id desc")
        list_items =""
        for i in Favorite_playlist_query:
            list_items += i.playlist_id +","

        return jsonify( success = True, play_list = list_items)

    except:
        return jsonify( success = False, play_list="")


#Send
@app.route('/get_homecover', methods = ['GET'])
def send_home_cover():
    try:
        cover_list = db_session.query(Home_cover).order_by("id desc").first().video_id

        return jsonify( success = True, cover_list = cover_list)
    except:
        return jsonify( success = False, cover_list = "")


#Send
@app.route('/get_recommend', methods = ['GET'])
def recommend_video():
    try:
        cover_query = db_session.query(Recommend_cover).order_by("id desc").first()
        cover_list = cover_query.video_id

        list_query = db_session.query(Recommend_video).order_by("id desc").first()
        video_list = list_query.playlist_id

        return jsonify( success = True, cover_list=cover_list, video_list = video_list)
    except:
        return jsonify( success = False, cover_list="", video_list = "")


@app.route('/set_data', methods = ['GET'])
def set_video():
    try:
        video_type = str(request.args.get('video_type'))
        id = str(request.args.get('id'))

        if video_type == "home":
            video = Home_cover(id)

        elif video_type == "recommend_cover":
            video = Recommend_cover(str(id))

        else:
            video = Recommend_video(str(id))

        db_session.add(video)
        db_session.commit()

        return "success"

    except:
        return "false"





