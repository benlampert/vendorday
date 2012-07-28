from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from models import *
from flaskext.mongoengine.wtf import model_form

vendors = Blueprint('vendors', __name__, template_folder='templates')


#this class is for the main dashboard views
class ListView(MethodView):
		
	def get(self):
		allVendors = Vendor.objects.all()
		recents = Vendor.objects.all().order_by('-created_at').limit(3)
		mostCommented = Vendor.objects.all().order_by('-comments').limit(3)

		#put all the vendor list views into one dict to pass into the template
		vendors = {
		'all':allVendors, 
		'recents':recents,
		'commented':mostCommented}
		
		return render_template('vendors/list.html', vendors = vendors)

class BrowseView(MethodView):

	def get(self):
		#query for all the vendors sorted by Vendor Name
		allVendorsSorted = Vendor.objects.all().order_by('vendorName')

		vendors = {
		'allSorted':allVendorsSorted}
		
		return render_template('vendors/browse.html', vendors = vendors)
	

		
class DetailView(MethodView):

	form = model_form(Comment, exclude=['created_at'])
	
	def get_context(self, slug):
		vendor = Vendor.objects.get_or_404(slug=slug)
		form = self.form(request.form)
		
		context = {
			"vendor": vendor,
			"form": form
		}
		return context
	
	
	def get(self, slug):
		context = self.get_context(slug)
		return render_template('vendors/detail.html', **context)

	def post(self, slug):
		context = self.get_context(slug)
		form = context.get('form')
		
		if form.validate():
			comment = Comment()
			form.populate_obj(comment)
			
			vendor = context.get('vendor')
			vendor.comments.append(comment)
			vendor.save()
			
			return redirect(url_for('vendors.detail', slug=slug))
		
		return render_template('vendors/detail.html', **context)

#Register the urls
vendors.add_url_rule('/', view_func=ListView.as_view('list'))
vendors.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
vendors.add_url_rule('/browse/', view_func=BrowseView.as_view('browse'))