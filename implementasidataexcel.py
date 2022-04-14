import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import resize
import math


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)


def sigma(kuadrat=False, **kwargs):
    result = {}
    if(kuadrat == False):
        if(len(kwargs) > 1):
            # Real X and Y
            for key, value in kwargs.items():
                result[str(key)] = value
            # Sum X and Y
            for key, value in kwargs.items():
                result[str(key) + "_sum"] = sum(value)

            XY_Sigma = 0
            X_pow_sum = 0
            Y_pow_sum = 0
            for i in range(len(result["X"])):
                XY_Sigma += result["X"][i] * result["Y"][i]
                X_pow_sum += math.pow(result["X"][i], 2)
                Y_pow_sum += math.pow(result["Y"][i], 2)

            result["XY_Sigma"] = XY_Sigma
            result["X_pow_sum"] = X_pow_sum
            result["Y_pow_sum"] = Y_pow_sum
            return result
        else:
            for key, value in kwargs.items():
                result[str(key) + "_sum"] = sum(value)
            return result
    else:
        for key, value in kwargs.items():
            result[str(key) + "_sum"] = sum(value)

        return result


def konstanta_a(n, sigma_X, sigma_Y, sigma_XY, sigma_X_pow):
    a_atas = (sigma_Y * sigma_X_pow) - (sigma_X * sigma_XY)
    a_bawah = (n * sigma_X_pow) - math.pow(sigma_X, 2)
    a = a_atas / a_bawah
    return a


def koef_b(n, sigma_X, sigma_Y, sigma_XY, xpow_sum):
    b_atas = (n * sigma_XY) - (sigma_X * sigma_Y)
    b_bawah = (n * xpow_sum) - math.pow(sigma_X, 2)
    b = b_atas / b_bawah
    return b

def main():
    # observations / data
    x = np.array([10, 2, 4, 6, 8])

    y = np.array([23, 7, 15, 17, 23])

    
    result = sigma(X=x, Y=y, kuadrat=False)
    a = konstanta_a(len(x), result["X_sum"], result["Y_sum"],
                    result["XY_Sigma"], result["X_pow_sum"])
    b = koef_b(len(x), result["X_sum"], result["Y_sum"],
               result["XY_Sigma"], result["X_pow_sum"])

    print(result)
    print("Konstanta =", a)
    print("Koefisien =",b)
    plt.scatter(x,y)
    plt.plot(a,b, color='blue')
    plt.title('Produksi pupuk parameter dengan parameter dosis pupuk')
    plt.xlabel('Dosis Pupuk')
    plt.ylabel('Produksi Pupuk')
    plt.show()


if __name__ == "__main__":
    main()
