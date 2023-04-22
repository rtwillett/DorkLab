from flask import Flask, render_template, url_for, request, session, flash, redirect

# Importing all of the Blueprint objects into the application
from flask_wtf.csrf import CSRFProtect
from modules.build_substring import BuildSubstring, NERDString

from forms import UserInput, QuicksearchForm

class Config(object):
	SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

app = Flask(__name__)
app.config.from_object(Config)

#csrf = CSRFProtect(app)

# Routing
# @app.route("/dashboard")
@app.route("/")
@app.route("/home")
def home():
	form = UserInput()
	return render_template('general_templates/dashboard.html', form=form, title = 'aaixlsop')

# Routing
@app.route("/post_dork_inputs", methods=['POST'])
def post_dork_inputs():

	import re

	form_data_dict = {
		'root_terms': request.form.get('root_terms'),
		'start_date': request.form.get('start_date'),
		'end_date': request.form.get('end_date'),
		'filetypes': request.form.getlist('filetypes')
		# 'search_engines': request.form.getlist('search_engines')
	}

	ns = NERDString(form_data_dict['root_terms'])

	form_data_dict['root_terms'] = re.split('[,;:]', form_data_dict['root_terms'])
	form_data_dict['persons'] = ns.data['persons']
	form_data_dict['orgs'] = ns.data['orgs']
	form_data_dict['gpe'] = ns.data['gpe']
	
	# form_data_dict['filetypes'] = form_data_dict['filetypes'].split()

	bs = BuildSubstring(form_data_dict)

	# return form_data_dict
	return  bs.q
	# return render_template('general_templates/dashboard.html', title = 'Results', results=search_links_dict)

# References
@app.route("/about")
def about():
	return render_template('general_templates/references.html', title = 'aabbbs')

@app.route("/quicksearch")
def quicksearch():

	form = QuicksearchForm()

	return render_template('general_templates/quicksearch.html', form = form, title = 'Quicksearch')

#Routing
@app.route("/post_q", methods=['POST'])
def post_q():

	from modules.build_substring import BuildSubstring

	form_data_dict = {
		'q': request.form.get('q')}

	ns = NERDString(form_data_dict['q'])


	# pass
	return ns.data
	# return form_data_dict

if __name__ == '__main__':
	app.run(debug = True, threaded = True)