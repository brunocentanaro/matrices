import tkinter as tk
from tkinter import ttk
import numpy as np
import math
from random import randint

class entradas:
    def __init__(self, root, operacion, m, n = 0, landa = 0):
        self.landa = landa
        self.root = root
        self.operacion = operacion
        if self.operacion == "det" or self.operacion == "inv":
            self.Filas = m
            self.Columnas = m
            self.crearEntradadas()
        elif self.operacion == "esc" or self.operacion == "mult":
            self.Filas = m
            self.Columnas = n
            self.crearEntradadas()


    def delete(self):
        try:
            for lista in self.entradas:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass
        try:
            self.boton.grid_forget()
        except AttributeError:
            pass
        try:
            self.error.grid_forget()
        except AttributeError:
            pass
        try:
            self.mostrar.grid_forget()
        except AttributeError:
            pass
        try:
            self.simbM.grid_forget()
        except AttributeError:
            pass
        try:
            for lista in self.entEscalerizada:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass
        try:
            for item in self.signoIgual:
                item.grid_forget()
        except AttributeError:
            pass
        try:
            for lista in self.entradasInversa:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass

        try:
            for lista in self.entMult:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass

    def crearEntradadas(self):
        try:
            for row in range(0, self.Filas):
                for column in range(0, self.Columnas):
                    try:
                        self.entradas[row][column].grid_forget()
                    except (IndexError, AttributeError):
                        pass
        except (TypeError, AttributeError, ValueError):
            pass
        try:
            self.mostrar.grid_forget()
        except AttributeError:
            pass
        try:
            self.error.grid_forget()
        except AttributeError:
            pass

        if self.operacion == "esc":
            self.signoIgual = [[] for k in range(0, self.Filas)]
            for row in range(0, self.Filas):
                self.signoIgual[row] = tk.Label(self.root, text = "=")
                self.signoIgual[row].grid(row=row+2,column=self.Columnas, sticky="nsew")

            self.Columnas +=1
            self.entradas = [[[] for j in range(0, self.Columnas)] for k in range(0, self.Filas)]
            for row in range(0, self.Filas):
                for column in range(0, self.Columnas-1):
                    rand = randint(0,1000)
                    self.entradas[row][column] = tk.Entry(self.root, text="Row : "+str(row+rand)+"Column : "+str(column - rand+self.landa))
                    self.entradas[row][column].grid(row=row+2,column=column+self.landa, sticky="nsew")
            for row in range(0, self.Filas):
                rand = randint(0,1000)
                self.entradas[row][self.Columnas-1] = tk.Entry(self.root, text="Row : "+str(row+rand)+"Column : "+str(column - rand+self.landa))
                self.entradas[row][self.Columnas-1].grid(row=row+2,column=self.Columnas+1, sticky="nsew")
        else:
            self.entradas = [[[] for j in range(0, self.Columnas)] for k in range(0, self.Filas)]
            for row in range(0, self.Filas):
                for column in range(0, self.Columnas):
                    rand = randint(0,1000)
                    self.entradas[row][column] = tk.Entry(self.root, text="Row : "+str(row+rand)+"Column : "+str(column - rand+self.landa))
                    self.entradas[row][column].grid(row=row+2,column=column+self.landa, sticky="nsew")

        if self.operacion == "det":
            self.boton = tk.Button(self.root, text = "hacer Det", command = self.hacerDeterminante)
            self.boton.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))-1)
        elif self.operacion == "inv":
            self.boton = tk.Button(self.root, text = "hacer inversa", command = self.hacerInversa)
            self.boton.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))-1)
        elif self.operacion == "esc":
            self.boton = tk.Button(self.root, text = "hacer esc", command = self.escalerizar)
            self.boton.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))-1)

        elif self.operacion == "mult" and self.landa != 0:
            self.simbM = tk.Label(self.root, text = "*")
            self.simbM.grid(row = 2, column = self.Filas + 1 )
            self.boton = tk.Button(self.root, text = "=", command = self.multplicar)
            self.boton.grid(row = math.ceil(self.Filas/2) + 1 , column = self.Columnas + self.Filas + 2)

    def hacerArray(self, esc = False):
        if esc == False:
            self.array = np.zeros((self.Filas,self.Columnas))
            for i in range(0, self.Filas):
                for j in range(0, self.Columnas):
                    if self.entradas[i][j].get() == "":
                        try:
                            self.error.grid_forget()
                        except AttributeError:
                            pass
                        self.error = tk.Label(self.root, text = f"El valor en la posicion {i+1}, {j+1} esta vacio, por favor completelo para seguir")
                        self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))+self.landa)
                        return False
                    try:
                        self.array[i][j] = float(self.entradas[i][j].get())
                    except ValueError:
                        try:
                            self.error.grid_forget()
                        except AttributeError:
                            pass
                        self.error = tk.Label(self.root, text = f"El valor en la posicion {i+1}, {j+1} no es un numero, por favor cambielo para seguir")
                        self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))+self.landa)
                        return False
        else:
            self.array = np.zeros((self.Filas,self.Columnas))
            for i in range(0, self.Filas):
                for j in range(0, self.Columnas-1):
                    if self.entradas[i][j].get() == "":
                        try:
                            self.error.grid_forget()
                        except AttributeError:
                            pass
                        self.error = tk.Label(self.root, text = f"El valor en la posicion {i+1}, {j+1} esta vacio, por favor completelo para seguir")
                        self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))+self.landa)
                        return False
                    try:
                        self.array[i][j] = float(self.entradas[i][j].get())
                    except ValueError:
                        try:
                            self.error.grid_forget()
                        except AttributeError:
                            pass
                        self.error = tk.Label(self.root, text = f"El valor en la posicion {i+1}, {j+1} no es un numero, por favor cambielo para seguir")
                        self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))+self.landa)
                        return False
            for i in range(0, self.Filas):
                if self.entradas[i][self.Columnas-1].get() == "":
                    self.array[i][self.Columnas-1] = float(0)
                else:
                    try:
                        self.array[i][self.Columnas-1] = float(self.entradas[i][self.Columnas-1].get())
                    except ValueError:
                        try:
                            self.error.grid_forget()
                        except AttributeError:
                            pass
                        self.error = tk.Label(self.root, text = f"El valor en la posicion {i+1}, {j+1} no es un numero, por favor cambielo para seguir")
                        self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2))+self.landa)
                        return False


    def hacerDeterminante(self):
        if self.hacerArray() == False:
            return
        else:
            try:
                self.mostrar.grid_forget()
            except AttributeError:
                pass
            try:
                self.error.grid_forget()
            except AttributeError:
                pass
            if self.Filas == 1:
                self.determinante = self.array[0][0]
            elif self.Filas == 2:
                self.determinante = self.array[0][0]*self.array[1][1] - self.array[0][1]*self.array[1][0]
            elif self.Filas == 3:
                self.determinante = deterArray3x3(self.array)
            else:
                self.determinante = deterArray(self.array)

        self.mostrar = tk.Label(self.root, text = f"El determinante de su matriz es: {self.determinante:,}")
        self.mostrar.grid(row = self.Filas + 2, column = round(math.ceil(self.Filas/2)))

    def escalerizar(self):
        try:
            for lista in self.entEscalerizada:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass
        if self.hacerArray(True) == False:
            return
        else:
            try:
                self.error.grid_forget()
            except AttributeError:
                pass


        self.escalerizada, self.cambios  = escalerizarr(self.array)

        self.entEscalerizada = [[[] for j in range(0, self.Columnas)] for k in range(0, self.Filas)]
        for row in range(0, self.Filas):
            for column in range(0, self.Columnas):
                self.format = self.escalerizada[row][column]
                self.entEscalerizada[row][column] = tk.Label(self.root, text= f"{self.format:,.2f}")
                self.entEscalerizada[row][column].grid(row=row+2,column=(column + self.Columnas +2))
                
        if self.Filas == self.Columnas-1:
            self.resultados = np.zeros(self.Columnas-1)
            for i in range(self.Filas-1, -1, -1):
                suma = self.escalerizada[i][self.Columnas-1]
                for j in range(0, self.Filas-1-i):
                    suma = suma - self.escalerizada[i][self.Columnas-2-j]*self.resultados[j]
                self.resultados[self.Filas-1-i] = suma / self.escalerizada[i][i]
            print(self.resultados)





    def multplicar(self):
        try:
            dim1 = len(self.entMult)
            dim2 = len(self.entMult[0])
            for i in range(0, dim1):
                for j in range(0, dim2):
                    self.entMult[i][j].grid_forget()
        except AttributeError:
            pass
        global C
        try:
            C.A.error.grid_forget()
        except AttributeError:
            pass
        try:
            C.B.error.grid_forget()
        except AttributeError:
            pass

        aCompleta = C.A.hacerArray()
        bCompleta = C.B.hacerArray()
        if aCompleta == False or bCompleta == False:
            self.generarR()
            return

        self.multplicada = multplicacionArray(C.A.array, C.B.array)
        a, b = self.multplicada.shape
        self.entMult = [[[] for j in range(0, b)] for k in range(0, a)]
        for i in range(0, a):
            for j in range(0, b):
                self.formatt = self.multplicada[i][j]
                self.entMult[i][j] = tk.Label(self.root, text = f"{self.formatt:,.2f}")
                self.entMult[i][j].grid(row = i + 2, column = j + self.Columnas + self.Filas + 3)

    def generarR(self):
        global C
        a = C.A.Filas
        b = C.B.Columnas
        self.entMult = [[[] for j in range(0, b)] for k in range(0, a)]
        for i in range(0, a):
            for j in range(0, b):
                self.entMult[i][j] = tk.Label(self.root, text = f"  -  ")
                self.entMult[i][j].grid(row = i + 2, column = j + self.Columnas + self.Filas + 3)

    def hacerInversa(self):
        try:
            for lista in self.entradasInversa:
                for item in lista:
                    item.grid_forget()
        except AttributeError:
            pass
        if self.hacerArray() == False:
            return
        else:
            try:
                self.error.grid_forget()
            except AttributeError:
                pass

        self.hacerDeterminante()
        #Esta para no hacer otra funcion
        self.mostrar.grid_forget()
        if self.determinante != 0:
            self.inversa = np.zeros((self.Filas,self.Filas))
            for i in range(0,self.Filas):
                self.inversa[i][i] = 1
            self.array, self.inversa = escalerizarInv(self.array, self.inversa)
            self.array, self.inversa = antiEsc(self.array, self.inversa)
            for i in range(0, self.Filas):
                self.factor = np.copy(self.array[i][i])
                self.inversa[i] = self.inversa[i]/self.factor

            a, b = self.inversa.shape
            self.entradasInversa = [[[] for j in range(0, b)] for k in range(0, a)]
            for i in range(0, a):
                for j in range(0, b):
                    self.formatt = self.inversa[i][j]
                    self.entradasInversa[i][j] = tk.Label(self.root, text = f"{self.formatt:,.4f}")
                    self.entradasInversa[i][j].grid(row = i + 2, column = j + self.Filas + 3)
            self.hacerArray()
            print(np.around(multplicacionArray(self.array, self.inversa),0).astype(int))
        else:
            self.error = tk.Label(self.root, text = f"El determinante de su matriz es 0 y por lo tanto no tiene inversa")
            self.error.grid(row = self.Filas + 2, column = round(math.ceil(self.Columnas/2)-1)+1)

class genMat:
    def __init__(self, root, operacion):
        self.root = root
        self.operacion = operacion
        self.run = False
        if self.operacion == "det" or self.operacion == "inv":
            self.EFilas = tk.Entry(self.root, text="Cuantos")
            self.EFilas.grid(row=0,column=0)
            self.button = tk.Button(self.root, text = "Generar Matriz A", command = self.check)
            self.button.grid(row=0,column=1)

        elif self.operacion == "esc":
            self.EFilas = tk.Entry(self.root, text="FilasE")
            self.EFilas.grid(row=0,column=0)
            self.EColumnas = tk.Entry(self.root, text="ColumnasE")
            self.EColumnas.grid(row=0,column=1)
            self.button = tk.Button(self.root, text = "Generar Matriz A", command = self.check)
            self.button.grid(row=0,column=2)

        elif self.operacion == "mult":
            #Matriz A
            self.LabelA = tk.Label(self.root, text = "Dimensiones matriz A: ")
            self.LabelA.grid(row = 0, column = 0)
            self.EFilas = tk.Entry(self.root, text="FilasM")
            self.EFilas.grid(row=0,column=1)
            self.EColumnas = tk.Entry(self.root, text="ColumnasM")
            self.EColumnas.grid(row=0,column=2)
            #matriz B
            self.LabelB = tk.Label(self.root, text = "Dimensiones matriz B: ")
            self.LabelB.grid(row = 0, column = 4)
            self.BEFilas = tk.Entry(self.root, text="FilasB")
            self.BEFilas.grid(row=0,column=5)
            self.BEColumnas = tk.Entry(self.root, text="ColumnasB")
            self.BEColumnas.grid(row=0,column=6)
            self.Bbutton = tk.Button(self.root, text = "Generar matrices.", command = self.check)
            self.Bbutton.grid(row=0,column=7)

    def check(self):
        try:
            self.error.grid_forget()
        except AttributeError:
            pass
        if self.operacion == "det" or self.operacion == "inv":
            if self.run == True:
                try:
                    self.A.delete()
                except AttributeError:
                    pass
                try:
                    self.D.delete()
                except AttributeError:
                    pass
            try:
                self.Filas = int(self.EFilas.get())
                self.Columnas = self.Filas
            except (ValueError, AttributeError):
                try:
                    self.error.grid_forget()
                except AttributeError:
                    pass
                self.error = tk.Label(self.root, text = "Los valores deben ser enteros positivos")
                self.error.grid(row = 1, column = 0)
                return

            self.run = True
            if self.operacion == "det":
                self.A = entradas(self.root, "det", self.Filas)
            elif self.operacion == "inv":
                self.D = entradas(self.root, "inv", self.Filas)

        elif self.operacion == "esc":
            try:
                self.A.delete()
            except AttributeError:
                pass
            try:
                self.Filas = int(self.EFilas.get())
                self.Columnas = int(self.EColumnas.get())
            except ValueError:
                try:
                    self.error.grid_forget()
                except AttributeError:
                    pass
                self.error = tk.Label(self.root, text = "Los valores deben ser enteros positivos")
                self.error.grid(row = 1, column = 0)
                return
            self.run = True
            self.A = entradas(self.root, "esc", self.Filas, self.Columnas)

        elif self.operacion == "mult":
            if self.run == True:
                    self.A.delete()
                    self.B.delete()
            try:
                self.Filas = int(self.EFilas.get())
                self.Columnas = int(self.EColumnas.get())
                self.BFilas = int(self.BEFilas.get())
                self.BColumnas = int(self.BEColumnas.get())
            except ValueError:
                try:
                    self.error.grid_forget()
                except AttributeError:
                    pass
                self.error = tk.Label(self.root, text = "Los valores deben ser enteros positivos")
                self.error.grid(row = 1, column = 0)
                return
            if self.Columnas == self.BFilas:
                self.LabelB.grid(row = 0, column = self.Columnas+2)
                self.BEFilas.grid(row=0,column=self.Columnas+3)
                self.BEColumnas.grid(row=0,column=self.Columnas+4)
                self.Bbutton.grid(row=0,column=self.Columnas+5)

                self.run = True
                self.A = entradas(self.root, "mult", self.Filas, self.Columnas)
                self.B = entradas(self.root, "mult", self.BFilas, self.BColumnas, self.Columnas+2)
                self.B.generarR()
            else:
                try:
                    self.error.grid_forget()
                except AttributeError:
                    pass
                self.error = tk.Label(self.root, text = "Las columnas de la matriz A y la cantidad de filas de la B deben ser iguales")
                self.error.grid(row = 1, column = 0)

#PARA CREAR INVERSAR
def prepararArray(Array, i,j, inversa = np.array([])):
    n, m = Array.shape
    minimo = min(n,m)
    if inversa.size == 0:
        cambio = None
        for p in range(j, minimo):
            if Array[p][i] != 0 and Array[i][p] != 0:
                nueva_fila = np.copy(Array[i])
                Array[i] = Array[p]
                Array[p] = nueva_fila
                cambio = f"se cambio la fila {i+1} por la {p+1}"
                pass
        return Array, cambio
    else:
        for p in range(j, m):
            if Array[p][i] != 0 and Array[i][p] != 0:
                nueva_fila = np.copy(Array[i])
                Array[i] = Array[p]
                Array[p] = nueva_fila
                nueva_fila_inv = np.copy(inversa[i])
                inversa[i] = inversa[p]
                inversa[p] = nueva_fila_inv
        return Array, inversa

def escalerizarInv(Array, inversa):
    _, m = Array.shape
    g = 0
    for i in range(0, m):
        if Array[i][i] == 0 and i != (m-1):
            Array, inversa = prepararArray(Array, i, i, inversa)

    for i in range(0, m):
        if Array[i][i] == 0:
            if Array[i][i] == 0 and i != (m-1):
                Array, inversa = prepararArray(Array, i, 0, inversa)

    for _ in range(m-1):
        Array, inversa = Esc(Array, inversa, g)
        g += 1

    return Array, inversa

def Esc(Array, inversa, g):
    _, n = Array.shape
    a =  Array[g][g]
    if a != 0:
        for i in range(0+g, n-1):
            factor = np.copy(Array[i+1][g] / a)
            inversa[i+1] = inversa[i+1] - inversa[g]*factor
            Array[i+1] = Array[i+1] - Array[g]*factor
        g += 1
    else:
        Array, inversa = prepararArray(Array, g, 0, inversa)
        Array, inversa = Esc(Array, inversa, g)
    return Array, inversa

def antiEsc(Array, inversa):
    m, n = Array.shape
    g = m-1
    for _ in range(n-1):
        a =  Array[g][g]
        for i in range(g, 0, -1):
            factor = np.copy(Array[i-1][g] / a)
            inversa[i-1] = inversa[i-1] - inversa[g]*factor
            Array[i-1] = Array[i-1] - Array[g]*factor
        g -= 1
    return Array, inversa

def deterArray3x3(A):
    suma = 0
    ABajo = np.delete(A, 2, 0)
    A = np.concatenate((A, ABajo))
    for i in range(0, 3):
        suma = suma + A[i][0]*A[i+1][1]*A[i+2][2]
        suma = suma - A[2+i][0]*A[1+i][1]*A[i][2]
    return(suma)

def deterArray(A):
    suma = 0
    a,_ = A.shape
    if a == 4:
        for i in range(0,a):
            a = A[i][0]
            if a != 0:
                nuevo = np.delete(A, i, 0)
                final = np.delete(nuevo, 0, 1)
                suma = suma + a*((-1)**(i+2))*deterArray3x3(final)
    else:
        for i in range(0,a):
            a = A[i][0]
            if a != 0:
                nuevo = np.delete(A, i, 0)
                final = np.delete(nuevo, 0, 1)
                suma = suma + a*((-1)**(i+2))*deterArray(final)
    return suma

def escalerizarr(Array):
    n, m = Array.shape
    g = 0
    Array = Array.astype(float)
    cambios = []
    minimo = min(n,m)
    for i in range(0, minimo):
        if Array[i][i] == 0 and i != (minimo-1):
            Array, cambio = prepararArray(Array, i, i)
            cambios.append(cambio)

    for i in range(0, minimo):
        if Array[i][i] == 0:
            if Array[i][i] == 0 and i != (minimo-1):
                Array, cambio = prepararArray(Array, i,0)
                cambios.append(cambio)

    for _ in range(minimo-1):
        a =  Array[g][g]
        if a != 0:
            for i in range(0+g, minimo-1):
                factor = Array[i+1][g] / a
                Array[i+1] = Array[i+1] - Array[g]*factor
            g += 1
        else:
            Array, cambio = prepararArray(Array, g, 0)
            cambios.append(cambio)

    return Array, cambios


def multplicacionArray(A,B):
    mA, nA = A.shape
    _, nB = B.shape
    multplicacion = np.empty([mA, nB])
    for i in range(0, mA):
        for j in range(0, nB):
            suma = 0
            for g in range(0, nA):
                suma = suma + A[i][g]*B[g][j]
            multplicacion[i][j] = suma
    return multplicacion

root = tk.Tk()

tabControl = ttk.Notebook(root)

determinante = ttk.Frame(tabControl)
escalerizar = ttk.Frame(tabControl)
multplicar = ttk.Frame(tabControl)
inversa = ttk.Frame(tabControl)
tabControl.add(determinante, text = "determinante")
tabControl.add(escalerizar, text = "escalerizar")
tabControl.add(multplicar, text = "multplicar")
tabControl.add(inversa, text = "inversa")
tabControl.pack(expand = 1, fill = "both")

A = genMat(escalerizar, "esc")
B = genMat(determinante, "det")
C = genMat(multplicar, "mult")
D = genMat(inversa, "inv")


root.mainloop()