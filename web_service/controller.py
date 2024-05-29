from flask import Flask
import service

#inizializzazione applicazione Flask
app = Flask(__name__)
#endpoint ·1: ricerca Posti Letto per anno localhost:5000/postiletto/get/<anno>
@app.get("/postiletto/get/<string:anno>")
def get_postiletto_by_anno(anno):
    response = service.get_posti_by_anno_service(anno)
    if not isinstance(response, list):
        return response.serialize(), response.code
    return response, 200

#endpoint ·2: ricerca giornate degenza per regione localhost:5000/giornatedegenza/get/<regione>
@app.get("/giornatedegenza/get/<string:nome>")
def get_giornatedegenza_by_regione(nome):
    response = service.get_giornate_by_regione_service(nome)
    if not isinstance(response, list):
        return response.serialize(), response.code
    return response, 200

#endpoint ·2: ricerca dati per regione localhost:5000/dati/get/<regione>
@app.get("/dati/get/<string:nome>/<string:anno>")
def get_dati_by_regione(nome,anno):
    response = service.get_regioni_dati_service(nome,anno)
    if not isinstance(response, list):
        return response.serialize(), response.code
    return response, 200
#eseguibilità script
if __name__=="__main__":
    app.run()