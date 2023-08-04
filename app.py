from flask import Flask, request, render_template
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app = application

# Route for a home page

@app.route('/')
def index():
    image_filename = "welcomeimage.jpeg"
    return render_template('index.html', image_filename=image_filename)

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))


        )

        pred_df=data.get_data_as_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
#About page which has complete imformation about project
@app.route('/about')
def about():
    image_filename = "images.avif"
    return render_template('about.html', image_filename=image_filename)    

@app.route('/portfolio')
def portfolio():
    image_filename = "img1.png"
    return render_template('portfolio.html', image_filename=image_filename)



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
