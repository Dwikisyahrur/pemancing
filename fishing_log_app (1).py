import json
from abc import ABC, abstractmethod
from datetime import datetime
import os

# === Abstract Class ===
class Animal(ABC):
    @abstractmethod
    def describe(self):
        pass

# === Fish Class (inherits Animal) ===
class Fish(Animal):
    def __init__(self, species, weight, bait):
        self.species = species
        self.weight = weight
        self.bait = bait

    def describe(self):
        return f"{self.species} ({self.weight} kg), umpan: {self.bait}"

# === Angler Class ===
class Angler:
    def __init__(self, name):
        self.name = name
        self.catch_log = []

    def log_catch(self, fish, location, date=None):
        date = date or datetime.now().strftime("%Y-%m-%d")
        entry = {
            "name": self.name,
            "species": fish.species,
            "weight": fish.weight,
            "bait": fish.bait,
            "location": location,
            "date": date
        }
        self.catch_log.append(entry)
        return entry

# === Fishing Log ===
class FishingLog:
    def __init__(self, filename="data/log.json"):
        self.filename = filename
        self.entries = []
        self.load()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w") as f:
            json.dump(self.entries, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            self.entries = []

    def show_all(self):
        if not self.entries:
            print("Belum ada catatan mancing.")
            return
        for i, entry in enumerate(self.entries, 1):
            print(f"[{i}] {entry['date']} - {entry['name']} menangkap {entry['species']} ({entry['weight']} kg) di {entry['location']}, umpan: {entry['bait']}")

    def show_stats(self):
        if not self.entries:
            print("Belum ada data untuk statistik.")
            return
        total_ikan = len(self.entries)
        total_berat = sum(float(entry['weight']) for entry in self.entries)
        lokasi_counter = {}
        for entry in self.entries:
            lokasi = entry['location']
            lokasi_counter[lokasi] = lokasi_counter.get(lokasi, 0) + 1

        print(f"\nTotal tangkapan: {total_ikan} ikan")
        print(f"Total berat: {total_berat:.2f} kg")
        print("Tangkapan per lokasi:")
        for lokasi, jumlah in lokasi_counter.items():
            print(f"- {lokasi}: {jumlah} ikan")

# === CLI App ===
class FishingApp:
    def __init__(self):
        self.log = FishingLog()

    def menu(self):
        while True:
            print("\n=== Fishing Log Menu ===")
            print("1. Tambah Catatan Mancing")
            print("2. Lihat Semua Catatan")
            print("3. Lihat Statistik")
            print("4. Keluar")
            pilihan = input("Pilih menu (1/2/3/4): ")
            if pilihan == "1":
                self.tambah_catatan()
            elif pilihan == "2":
                self.log.show_all()
            elif pilihan == "3":
                self.log.show_stats()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan Fishing Log!")
                break
            else:
                print("Pilihan tidak valid.")

    def tambah_catatan(self):
        try:
            name = input("Nama pemancing: ")
            species = input("Jenis ikan: ")
            weight = float(input("Berat (kg): "))
            bait = input("Umpan yang digunakan: ")
            location = input("Lokasi mancing: ")

            fish = Fish(species, weight, bait)
            angler = Angler(name)
            entry = angler.log_catch(fish, location)
            self.log.add_entry(entry)
            print("Catatan berhasil ditambahkan!")
        except ValueError:
            print("Input tidak valid. Berat harus berupa angka.")

if __name__ == "__main__":
    app = FishingApp()
    app.menu()
