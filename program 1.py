class Hoshi:
    def name(self):
        print("Name: Kwon Soonyoung")

    def unit(self):
        print("Unit: Performance Unit")

class Dokyeom:
    def name(self):
        print("Name: Lee Seokmin")

    def unit(self):
        print("Unit: Vocal Unit")

hoshi = Hoshi()
dk = Dokyeom()

for svt in (hoshi, dk):
    print()
    svt.name()
    svt.unit()