from flask import Flask, render_template, url_for, request, session, flash, redirect

# Importing all of the Blueprint objects into the application
from flask_wtf.csrf import CSRFProtect
from modules.build_substring import BuildSubstringGoogle, BuildSubstringYandex, BuildSubstringBing, NERDString

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
	return render_template('general_templates/dashboard.html', form=form, title = 'Dork Console Dashboard')

# Routing
@app.route("/post_dork_inputs", methods=['POST'])
def post_dork_inputs():

	import re

	form_data_dict = {
		'root_terms': request.form.get('root_terms'),
		'start_date': request.form.get('start_date'),
		'end_date': request.form.get('end_date'),
		'filetypes': request.form.getlist('filetypes'),
		'moreterms': request.form.getlist('moreterms'),
		'filterwords': request.form.getlist('filterwords')

	}

	ns = NERDString(form_data_dict['root_terms'])

	form_data_dict['root_terms'] = re.split('[,;:]', form_data_dict['root_terms'])
	form_data_dict['persons'] = ns.data['persons']
	form_data_dict['orgs'] = ns.data['orgs']
	form_data_dict['gpe'] = ns.data['gpe']
	form_data_dict['moreterms'] = [x.strip() for x in re.split('[,;:]', form_data_dict['moreterms'][0].replace('\r', '\n').replace('\n', ', '))]
	form_data_dict['filterwords'] = [x.strip() for x in re.split('[,;:]', form_data_dict['filterwords'][0].replace('\r', '\n').replace('\n', ', '))]


	bsg = BuildSubstringGoogle(form_data_dict)
	bsy = BuildSubstringYandex(form_data_dict)
	bsb = BuildSubstringBing(form_data_dict)

	search_links_dict = {
		"google": {
			"link": bsg.build_search_link(),
			"query": bsg.q
		},
		"yandex": {
			"link": bsy.build_search_link(),
			"query": bsy.q
		},
		"bing": {
			"link": bsb.build_search_link(),
			"query": bsb.q
		}
	}

	#bs = BuildSubstringGoogle(form_data_dict)

	# return form_data_dict
	# return  bs.q
	# return redirect(url_for('results', search_links = search_links_dict))
	# return search_links_dict
	return render_template('general_templates/results2.html', title = 'Results', results=search_links_dict)

@app.route("/results", methods=['POST', 'GET'])
def results():
	import json

	# convert string representation of dictionary to actual dictionary
	search_links = request.args.get('search_links')
	json_acceptable_string = search_links.replace("'", "\"")
	search_links_dict = json.loads(json_acceptable_string)

	return render_template('general_templates/results.html', title = 'Results', results=search_links_dict)

# References
@app.route("/about")
def about():
	return render_template('general_templates/about.html', title = 'About')

@app.route("/quicksearch")
def quicksearch():

	form = QuicksearchForm()

	return render_template('general_templates/quicksearch.html', form = form, title = 'Quicksearch')

#Routing
@app.route("/post_q", methods=['POST', 'GET'])
def post_q():

	# from modules.build_substring import BuildSubstring
	import re

	form_data_dict = {
		'q': request.form.get('q')}

	ns = NERDString(form_data_dict['q'])

	form_data_dict['root_terms'] = re.split('[,;:]', form_data_dict['q'])
	form_data_dict['persons'] = ns.data['persons']
	form_data_dict['orgs'] = ns.data['orgs']
	form_data_dict['gpe'] = ns.data['gpe']
	form_data_dict['start_date'] = ns.data['min_date']
	form_data_dict['end_date'] = ns.data['max_date']
	form_data_dict['urls'] = ns.data['urls']
	form_data_dict['filetypes'] = ns.data['filetypes']
	form_data_dict['moreterms'] = []
	form_data_dict['filterwords'] = []

	bsg = BuildSubstringGoogle(form_data_dict)
	bsy = BuildSubstringYandex(form_data_dict)
	bsb = BuildSubstringBing(form_data_dict)

	search_links_dict = {
		"google": {
			"link": bsg.build_search_link(),
			"query": bsg.q
		},
		"yandex": {
			"link": bsy.build_search_link(),
			"query": bsy.q
		},
		"bing": {
			"link": bsb.build_search_link(),
			"query": bsb.q
		}
	}

	# pass
	# return ns.data
	# return search_links_dict
	# return redirect(url_for('results2.html', search_links = search_links_dict))
	return render_template('general_templates/results2.html', title = 'Results', results=search_links_dict)


if __name__ == '__main__':
	app.run(debug = True, threaded = True)