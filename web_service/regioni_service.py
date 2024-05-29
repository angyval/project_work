from .model import ResponseManager
from .regioni_repository import get_regione_dati

#funzione di servizio per endpoint "ricerca cliente per id"
def get_regioni_dati_service(nome,anno):
    db_result = get_regione_dati(nome,anno)
    if not db_result:
        return ResponseManager(404, "Regione Not Found")
    serialized_regione = [r.serialize_dati_regione() for r in db_result]
    return serialized_regione
