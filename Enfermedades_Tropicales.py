#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib as mp # graficos 
import seaborn as sb # estadistica y visualizacion
Enfermedades_Tropicales= pd.read_csv("Total_Egresos.csv", header=0, sep=';', encoding='latin-1')
E1= Enfermedades_Tropicales.causa3.str.contains("dengue|chagas|leishmaniasis", case=False, regex=True)
E2= Enfermedades_Tropicales.cau_cie10.str.contains("dengue|chagas|leishmaniasis", case=False, regex=True)
Matriz_Enfermedades_Tropicales= Enfermedades_Tropicales[E1 & E2]
Matriz_Enfermedades_Tropicales.to_csv('Enfermedades_Tropicales.csv',sep=';', mode='a', index=False, header=False, encoding='latin-1')