# Escriba el codigo necesario para que al ejecutar python ejercicio2.py
# se cree una grafica con una funcion sinusoidal entre 0 y 2pi.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi)
sen= np.sin(x)

plt.plot(x,sen)

