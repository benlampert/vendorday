from flask import Flask
from flaskext.mongoengine import MongoEngine
#from mongoengine import connect

#enter mongolab credentials here
#un = 'benlampert'
#pw = 'hannah'

#connect('flasktest', host='mongodb://'+un+':'+pw+'@ds033877.mongolab.com:33877/flasktest')


app = Flask(__name__)
app.config["MONGODB_DB"] = 'vendorDB'
#app.config["MONGO_HOST"] = 'mongodb://'+un+':'+pw+'@ds033877.mongolab.com:33877/flasktest'

db = MongoEngine(app)

def register_blueprints(app):
	#Prevents circular imports
	from views import vendors
	from admin import admin
	app.register_blueprint(vendors)
	app.register_blueprint(admin)

register_blueprints(app)


if __name__ == '__main__':
	app.run()


