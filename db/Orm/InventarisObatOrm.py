from sqlalchemy import Column, String, Integer, ForeignKey, Date
from db.base import Base


class InventarisObatOrm(Base):
    __tablename__ = 'inventaris_obat'

    id = Column(Integer, primary_key=True)
    idObat = Column(Integer, ForeignKey('obat.id'))
    stockObat = Column(Integer)
    expObat = Column(Date)
    hargaObat = Column(Integer)
    lokasi = Column(String)

    def __init__(self, idObat, stockObat, expObat, hargaObat, lokasi):
        self.idObat = idObat
        self.stockObat = stockObat
        self.expObat = expObat
        self.hargaObat = hargaObat
        self.lokasi = lokasi