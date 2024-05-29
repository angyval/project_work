from .model import Giornata, Regione, Specializzazione
from .posti_letto_repository import get_connection

#funzione per ottenere dati delle giornate di degenza identificate per Regione
def get_giornate_regione(nome):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT giornate.anno, giornate.giornate, regioni.nome, specializzazioni_cliniche.specializzazione_clinica FROM giornate JOIN regioni ON giornate.id_regione=regioni.id_regione JOIN specializzazioni_cliniche ON giornate.id_specializzazione_clinicha=specializzazioni_cliniche.id_specializzazione_clinica WHERE regioni.nome=%s;"
        values = nome,
        cursor.execute(sql,values)
        result = cursor.fetchall()
        giornate = []
        for r in result:
            specializzazione = Specializzazione(r[3])
            regione = Regione(r[2])
            giornata = Giornata(r[0], r[1], specializzazione, regione)
            giornate.append(giornata)
        return giornate
    except Exception as e:
        print(e)
        return None