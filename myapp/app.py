from flask import Flask , render_template, request
import pandas as pd
import pickle
import os

app=Flask(__name__)

def cleaned_data (form_data):
    gestation= float(form_data["gestation"])
    parity=    int(form_data["parity"])
    age=       float(form_data["age"])
    height=    float(form_data["height"])
    weight=    float(form_data["weight"])
    smoke=     float(form_data["smoke"])

    cleaned_data= {
                    "gestation" : [gestation],
                    "parity" : [parity],
                    "age" : [age],
                    "height" : [height],
                    "weight" : [weight],
                    "smoke" : [smoke]
                   }

    return cleaned_data
    




@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")




@app.route("/hello", methods=["GET"])
def hello():
    return "hello world", 200


EXPECTED_COLUMNS=['gestation', 'parity', 'age', 'height', 'weight', 'smoke']


@app.route("/predict", methods=["POST"])
def birth_weight_prediction ():
    #baby_data=request.form
    baby_data_form= request.get_json()



    #baby_data_cleaned= cleaned_data(baby_data)

    data_dataframe= pd.DataFrame(baby_data_form)
    data_dataframe= data_dataframe[EXPECTED_COLUMNS]

    model_path= os.path.join(os.path.dirname(__file__),"model.pkl")
    with open (model_path, "rb")as obj:
        model=pickle.load(obj)

        prediction=model.predict(data_dataframe)

        prediction= round(float(prediction),2)

        response= {"prediction" : prediction}

        #return render_template("index.html", prediction= prediction)
        return response, 200



if __name__=="__main__":
    app.run(debug=True)