from appname import create_app
#from tracker import db

app = create_app()

#with app.app_context():
#   db.create_all()

if __name__ == '__main__':
    app.run(debug=True)