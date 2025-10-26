from flask import Flask, render_template, request



app= Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("csv_file.html")




@app.route("/upload", methods=["POST"])
def get_file():
    file=request.files["file"]
    
    if file.filename.endswith(".csv"):
        
        path= "myapp/userfile/" + file.filename
        file.save(path)
        return "we have received your csv file successfully"
    
    else:
        return "please upload a csv file only"




if __name__=="__main__":
    app.run(debug=True)




