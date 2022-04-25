from PyQt5.QtWidgets import QApplication, QWidget
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from Problem1_1 import Ui_Form
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from math import pi
from matplotlib.backends.backend_qt5agg import  NavigationToolbar2QT as NavigationToolbar

class main_window(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupImageLabel()
        self.show()
        self.MakeCanvas()
        self.toolbar=NavigationToolbar(self.canvas,self)
        self.layout_GridInput.addWidget(self.toolbar,8,1)

    def setupImageLabel(self):
        #region setup a label to display the image of the circuit
        self.pixMap = qtg.QPixmap()
        self.pixMap.load("Circuit1.png")
        self.image_label = qtw.QLabel()
        self.image_label.setPixmap(self.pixMap)
        self.layout_GridInput.addWidget(self.image_label,0,2,7,1)
        #endregion

    def Calculate_Click(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        self.makeGraph()


    def MakeCanvas(self):
        """
        Create a place to make graph of Rankine cycle
        Step 1:  create a Figure object called self.figure
        Step 2:  create a FigureCanvasQTAgg object called self.canvas
        Step 3:  create an axes object for making plot
        Step 4:  add self.canvas to self.gb_Output.layout() which is a grid layout
        :return:
        """
        #Step 1.
        self.figure=Figure(figsize=(2,4),tight_layout=True, frameon=True)
        #Step 2.
        self.canvas=FigureCanvasQTAgg(self.figure)
        #Step 3.
        self.ax = self.figure.add_subplot()
        #Step 4.
        self.layout_GridInput.addWidget(self.canvas, 9,0,1,4)

    def makeGraph(self):
        R = float(self.LE_R.text())
        t_end = 10.0  # t value to stop on in seconds
        t = np.arange(0, t_end, 0.02)  # create t variable
        # Initial conditions
        i0 = [0, 0]
        # use odeint to solve the functions with the initial conditions
        i = odeint(self.function, i0, t)
        i1, i2 = i[:, 0], i[:, 1]
        # Equation for Vc(t)
        vct = R * (i2 - i1)
        ax1 = self.ax
        ax1.clear()
        #fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        # Plotting i1, i2, and Vc(t)
        ax1.plot(t, i1, '-', color='k')
        ax1.plot(t, i2, '--', color='k')
        ax2.plot(t, vct, linestyle='dotted', color='k')
        # Title the plot
        plt.title('RLC Network')
        # Creating the legend for both currents
        ax1.legend(['$i_1(t)$', '$i_2(t)$'], loc='lower right')
        ax2.legend(['$V_C(t)$'], loc='upper right')
        # Label the axes
        ax1.set_xlabel('Time')
        ax1.set_ylabel('$i_1$ and $i_2$', color='k')
        ax2.set_ylabel('$V_C(t)$', color='k')
        self.canvas.draw()

    def function(self, i, t):
        """
        This function takes the intial condtions and time variables and solves for the ode.
        :param i: tuple of initial conditions
        :param t: time in seconds
        :return: tuple with i1_dot and i2_dot
        """
        R = float(self.LE_R.text())
        L = float(self.LE_L.text())
        C = float(self.LE_C.text())
        V_max=float(self.LE_Magnitude.text())
        Freq=float(self.LE_Frequency.text())*2*pi
        Phase=float(self.LE_Phase.text())
        # Unpack initial conditions
        i1 = i[0]
        i2 = i[1]
        # Equations for i1_dot and i2_dot acquired by solving KVL
        i1_dot = (((V_max * np.sin((Freq * t)+Phase))- R * (i1 - i2)) / L)
        i2_dot = i1_dot - (i2 / (R * C))
        return [i1_dot, i2_dot]


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())