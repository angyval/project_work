from .model import ResponseManager
from .giornate_degenza_repository import get_giornate_regione

#funzione di servizio per endpoint "ricerca cliente per id"
def get_giornate_by_regione_service(nome):
    db_result = get_giornate_regione(nome)
    if not db_result:
        return ResponseManager(404, "Giornate Not Found")
    serialized_giornate = [g.serialize_giornate_for_posto() for g in db_result]
    return serialized_giornate