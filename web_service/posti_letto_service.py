from .model import ResponseManager
from .posti_letto_repository import get_posti_by_anno

#funzione di servizio per endpoint "ricerca cliente per id"
def get_posti_by_anno_service(anno):
    db_result = get_posti_by_anno(anno)
    if not db_result:
        return ResponseManager(404, "Posti Not Found")
    serialized_posti = [p.serialize() for p in db_result]
    return serialized_posti