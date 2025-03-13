class Blue:
    def intro(self):
        print("Jenis warna biru:")

    def name(self):
        print("Name: Navy")

    def hex_code(Self):
        print("Code: #000080")

class Turquoise(Blue):
    def name(self):
        print("Name: Turquoise")

    def hex_code(Self):
        print("Code: #40e0d0")

objek_Blue = Blue()
objek_Trqs = Turquoise()

for biru in (objek_Blue, objek_Trqs):
    print()
    biru.intro()
    biru.name()
    biru.hex_code()
