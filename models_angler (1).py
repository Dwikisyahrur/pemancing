from datetime import datetime

class Angler:
    def __init__(self, name="Dwiki"):
        self.name = name

    def log_catch(self, fish, location="Sungai", date=None):
        date = date or datetime.now().strftime("%Y-%m-%d")
        return {
            "pemancing": self.name,
            "jenis_ikan": fish.species,
            "berat": fish.weight,
            "umpan": fish.bait,
            "lokasi": location,
            "tanggal": date,
            "cuaca": "Cerah",
            "waktu": "Pagi hari",
            "catatan": "Ikan ditangkap dekat batu besar."
        }
