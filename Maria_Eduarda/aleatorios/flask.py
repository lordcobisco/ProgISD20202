from flask import Flask

app=Flask(__name__)

#Só executa a aplicação se for a aplicação principal
@app.route("/") #caminho da rota
def index():
    return "Duda no Flask!"
if __name__=='__main__':
    app.run()
