# Titanic prediction app
import tensorflow as tf # Machine learning
from tensorflow import keras # Machine learing
from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)

# Loading the model
loaded_model = keras.models.load_model("94_model.h5")

graph = tf.get_default_graph()

def make_prediction(data):

	# Reshape the data a bit
	data = np.array([data])

	global graph
	with graph.as_default():
		prediction = loaded_model.predict(data)
		return prediction



def validate_from(form_data):
	for key, value in form_data.items():
		if form_data[key] == '':
			return False
	return True

def prepare_form_data(form_data):
	final_data = []
	pclass = form_data["class"]
	ticket = 0
	if pclass == 1:
		ticket = 60
	elif pclass == 2:
		ticket = 40
	elif pclass == 3:
		ticket = 7

	final_data.append(pclass)
	final_data.append(int(form_data["gender"]))
	final_data.append(int(form_data["age"]))
	final_data.append(int(form_data["sibs"]))
	final_data.append(int(form_data["pars"]))
	final_data.append(ticket)
	final_data.append(int(form_data["embarked"]))

	print(final_data)

	return final_data

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
	# Check for correct protocol
	if not request.method == 'POST':
		return "<h1>Invalid request</h1>"

	# Get formdata
	form_data = dict(request.form)

	# Validate form
	if not validate_from(form_data):
		return "<h1>Oops! You didn't fill in the entire form!</h1>"

	data = prepare_form_data(form_data)
	prediction = make_prediction(data)[0][0]

	print(prediction)

	result = np.round(100*prediction)
	color = ""
	message = ""
	good = False
	meh = False
	sad = False

	name = form_data["name"].split(' ')[0]

	if prediction > 0.6:
		color = "#7FFF00"
		message = f'Congratz {name}! It looks like you would survive this horrible disaster.'
		good = True
	elif prediction >= 0.5 and prediction <= 0.6:
		color = "orange"
		message = f'Oh... Well, try and hold your breath {name}!'
		status = "meh"
		meh = True
	elif prediction < 0.5:
		color = "red"
		message = f'{name}, this is just sad... :('
		status = "sad"
		sad = True

	return render_template("result.html", result=result, color=color, message=message, good=good, meh=meh, sad=sad)

if __name__ == "__main__":
	app.run(debug=True)
