from flask import Flask
from flaskext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_DB"] = "my_tumble_log"

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


