from myFileReader import MyFileReader
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

fileReader = MyFileReader()

@app.route("/")
def index():
    files = fileReader.getFileDict()

    return render_template("index.html", files=files)


@app.route("/get_file_name")
def getFile():
    return render_template("file_load.html")


@app.route("/load_file", methods = ['POST'])
def loadFile():
    filename = request.form["filename"]
    fileReader.readFile(filename)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
    )
