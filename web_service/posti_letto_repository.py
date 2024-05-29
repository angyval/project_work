import mysql.connector as driver
from .model import Posto, Specializzazione, Giornata, Regione

#funzione ausiliariaa per ottenere la connessione
def get_connection():
    return driver.connect(
        host="localhost",
        port="3306",
        user="root",
        password=None,
        database="sanita"
    )
def get_posti_by_anno(anno):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = ("SELECT posti_letto.anno, posti_letto.posti_letto, specializzazioni_cliniche.specializzazione_clinica, regioni.nome FROM posti_letto JOIN specializzazioni_cliniche ON posti_letto.id_specializzazione_clinicha=specializzazioni_cliniche.id_specializzazione_clinica JOIN regioni ON posti_letto.id_regione=regioni.id_regione WHERE posti_letto.anno=%s;")
        values = anno,
        cursor.execute(sql, values)
        result = cursor.fetchall()
        posti = []
        for r in result:
            specializzazione = Specializzazione(r[2])
            regione = Regione(r[3])
            posto = Posto(r[0],r[1],regione,specializzazione)
            posti.append(posto)
        return posti
    except Exception as e:
        print(e)
        return None