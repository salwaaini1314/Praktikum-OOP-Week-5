# Program menghitung sisa stok barang di beberapa toko cabang

class Barang:
    def __init__(self, nama_barang, stok):
        self.nama_barang = nama_barang
        self.stok = stok

    def __add__(self, other):
        return self.stok + other.stok

Gudang1 = Barang("Komputer", 60)
Gudang2 = Barang("Laptop", 30)
Gudang3 = Barang("Laptop", 15)
Gudang4 = Barang("Komputer", 45)

print(f"Sisa stok {Gudang1.nama_barang} ada {Gudang1 + Gudang4} unit")
print(f"Sisa stok {Gudang2.nama_barang} ada {Gudang2 + Gudang3} unit")