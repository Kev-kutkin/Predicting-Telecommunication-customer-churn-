from flask import Flask, render_template, url_for, request
import pandas as pd 
import pickle
from sklearn.ensemble import GradientBoostingClassifier


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('result.html')

@app.route('/predict',methods=['POST'])
def predict():
	def load_models():
		file_name = "models/model_file.p"
		with open(file_name, 'rb') as pickled:
			data = pickle.load(pickled)
			model = data['model']
		return model
	
	features = [float(x) for x in request.form.values()]
	final_features = [np.array(features)]
	final_features = scaler.transform(final_features)  
	model = load_model('churn.pkl')
	prediction = model.predict(final_features)
         

    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	app.run()