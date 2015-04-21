


from app import app, init_db

#df

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')