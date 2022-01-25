import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

def estimacion_bo_b1(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)

    sumatoria_xy = np.sum((x-m_x)*(y-m_y))
    sumatoria_xx = np.sum((x-m_x)**2)

    b_1 = sumatoria_xy/sumatoria_xx
    b_o = m_y - b_1 * m_x

    return(b_o, b_1)


def plot_regresion(x, y, b):
    plt.scatter(x, y, color="g", marker="o", s=30)

    y_pred = b[0] + b[1]*x

    plt.plot(x, y_pred, color="b")
    plt.xlabel("X Variable independiente")
    plt.ylabel("Y variale dependiente")
    plt.show()

def main():
    x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    y = np.array([125,124,123,122,100,110,115,123,56,60,111,150,200,95,125,154,124,121,122])

    b = estimacion_bo_b1(x,y)
    print("Los valores de bo={} los valores de b1={}".format(b[0],b[1]))
    plot_regresion(x,y,b)

if __name__=="__main__":
    main()
