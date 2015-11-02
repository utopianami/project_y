#-*- coding: utf-8 -*-
from flask import jsonify, render_template
from flask import Flask, request
from flask import Flask, render_template, jsonify, session
from flask.ext.sqlalchemy import SQLAlchemy
import urllib2
import json
import urllib2


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)



from app.models import *
from app.upload import upload

from app.hongbangjang.views import mod as hongbangjangModule
app.register_blueprint(hongbangjangModule)


@app.route('/')
def hello_world():

    try:
	print('HELLO');
        count = db.session.query(User).count()
        return jsonify( success = True, member = count)
    except:
        return jsonify( success = False, member = 0)



@app.route('/get_ddottylog')
def get_ddottylog():

    try:
        DDotty_query = db.session.query(DDotty).order_by("id desc")
        entries = [dict(date=log.time, img_path=log.img, content=log.content) for log in DDotty_query]
        return jsonify(success = True, result = entries)
    except:
        return jsonify(success = False, result = "")


@app.route('/ddottylog')
def ddottylog():
    return render_template('ddottylog.html')
@app.route('/feature')
def feature():
    return render_template('feature.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = request.form['content']

    try:
        img_path = upload(file)
        print img_path
        log = DDotty(img_path, content)
        db.session.add(log)
        db.session.commit()

        return "success"
    except:
        return "fail"



#Write
@app.route('/signup', methods = ['GET'])
def sign_up():
    try:
        user_name = request.args.get('user_name')
        googleId = request.args.get('google_id')
        count = db.session.query(User).filter(User.googleId ==googleId).count()
        if count == 0:
            user = User(user_name, googleId, creade_time)
            db.session.add(user)
            db.session.commit()

        user = db.session.query(User).filter(User.googleId == googleId).first()

        return jsonify( success = True, user_id=user.id, user_name = user.name, user_googleId= user.googleId)
    except:
        return jsonify( success = False, user_id=0)

@app.route('/user_update', methods = ['GET'])
def user_update():
    try:
        id = request.args.get('user_id')
        name = request.args.get('name')

        user = db.session.query(User).filter(User.id==id).first()
        user.name = name

        db.session.commit()
        return jsonify( success = True, user_id=id)
    except:
        return jsonify( success = False, user_id="")



#Write
@app.route('/check_favorite_video', methods = ['GET'])
def check_favorite_video():

    try:
        user_id = request.args.get('user_id')
        video_id = request.args.get('video_id')

        video = db.session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
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

        playlist = db.session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
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

        video = db.session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
                                                   Favorite_video.video_id ==video_id)
        count = video.count()
        if count == 0:
            i = Favorite_video(user_id ,video_id)
            db.session.add(i)
            db.session.commit()
            return "success"
        else:
            db.session.query(Favorite_video).filter(Favorite_video.user_id == user_id,
                                                   Favorite_video.video_id ==video_id).delete()
            db.session.commit()
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

        playlist = db.session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
                                                   Favorite_playlist.playlist_id ==playlist_id)
        count = playlist.count()

        if count == 0:
            i = Favorite_playlist(user_id, playlist_id)
            db.session.add(i)
            db.session.commit()
            return "success"
        else:
            db.session.query(Favorite_playlist).filter(Favorite_playlist.user_id == user_id,
                                                   Favorite_playlist.playlist_id ==playlist_id).delete()
            db.session.commit()
            return "duplication"

    except:
        return "fail"


#Send
@app.route('/get_favorite_videolist', methods = ['GET'])
def send_favorite_video():
    user_id = request.args.get('user_id')
    try:
        favorite_video_query = db.session.query(Favorite_video).filter(Favorite_video.user_id==user_id).order_by("id desc")
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
        Favorite_playlist_query = db.session.query(Favorite_playlist).filter(Favorite_playlist.user_id==user_id).order_by("id desc")
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
        cover_list = db.session.query(Home_cover).order_by("id desc").first().video_id

        return jsonify( success = True, cover_list = cover_list)
    except:
        return jsonify( success = False, cover_list = "")


#Send
@app.route('/get_recommend', methods = ['GET'])
def recommend_video():
    try:
        cover_query = db.session.query(Recommend_cover).order_by("id desc").first()
        cover_list = cover_query.video_id

        list_query = db.session.query(Recommend_video).order_by("id desc").first()
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

        db.session.add(video)
        db.session.commit()

        return "success"

    except:
        return "false"



@app.route('/get_ad', methods=['GET'])
def get_ad():
    url = 'https://api.buzzad.io/api/v1/list?unit_id=189665253897479'

    data = json.load(urllib2.urlopen(url))

    if data['code'] != 200:
        return 'error'

    ad_list = data['ads']
    for ad in ad_list:
        reward = int(ad['revenue'] * 0.5)


        if ad['revenue'] > 150 and ad['revenue_type'] == 'cpi':
            reward = 100

        print reward

    return jsonify(ad_list[0])


@app.route('/upload_homecover', methods=['POST'])
def upload_homecover():
    try:
        code = int(request.form['code'])
        video1 = request.form['video1'].split('v=')[1]
        video2 = request.form['video2'].split('v=')[1]
        video3 = request.form['video3'].split('v=')[1]
        video4 = request.form['video4'].split('v=')[1]
        video5 = request.form['video5'].split('v=')[1]

        if code == 378:
            video_str = video1+','+video2+','+video3+','+video4+','+video5
            video = Home_cover(video_str)
            db.session.add(video)
            db.session.commit()
        else:
            return "false"

        return "success"

    except:
        return "false"

@app.route('/upload_recommendcover', methods=['POST'])
def upload_recommedcover():
    try:
        code = int(request.form['code'])
        video1 = request.form['video1'].split('v=')[1]
        video2 = request.form['video2'].split('v=')[1]
        video3 = request.form['video3'].split('v=')[1]
        video4 = request.form['video4'].split('v=')[1]
        video5 = request.form['video5'].split('v=')[1]

        if code == 378:
            video_str = video1+','+video2+','+video3+','+video4+','+video5
            video = Recommend_cover(video_str)
            db.session.add(video)
            db.session.commit()
        else:
            return "false"

        return "success"

    except:
        return "false"
