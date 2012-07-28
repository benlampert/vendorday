import datetime
from flask import url_for
from tumblelog import db

class Vendor(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	vendorName = db.StringField(max_length=255, required=True)
	slug = db.StringField(max_length=255, required=True)
	vendorFacts = db.StringField(required=True)
	vendorOfferings = db.StringField(required=True)
	vendorKeywords = db.StringField(required=True)
	vendorCategory = db.StringField(required=True)
	contacts = db.EmailField(required=True)
	comments = db.ListField(db.EmbeddedDocumentField('Comment'))
	
	def get_absolute_url(self):
		return url_for('post', kwargs={"slug": self.slug})
		
	def __unicode__(self):
		return self.vendorName
		
	meta = {
		'indexes': ['-created_at', 'slug'],
		'ordering': ['-created_at']
	}
class Category(db.EmbeddedDocument):
	category = db.StringField(verbose_name="Category", required=True)

class Keywords(db.EmbeddedDocument):
	keywords = db.StringField(verbose_name="Keywords", required=True)
	
class Contacts(db.EmbeddedDocument):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	body = db.StringField(verbose_name="Contacts", required=False)
	
class Comment(db.EmbeddedDocument):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	body = db.StringField(verbose_name="Comment", required=True)
	author = db.StringField(verbose_name="Name", max_length=255, required=True)	