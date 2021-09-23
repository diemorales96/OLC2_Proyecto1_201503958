from flask import Flask, render_template, request,url_for,redirect
from grammar import Analizar as analizador
import os, webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Reportes',methods =["POST","GET"])
def Reportes():
    return render_template('Reportes.html')

@app.route('/TablaSimbolos',methods =["POST","GET"])
def TablaSimbolos():
    return render_template('TablaSimbolos.html') 

@app.route('/Arbol',methods =["POST","GET"])

def Arbol():
    webbrowser.open('file://' + os.path.realpath("ast.svg"))
    return render_template('home.html')    

@app.route('/Analisis',methods=["POST","GET"])
def Analisis():
    if request.method=="POST":
        input = request.form.get("text1") 
        try:
            output = analizador(input)
            return render_template('Analisis.html',input = input,output = output)
        except:
            output = "Se encontro un error del que no se puede recuperar en la entrada."
            return render_template('Analisis.html',input = input,output = output)
    elif request.method == 'GET':
        return render_template('Analisis.html')

if __name__ == '__main__':
    app.run(debug=True)


