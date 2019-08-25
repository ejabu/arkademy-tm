class Binatang():
    def __init__(self, kaki):
        self.kaki = kaki
    def show_kaki(self):
        print(self.kaki)
    def show_home(self):
        print("Kebun Binatang")

singa = Binatang(4)
singa.show_kaki()

kucing = Binatang(4)
kucing.show_kaki()

ayam = Binatang(2)
ayam.show_kaki()

