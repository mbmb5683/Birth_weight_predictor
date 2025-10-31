from flask import Flask , render_template, request
import pandas as pd
import pickle


#create flask app
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
    


#this is render my homepage of my predict url
@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")



#this route is made for prediction of baby's birth weight....

@app.route("/predict", methods=["POST"])
def birth_weight_prediction ():
    baby_data=request.form

    #cleaning the user data from string to float or int in function cleaned_data
    baby_data_cleaned= cleaned_data(baby_data)

    #convert user data into dataframe
    data_dataframe= pd.DataFrame(baby_data_cleaned)


    #load machine learning trained model
    with open ("myapp/model/model.pkl" , "rb")as obj:
        model=pickle.load(obj)

    #make prediction on user data
    prediction=model.predict(data_dataframe)
    prediction= round(float(prediction),2)

    #return response in json format
    
    return render_template("index.html", prediction= prediction)
    
    


if __name__=="__main__":
    app.run(debug=True)