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
        input = request.form.get("text1")
        #print(str(input))
        #for a in input:
            #print(ord(a))
        try:
            output = analizador(input)
            #print(output)
            return render_template('Analisis.html',input = input,output = output)
        except:
            output = "Se encontro un error del que no se puede recuperar en la entrada."
            return render_template('Analisis.html',input = input,output = output)
    elif request.method == 'GET':
        return render_template('Analisis.html')

if __name__ == '__main__':
    app.run(debug=True)


