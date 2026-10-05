# ==========================================================
#  PROGRAM SISTEM PARKIR KAMPUS
#  Watermark : Kelompok 40
# ==========================================================

WATERMARK = "Kelompok 40"
TARIF = {"motor": 2000, "mobil": 5000}  # tarif per jam


# ---------------------- FUNCTION ----------------------
def tampilkan_watermark(judul):  # non-return, param
    print("=" * 44)
    print(judul.center(44))
    print(("[ " + WATERMARK + " ]").center(44))
    print("=" * 44)


def tampilkan_menu():  # non-return, tanpa param
    print("\n1. Kendaraan Masuk")
    print("2. Kendaraan Keluar")
    print("3. Daftar Kendaraan")
    print("4. Cari Kendaraan")
    print("5. Keluar Program")


def ambil_kapasitas():  # return, tanpa param
    return 5


def hitung_biaya(jenis, jam):  # return, param
    if jam < 1:
        jam = 1
    biaya = TARIF[jenis] * jam
    if jam > 5:  # diskon > 5 jam
        biaya = int(biaya * 0.8)
    return biaya


# ------------------------ CLASS -----------------------
class Parkiran:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.kendaraan = {}  # plat -> jenis
        self.pendapatan = 0

    def sisa_slot(self):  # return
        return self.kapasitas - len(self.kendaraan)

    def ada(self, plat):  # return
        return plat in self.kendaraan

    def masuk(self, plat, jenis):  # non-return
        if self.sisa_slot() == 0:
            print("Parkiran penuh!")
        elif self.ada(plat):
            print("Plat", plat, "sudah terdaftar di dalam.")
        else:
            self.kendaraan[plat] = jenis
            print("Berhasil masuk. Sisa:", self.sisa_slot())

    def keluar(self, plat, jam):  # non-return
        if not self.ada(plat):
            print("Kendaraan tidak ditemukan.")
            return
        biaya = hitung_biaya(self.kendaraan[plat], jam)
        self.pendapatan += biaya
        del self.kendaraan[plat]
        print("Biaya parkir: Rp", biaya)

    def tampilkan_daftar(self):  # non-return
        if len(self.kendaraan) == 0:
            print("Parkiran kosong.")
            return
        nomor = 1
        for plat, jenis in self.kendaraan.items():
            print(str(nomor) + ".", plat, "-", jenis)
            nomor += 1
        print("Total pendapatan: Rp", self.pendapatan)


# ------------------------ MAIN ------------------------
def main():
    parkir = Parkiran(ambil_kapasitas())
    tampilkan_watermark("SISTEM PARKIR KAMPUS")
    jalan = True
    while jalan:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            plat = input("Plat nomor: ").upper()
            jenis = input("Jenis (motor/mobil): ").lower()
            if jenis in TARIF:
                parkir.masuk(plat, jenis)
            else:
                print("Jenis tidak valid.")
        elif pilihan == "2":
            plat = input("Plat nomor: ").upper()
            lama = input("Lama parkir (jam): ")
            if lama.isdigit():
                parkir.keluar(plat, int(lama))
            else:
                print("Input jam harus angka.")
        elif pilihan == "3":
            parkir.tampilkan_daftar()
        elif pilihan == "4":
            plat = input("Plat nomor: ").upper()
            if parkir.ada(plat):
                print("Kendaraan ADA di dalam parkiran.")
            else:
                print("Kendaraan TIDAK ada.")
        elif pilihan == "5":
            jalan = False
            tampilkan_watermark("TERIMA KASIH")
        else:
            print("Menu tidak tersedia.")


main()