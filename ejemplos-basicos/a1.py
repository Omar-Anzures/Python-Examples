import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 

import random 

#se crea la grafica inicial

tirosdados = [random.randrange(1,7)for i in range(600)]
valores,frecuencias =  np.unique(tirosdados, return_counts= True)

# ventana y etiqueta de ejes
titulo =  f'Resultados de tirar los dados {len(tirosdados)} veces'
sns.set_style('whitegrid')
axes = sns.barplot(x = valores, y = frecuencias, palette = 'bright')

#titulo y titulo de x,y
axes.set_title(titulo)
axes.set(xlabel = 'Valores', ylabel = 'Frecuencias')

#le digo que el eje y se haga mas alto para que quepan los porcentages
axes.set_ylim(top=max(frecuencias)*1.10)

#porcentage de cada columna de la graifica
for bar,frecuencias in zip (axes.patches,frecuencias):
    text_x=bar.get_x()+bar.get_width()/2.0
    text_y=bar.get_height()
    text = f'{frecuencias:,}\n{frecuencias/len(tirosdados):.3%}'
    axes.text(text_x,text_y,text,fontsize = 11,ha='center',va='bottom')

#lo muestra en pantalla
plt.show()