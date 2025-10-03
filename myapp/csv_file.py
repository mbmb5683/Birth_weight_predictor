from flask import Flask, render_template, request



app= Flask (__name__)
@app.route("/", methods=["GET"])
def csv_file ():
    return render_template("csv_file.html")

@app.route("/csv", methods=["POST"])
def access_csv ():
    file=request.files["file"]

    if file.filename.endswith(".csv"):
        path= "myapp/userfile/" + file.filename

        file.save(path)
        return "we received your csv file"

    else:
        return ({"msg" : "upload only csv file"})



if __name__=="__main__":
    app.run(debug=True)