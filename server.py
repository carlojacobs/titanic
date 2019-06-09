# Titanic prediction app
import tensorflow as tf # Machine learning
from tensorflow.python import keras # Machine learing
from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)

print(tf.__version__)

# Loading the model
loaded_model = keras.models.load_model("94_model.h5")

graph = tf.compat.v1.get_default_graph()

def make_prediction(data):

	# Reshape the data a bit
	data = np.array([data])

	global graph
	with graph.as_default():
		prediction = loaded_model.predict(data)
		return prediction



def validate_from(form_data):
	keys = []
	for key, value in form_data.items():
		if form_data[key] == '':
			keys.append(key)
	return keys

def prepare_form_data(form_data):
	final_data = []
	pclass = form_data["class"]
	ticket = 0
	if pclass == 0:
		ticket = 60
	elif pclass == 1:
		ticket = 40
	elif pclass == 2:
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
  return render_template("index2.html", nameIsvalid=True, ageIsvalid=True, genderIsvalid=True, sibsIsvalid=True, parsIsvalid=True, embarkedIsvalid=True, classIsvalid=True)

def is_item_in_list(list, item):
	if item in list:
		return False
	else:
		return True

@app.route("/predict", methods=["POST"])
def predict():
	# Check for correct protocol
	if not request.method == 'POST':
		return "<h1>Invalid request</h1>"

	# Get formdata
	form_data = dict(request.form)

	print("FORMDATA: ", form_data)

	# Validate form
	validation_keys = validate_from(form_data)
	print("VALKEYS: ", validation_keys)
	if len(validation_keys) > 0:
		nameIsvalid = is_item_in_list(validation_keys, 'name')
		ageIsvalid = is_item_in_list(validation_keys, 'age')
		genderIsvalid = is_item_in_list(validation_keys, 'gender')
		sibsIsvalid = is_item_in_list(validation_keys, 'sibs')
		parsIsvalid = is_item_in_list(validation_keys, 'pars')
		embarkedIsvalid = is_item_in_list(validation_keys, 'embarked')
		classIsvalid = is_item_in_list(validation_keys, 'class')
		return render_template("index2.html", nameIsvalid=nameIsvalid, ageIsvalid=ageIsvalid, genderIsvalid=genderIsvalid, sibsIsvalid=sibsIsvalid, parsIsvalid=parsIsvalid, embarkedIsvalid=embarkedIsvalid, classIsvalid=classIsvalid)

	print("FORMDATA", form_data)

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

	return render_template("result2.html", result=result, color=color, message=message, good=good, meh=meh, sad=sad)

if __name__ == "__main__":
	app.run(debug=True)
