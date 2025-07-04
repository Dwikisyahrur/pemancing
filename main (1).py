from models.fish import Fish
from models.angler import Angler
from models.log import FishingLog

def main():
    log = FishingLog("data/log.json")

    # Tambah catatan sesuai permintaan pengguna
    name = "Dwiki"
    species = "Lele"
    weight = 2.0
    bait = "Cacing"
    location = "Sungai di Sukabumi"

    angler = Angler(name)
    fish = Fish(species, weight, bait)
    entry = angler.log_catch(fish, location)
    log.add_entry(entry)

    while True:
        print("\n=== Menu Catatan Mancing ===")
        print("1. Tambah Catatan")
        print("2. Lihat Semua Catatan")
        print("3. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            try:
                name = input("Nama pemancing: ")
                species = input("Jenis ikan: ")
                weight = float(input("Berat ikan (kg): "))
                bait = input("Umpan: ")
                location = input("Lokasi: ")

                angler = Angler(name)
                fish = Fish(species, weight, bait)
                entry = angler.log_catch(fish, location)
                log.add_entry(entry)
                print("Catatan berhasil ditambahkan!")
            except ValueError:
                print("Input tidak valid. Berat harus berupa angka.")

        elif pilih == "2":
            log.show_all()

        elif pilih == "3":
            print("Terima kasih telah menggunakan aplikasi catatan mancing!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
