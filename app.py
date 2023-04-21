from flask import Flask, render_template, url_for, request, session, flash, redirect
# from ocr import ocr
# from ner import ner
# from summarization import summ

# Importing all of the Blueprint objects into the application
from flask_wtf.csrf import CSRFProtect
from modules.build_substring import BuildSubstring

from forms import UserInputAP, UserInput

# from models import User

class Config(object):
	SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

app = Flask(__name__)
app.config.from_object(Config)
# app.secret_key = "mastadon"
# app.config['UPLOAD_FOLDER'] = './uploads'
# app.config['DATA_FOLDER'] = './application_data'

#csrf = CSRFProtect(app)

# Registering all Blueprints (makes them available application)
# app.register_blueprint(ner, url_prefix="")
# app.register_blueprint(ocr, url_prefix="")
# app.register_blueprint(summ, url_prefix="")

# Routing
@app.route("/")
@app.route("/home")
def landing():
	return render_template('general_templates/landing_page.html', title = 'testsiala')

# Routing
@app.route("/dashboard")
def dashboard():

	form = UserInput()

	return render_template('general_templates/dashboard.html', form = form, title = 'Title')

@app.route("/dashboard-ap")
def dashboardAP():
	form = UserInputAP()
	return render_template('general_templates/dashboard-ap.html', form=form, title = 'aaixlsop')

# Routing
@app.route("/post_dork_inputs", methods=['POST'])
def post_dork_inputs():

	form_data_dict = {
		'root_terms': request.form.get('entity'),
		'start_date': request.form.get('startdate'),
		'end_date': request.form.get('enddate'),
		'filetypes': request.form.get('doc_type'),
		'search_engines': request.form.get('search_engines')
	}

	bs = BuildSubstring(form_data_dict)

	#return form_data_dict
	#return { "test" :str(type(bs.build_full_string()))}
	return bs.build_search_engine_strings()
	# return render_template('general_templates/dashboard-ap.html', title = 'resuls', form=form, results=bs.build_full_string())

# References
@app.route("/about")
def about():
	return render_template('general_templates/references.html', title = 'aabbbs')



if __name__ == '__main__':
	app.run(debug = True, threaded = True)