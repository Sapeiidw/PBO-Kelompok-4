from Class.JenisObat import JenisObat
class Obat():

    def __init__(self, JenisObat, namaObat):
        self.__jenisObat = JenisObat
        self.__namaObat = namaObat

    @property
    def jenisObat(self):
        return self.__jenisObat
    
    @jenisObat.setter
    def jenisObat(self, JenisObat):
        self.__jenisObat = JenisObat

    @property
    def namaObat(self):
        return self.__namaObat
    
    @namaObat.setter
    def namaObat(self, namaObat):
        self.__namaObat = namaObat


# o = Obat(JenisObat(2), "somtehing")
# print(o.jenisObat)