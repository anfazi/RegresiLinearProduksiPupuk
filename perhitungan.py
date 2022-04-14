import math


class DataRegresi:
    count_x = 0
    count_y = 0
    sigma_x = 0
    sigma_y = 0
    sigma_xy = 0

    def __init__(self, x, y, x_name, y_name):
        self.x = x
        self.y = y
        self.x_name = x_name
        self.y_name = y_name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_x_name(self):
        return self.x_name

    def get_y_name(self):
        return self.y_name

    def get_count_x(self):
        return len(self.x)

    def get_count_y(self):
        return len(self.y)

    def get_sigma_x(self, power=False):
        result = 0
        if(power == False):
            for x in self.x:
                result += x
            return result
        else:
            for x in self.x:
                result += math.pow(x, power)
            return result

    def get_sigma_y(self, power=False):
        result = 0
        if(power == False):
            for y in self.y:
                result += y
            return result
        else:
            for y in self.y:
                result += math.pow(y, power)
            return result

    def get_sigma_xy(self):
        result = 0
        if len(self.x) == len(self.y):
            for i in range(len(self.x)):
                result += self.x[i] * self.y[i]
            return result
        else:
            raise Exception("Error X and Y doesn't have same length!")

    def get_konstanta_a(self):
        atas = (self.get_sigma_y() * self.get_sigma_x(2)) - \
            (self.get_sigma_x() * self.get_sigma_xy())
        bawah = self.get_count_x() * self.get_sigma_x(2) - \
            math.pow(self.get_sigma_x(), 2)
        a = atas / bawah
        return a

    def get_koefisien_b(self):
        atas = (self.get_count_x() * self.get_sigma_xy()) - \
            (self.get_sigma_x() * self.get_sigma_y())
        bawah = (self.get_count_x() * self.get_sigma_x()) - \
            math.pow(self.get_sigma_x(), 2)
        b = atas / bawah
        return b

    def get_model(self, x):
        y = self.get_konstanta_a() + (self.get_koefisien_b() * x)
        return y

    def print_model(self):
        if(self.get_koefisien_b() < 0):
            return "Y = " + str(round(self.get_konstanta_a(), 3)) + " - " + str(abs(round(self.get_koefisien_b(), 3))) + "x" + "\n" + "di mana x adalah dari [" + str(min(self.x)) + "," + str(max(self.x)) + "]"
        else:
            return "Y = " + str(round(self.get_konstanta_a(), 3)) + " + " + str(abs(round(self.get_koefisien_b(), 3))) + "x" + "\n" + "di mana x adalah dari [" + str(min(self.x)) + "," + str(max(self.x)) + "]"

    def get_korelasi(self):
        atas = (self.get_count_x() * self.get_sigma_xy()) - \
            (self.get_sigma_x() * self.get_sigma_y())
        bawah_1 = (self.get_count_x() * self.get_sigma_x(2)) - \
            (math.pow(self.get_sigma_x(), 2))
        bawah_2 = (self.get_count_x() * self.get_sigma_y(2) -
                   math.pow(self.get_sigma_y(), 2))
        bawah = math.sqrt(bawah_1 * bawah_2)
        r = atas / bawah
        return r

    def get_jenis_hubungan(self):
        if(self.get_korelasi() < 0):
            return "negatif"
        else:
            return "positif"

    def get_kekuatanpearsonkorelasi(self):
        if(abs(self.get_korelasi()) < 0.2):
            return "sangat lemah"
        elif(abs(self.get_korelasi()) >= 0.2 or abs(self.get_korelasi()) < 0.4):
            return "lemah"
        elif(abs(self.get_korelasi()) >= 0.4 or abs(self.get_korelasi()) < 0.6):
            return "sedang"
        elif(abs(self.get_korelasi()) >= 0.6 or abs(self.get_korelasi()) < 0.8):
            return "kuat"
        elif(abs(self.get_korelasi()) >= 0.8 or abs(self.get_korelasi()) <= 1):
            return "sangat kuat"
        else:
            return "undefined"

    def get_deskripsi_korelasi(self):
        besar_hubungan = "Besar hubungan antara " + self.get_x_name() + " dan " + \
            self.get_y_name() + " adalah " + str(self.get_korelasi())
        jenis_hubungan = "\nDi mana jenis hubungannya adalah " + self.get_jenis_hubungan()
        kekuatanpearsonkorelasi = " dan kekuatan pearson korelasi hubungannya adalah " + self.get_kekuatanpearsonkorelasi()
        return besar_hubungan + jenis_hubungan + kekuatanpearsonkorelasi

    def get_koefisien_determinasi(self):
        r = math.pow(self.get_korelasi(), 2) * 100
        return round(r, 2)

    def get_deskripsi_determinasi(self):
        return "Besar kontribusi dari variabel " + self.get_x_name() + " terhadap " + self.get_y_name() + " adalah " + str(self.get_koefisien_determinasi()) + "%"

    def get_kontribusi_lain(self):
        return round(100 - round(self.get_koefisien_determinasi(), 3), 2)

    def get_deskripsi_kontribusi_lain(self):
        return "Sisanya " + str(self.get_kontribusi_lain()) + "% merupakan kontribusi dari variabel selain " + self.get_x_name()
