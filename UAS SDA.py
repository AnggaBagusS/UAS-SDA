class Pasien:
    def __init__(self, nama, nomor_antrian):
        self.nama = nama
        self.nomor_antrian = nomor_antrian

class AntrianKlinik:
    def __init__(self):
        self.nomor_antrian_terpanggil = []  # Stack
        self.antrian_tunggu = []  # Queue
        self.data_pasien = {}  # Hash Table

    def masukkan_antrian(self, pasien):
        self.antrian_tunggu.append(pasien)
        self.data_pasien[pasien.nomor_antrian] = pasien

    def panggil_antrian(self):
        if len(self.antrian_tunggu) == 0:
            print("Tidak ada pasien dalam antrian.")
            return None

        pasien = self.antrian_tunggu.pop(0)
        self.nomor_antrian_terpanggil.append(pasien.nomor_antrian)
        return pasien

    def dapatkan_pasien_berdasarkan_nomor_antrian(self, nomor_antrian):
        if nomor_antrian in self.data_pasien:
            return self.data_pasien[nomor_antrian]
        else:
            return None

    def tampilkan_antrian_tunggu(self):
        print("Antrian Tunggu:")
        for pasien in self.antrian_tunggu:
            print("Nomor Antrian:", pasien.nomor_antrian, "Nama:", pasien.nama)

    def tampilkan_nomor_antrian_terpanggil(self):
        print("Nomor Antrian Terpanggil:")
        for nomor in self.nomor_antrian_terpanggil:
            pasien = self.dapatkan_pasien_berdasarkan_nomor_antrian(nomor)
            if pasien:
                print("Nomor Antrian:", pasien.nomor_antrian, "Nama:", pasien.nama)

# Fungsi untuk menampilkan opsi kepada pengguna
def tampilkan_opsi():
    print("==========")
    print("Opsi:")
    print("1. Tambahkan pasien ke antrian")
    print("2. Panggil antrian")
    print("3. Tampilkan antrian tunggu")
    print("4. Tampilkan nomor antrian terpanggil")
    print("5. Keluar")
    print("==========")

# Contoh penggunaan sistem antrian klinik
klinik = AntrianKlinik()

while True:
    tampilkan_opsi()
    opsi = input("Pilih opsi (1-5): ")

    if opsi == "1":
        nama = input("Masukkan nama pasien: ")
        nomor_antrian = int(input("Masukkan nomor antrian: "))
        pasien = Pasien(nama, nomor_antrian)
        klinik.masukkan_antrian(pasien)
        print("Pasien", nama, "telah ditambahkan ke dalam antrian.")
    elif opsi == "2":
        pasien = klinik.panggil_antrian()
        if pasien:
            print("Pasien", pasien.nama, "dipanggil.")
    elif opsi == "3":
        klinik.tampilkan_antrian_tunggu()
    elif opsi == "4":
        klinik.tampilkan_nomor_antrian_terpanggil()
    elif opsi == "5":
        print("Program selesai.")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang sesuai (1-5).")
