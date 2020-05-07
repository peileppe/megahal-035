import pickle

from megahal import MegaHAL
from twitterhal.database import RedisDatabase

megahal_kwargs = {
    "banwords": ["ALDRIG", "ALLA", "ALLT", "ALLTID", "ALLTSÅ", "ANDERS", "ANDRA", "ANNAN", "ANNAN", "ANSER", "ATT",
                 "AV", "BAKOM", "BARA", "BARN", "BEHÖVA", "BERÄTTA", "BILD", "BLAND", "BLI", "BLI", "BLIVA", "BORDE",
                 "BORT", "BRA", "BÄSTA", "BÄTTRE", "BÅDA", "BÅDE", "BÖR", "BÖRJA", "BÖRJAN", "DAG", "DEL", "DENNA",
                 "DENNA", "DESSUTOM", "DETTA", "DOCK", "DOM", "DÄR", "DÄRFÖR", "DÅ", "EFTER", "EFTERSOM", "EGEN",
                 "EGENTLIGEN", "EGNA", "ELLER", "ENDA", "ENLIGT", "EXEMPEL", "FALL", "FAST", "FEM", "FINNAS",
                 "FINNAS", "FLER", "FLERA", "FLESTA", "FOLK", "FORTFARANDE", "FRAM", "FRAMFÖR", "FRÅGA", "FRÅGA",
                 "FRÅN", "FYRA", "FÅ", "FÖR", "FÖRE", "FÖRRA", "FÖRST", "FÖRST", "GAMMAL", "GE", "GE", "GENOM",
                 "GÄLLER", "GÅ", "GÅ", "GÅNG", "GÅTT", "GÖR", "GÖRA", "GÖRA", "GÖRA", "HA", "HA", "HAFT", "HAND",
                 "HANDLA", "HEL", "HELLER", "HELT", "HEM", "HOS", "HUR", "HÄR", "HÅLLA", "HÅLLA", "I", "IBLAND",
                 "IGEN", "IN", "INFÖR", "INGA", "INGEN", "INGET", "INNAN", "INNEBÄR", "INOM", "INTE", "JA",
                 "JOHANSSON", "JU", "JUST", "KANSKE", "KL.", "KLAR", "KOMMA", "KOMMA", "KOMMA", "KOMMA", "KRONA",
                 "KUNNA", "KUNNA", "KUNNA", "KVAR", "KVINNA", "KÄNNA", "LANDET", "LARS", "LIGGER", "LIKA", "LITE",
                 "LITEN", "LITEN", "LIV", "LÄNGE", "LÄTT", "LÅG", "LÅNG", "LÅNGT", "MAN", "MED", "MEDAN", "MELLAN",
                 "MEN", "MENA", "MER", "MEST", "MILJON", "MINST", "MOT", "MYCKET", "MÄNNISKOR", "MÅL", "MÅNGA",
                 "MÅSTE", "NEJ", "NER", "NOG", "NU", "NY", "NY", "NYTT", "NÄR", "NÄSTA", "NÄSTAN", "NÅGON", "NÅGOT",
                 "OCH", "OCKSÅ", "OFTA", "OLIKA", "OM", "OSS", "PAR", "PENGAR", "PER", "PLATS", "PROBLEM", "PROCENT",
                 "PÅ", "REDAN", "REGERING", "RIKTIG", "RUNT", "RÄTT", "SA", "SADE", "SAMMA", "SAMT", "SAMTIDIGT",
                 "SATT", "SE", "SEDAN", "SENARE", "SENAST", "SER", "SETT", "SIDA", "SIG", "SIN", "SIN", "SIST",
                 "SJÄLV", "SJÄLV", "SKA", "SKA", "SKOLA", "SMÅ", "SOM", "STOR", "STOR", "STOR", "STOR", "STÄLLET",
                 "STÅ", "STÅR", "SVENSK", "SVENSKA", "SVERIGE", "SVÅR", "SÄGA", "SÄGA", "SÄRSKILD", "SÄTT", "SÅ",
                 "SÅG", "TA", "TAR", "TID", "TID", "TIDIG", "TILL", "TILLBAKA", "TILLSAMMANS", "TIO", "TOG", "TRO",
                 "TROTS", "TYCKER", "UNDER", "UPP", "UR", "USA", "UT", "UTAN", "UTANFÖR", "VAD", "VARA", "VARFÖR",
                 "VARJE", "VETA", "VID", "VIDARE", "VILJA", "VILJA", "VILKET", "VISA", "VÄG", "VÄL", "VÄRLDEN",
                 "YTTERLIGARE", "ÄN", "ÄNDÅ", "ÄNNU", "ÄR", "ÄTA", "ÄVEN", "ÅR", "ÅR", "ÖVER"],
    "auxwords": ["DE", "DEM", "DEN", "DERAS", "DESS", "DET", "DIG", "DIN", "DINA", "DITT", "DU", "EN", "ER", "ERA",
                 "ERT", "ETT", "HAN", "HANS", "HENNE", "HENNES", "HON", "HONOM", "JAG", "MIG", "MIN", "MINA",
                 "MITT", "NI", "OSS", "TRE", "TVÅ", "VI", "VÅR", "VÅRA", "VÅRT"],
    "swapwords": {"DIG": "MIG", "DINA": "MINA", "DITT": "MITT", "DU": "JAG", "ER": "OSS", "ERA": "VÅRA",
                  "ERT": "VÅRT", "JAG": "DU", "MIG": "DIG", "MIN": "DIN", "MINA": "DINA", "MITT": "DITT",
                  "NI": "VI", "OSS": "ER", "VI": "NI", "VÅR": "ER", "VÅRA": "ERA", "VÅRT": "ERT"},
}

db = RedisDatabase(pickle_protocol=pickle.HIGHEST_PROTOCOL, namespace="megahal", db=3)

hal = MegaHAL(timeout=5, db=db, **megahal_kwargs)
hal.interact()
hal.close()
