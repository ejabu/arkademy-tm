class Binatang():

    def __init__(self, kaki):
        self.kaki = kaki

    def show_kaki(self):
        print(self.kaki)

    def show_home(self):
        print("Kebun Binatang")
        
    def taaruf(self):
        self.show_kaki()
        self.show_home()

singa = Binatang(4)
singa.taaruf()

kucing = Binatang(4)
kucing.taaruf()

ayam = Binatang(2)
ayam.taaruf()

