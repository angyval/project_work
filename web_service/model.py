#classe di modellazione oggetti di tipo Posti Letto
class Posto:
    #metodo inizializzazione
    def __init__(self,anno,posti_letto, regione=None, specializzazione_clinica=None):
        self.anno = anno
        self.posti_letto = posti_letto
        self.regione = regione
        self.specializzazione_clinica = specializzazione_clinica

    # metodo di serializzazione (da Posto a json)
    def serialize(self):
        return {
            "anno": self.anno,
            "posti_letto":self.posti_letto,
            "regione":self.regione.serialize_regione_for_posto(),
            "specializzazione_clinica":self.specializzazione_clinica.serialize_specializzazione_for_posto()
        }
#classe di modellazione oggetti di tipo Regione
class Regione:
    def __init__(self,nome):
        self.nome = nome

    #metodo di serializzazione (da Regione a json)
    def serialize_regione_for_posto(self):
        return self.__dict__
#classe di modellazione oggetti di tipo Specializzazione
class Specializzazione:
    def __init__(self,specializzazione_clinica):
        self.specializzazione_clinica = specializzazione_clinica

    #metodo di serializzazione (da Regione a json)
    def serialize_specializzazione_for_posto(self):
        return self.__dict__
#classe di modellazione oggetti di tipo Specializzazione
class Giornata:
    #metodo inizializzazione
    def __init__(self, anno, giornate, specializzazione_clinica=None,regione=None):
        self.anno = anno
        self.giornate = giornate
        self.specializzazione_clinica = specializzazione_clinica
        self.regione = regione
    #metodo di serializzazione per giornate
    def serialize_giornate_for_posto(self):
        return {
            "anno":self.anno,
            "giornate":self.giornate,
            "specializzazione_clinica": self.specializzazione_clinica.serialize_specializzazione_for_posto(),
            "regione": self.regione.serialize_regione_for_posto()
        }
class Giornata1:
    # metodo inizializzazione
    def __init__(self, giornate):
        self.giornate = giornate

    def serialize_giornate(self):
        return {
            "giornate":self.giornate
        }

class Popolazione:
    def __init__(self,popolazione):
        self.popolazione = popolazione

    #metodo di serializzazione (da Regione a json)
    def serialize_popolazione(self):
        return self.__dict__

class DatiRegione:
    #metodo inizializzazione
    def __init__(self,nome,popolazione,giornate,specializzazione,posto):
        self.nome = nome
        self.popolazione = popolazione
        self.giornate = giornate
        self.specializzazione = specializzazione
        self.posto = posto

        # metodo di serializzazione (da Posto a json)
    def serialize_dati_regione(self):
        return {
            "regione": self.nome.serialize_regione_for_posto(),
            "popolazione": self.popolazione.serialize_popolazione(),
            "giornate": self.giornata1.serialize_giornate(),
            "specializzazione": self.specializzazione.serialize_specializzazione_for_posto(),
            "posto": self.posto.serialize()
        }
#classe di gestione delle risposte
class ResponseManager:
    def __init__(self,code,message):
        self.code = code
        self.message = message

    def serialize(self):
        return self.__dict__