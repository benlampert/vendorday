from flask import Flask
from flaskext.mongoengine import MongoEngine
from mongoengine import connect

connect('tumbleblog_mlab', host='mongodb://benlampert:hannah@ds033877.mongolab.com:33877/flasktest')

#mongodb://benlampert:hannah24@ds033877.mongolab.com:33877/flasktest

app = Flask(__name__)
app.config["MONGODB_DB"] = "flasktest"

db = MongoEngine(app)
#db = mongoengine.connect('flasktest', host='ds033877.mongolab.com:33877', username='benlampert', password='hannah24')

def register_blueprints(app):
	#Prevents circular imports
	from views import posts
	from admin import admin
	app.register_blueprint(posts)
	app.register_blueprint(admin)

register_blueprints(app)


if __name__ == '__main__':
	app.run()


