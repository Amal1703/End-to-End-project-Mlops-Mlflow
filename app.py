from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.stage_06_prediction_new_data import PredictionPipeline


# Pour voir la de index.html excuter le code ci dessous
# index.html est un template géner par le site (bootstrap) :

#app = Flask(__name__) # initializing a flask app

#@app.route('/',methods=['GET'])  # route to display the home page
#def homePage():
#   return render_template("index.html")

#if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080)


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"  # do the training using the web : "http://127.0.0.1:8080/train" => output sur page web "Training Successful!"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST': # POST : Sert à envoyer des données au serveur. Utilisation : formulaire HTML, login / password, envoi de features pour un modèle ML
        try:
            #  reading the inputs given by the user (from web)
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            bathrooms = int(request.form['bathrooms'])
            stories = int(request.form['stories'])
            
            mainroad = str(request.form['mainroad']) 
            guestroom = str(request.form['guestroom']) 
            basement = str(request.form['basement'])   
            hotwaterheating = str(request.form['hotwaterheating'])   
            
            airconditioning = str(request.form['airconditioning'])     
            parking = int(request.form['parking'])    
            prefarea = str(request.form['prefarea'])   
            furnishingstatus = str(request.form['furnishingstatus'])           

            data = [area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]
            
            #data = np.array(data).reshape(1, 12)
            
            obj = PredictionPipeline()
            data_normalized = obj.Normalize_input_data(data)
            predict = obj.predict(data_normalized)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else: # GET : Sert à récupérer des données. Utilisation : afficher une page, récupérer des infos, recherche simple
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)