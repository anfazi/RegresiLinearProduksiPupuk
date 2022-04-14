from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import  QMainWindow
from PyQt5.uic import loadUi
import sys
import pandas as pd
import matplotlib.pyplot as plt
from regex import B
from perhitungan import DataRegresi
import numpy as np

data = pd.read_csv('pupuk.csv')
x = data['X']
y = data['Y']

print("x=", x)
print("y=", y)

dataRegresi = DataRegresi(x, y, "Dosis pupuk", "Produksi Pupuk")

class CB (QMainWindow):
    def __init__(self):
        super(CB,self).__init__()
        loadUi('gui.ui',self)

        self.btnTampilModelRegresi.clicked.connect(self.TampilModelRegresiClicked)
        self.btnprosesInputDosisPupuk.clicked.connect(self.prosesInputDosisPupukClicked)
        self.btnTampilkanKorelasi.clicked.connect(self.TampilkanKorelasiClicked)
        self.btnTampilkanKontribusi.clicked.connect(self.TampilkanKontribusiClicked)
        self.btnTampilkanGrafik.clicked.connect(self.TampilkanGrafikClicked)


    def TampilModelRegresiClicked(self):
        self.lineEditTampilModelRegresi.setText(dataRegresi.print_model())
    
    def prosesInputDosisPupukClicked(self):
        inputData = self.lineEditDosisInput.text()
        model = dataRegresi.get_model(int(inputData))
        self.lineEditHasilModel.setText(str(model))
    
    def TampilkanKorelasiClicked(self):
        a = str(dataRegresi.get_korelasi())
        b = dataRegresi.get_deskripsi_korelasi()
        c = a + b
        self.lineEditKorelasi.setText(c)
        
    def TampilkanKontribusiClicked(self):
        a = dataRegresi.get_deskripsi_determinasi()
        b = dataRegresi.get_deskripsi_kontribusi_lain()
        c = a + b
        self.lineEditKontribusi.setText(c)

    def TampilkanGrafikClicked(self):
        plt.xlabel(dataRegresi.get_x_name())
        plt.ylabel(dataRegresi.get_y_name())
        plt.title('Grafik Model')
        plt.scatter(dataRegresi.get_x(), dataRegresi.get_y(),
                    c=np.random.rand(dataRegresi.get_count_x()), alpha=0.5)
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CB()
    window.setWindowTitle('Prediksi Produksi Pupuk Berdasarkan Dosis Pupuk')
    window.show()
    sys.exit(app.exec())
