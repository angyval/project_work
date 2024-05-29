from .model import Regione, Specializzazione, Posto, Giornata, Popolazione, Giornata1, DatiRegione
from .posti_letto_repository import get_connection
from collections import OrderedDict
#funzione per ottenere dati delle giornate di degenza identificate per Regione
def get_regione_dati(nome,anno):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT regioni.nome, posti_letto.anno, posti_letto.posti_letto, specializzazioni_cliniche.specializzazione_clinica, popolazione.popolazione, giornate.giornate FROM regioni JOIN posti_letto ON regioni.id_regione=posti_letto.id_regione JOIN specializzazioni_cliniche ON posti_letto.id_specializzazione_clinicha=specializzazioni_cliniche.id_specializzazione_clinica JOIN popolazione ON regioni.id_regione=popolazione.id_regione JOIN giornate ON regioni.id_regione=giornate.id_regione WHERE regioni.nome=%s AND posti_letto.anno=%s;"
        values = nome, anno,
        cursor.execute(sql,values)
        result = cursor.fetchall()
        regioni = []
        for r in result:
            posti_letto = Posto(r[1],r[2],r[0],r[3])
            dati_regione = DatiRegione(r[0],r[4],r[5],r[3],posti_letto)
            regioni.append(dati_regione)
        return regioni
    except Exception as e:
        print(e)
        return None