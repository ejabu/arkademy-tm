print("""
Task :
    Coba Print kaki Ayam dengan jumlah yang benar !
""")

class Binatang():
    kaki = 4
    def show_kaki(self):
        print(self.kaki)
    def show_home(self):
        print("Kebun Binatang")

singa = Binatang()
singa.show_kaki()

kucing = Binatang()
kucing.show_kaki()

## .. Silahkan dikoreksi ..

ayam = Binatang()
ayam.show_kaki()
