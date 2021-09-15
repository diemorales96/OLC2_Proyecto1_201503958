from flask import Flask, render_template, request,url_for,redirect
from grammar import Analizar as analizador


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Reportes')
def Reportes():
    return render_template('Reportes.html')

@app.route('/Analisis',methods=["POST","GET"])
def Analisis():
    if request.method=="POST":
        global contenido
        contenido = request.form["text1"]
        #print(str(contenido))
        analizador(str(contenido))
        return redirect(url_for("Analisis"))
    else:
        return render_template('Analisis.html')

if __name__ == '__main__':
    app.run(debug=True)


