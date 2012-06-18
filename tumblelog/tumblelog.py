from flask import Flask
from flaskext.mongoengine import MongoEngine
from mongoengine import connect

un = ''
pw = ''

connect('tumbleblog_mlab', host='mongodb://'+un+':'+pw+'@ds033877.mongolab.com:33877/flasktest')


app = Flask(__name__)
app.config["MONGODB_DB"] = "flasktest"

db = MongoEngine(app)

def register_blueprints(app):
	#Prevents circular imports
	from views import posts
	from admin import admin
	app.register_blueprint(posts)
	app.register_blueprint(admin)

register_blueprints(app)


if __name__ == '__main__':
	app.run()


