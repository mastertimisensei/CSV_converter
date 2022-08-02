from flask import Flask, render_template,request, Response
from csv_conveter import csv_converter, Error

app = Flask(__name__)




@app.route("/", methods = ["POST","GET"])
def getCSV():
    if request.method == 'POST':
        filepath = request.form.get('file_input')
        csv = csv_converter(filepath)
        try:
            if csv == 1 or len(csv) == 0:
                raise Error
        except:
            return "Invalid File or File Input not in correct format"
        return_value =  Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myoutput.csv"})
        return return_value
    return render_template("layout.html")


if __name__ == '__main__':
    app.run(debug=True, port = 8000, host ="0.0.0.0")