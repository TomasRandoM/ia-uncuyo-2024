# TP 7 - B
### Alumno: Tomás Rando
#### Descripción del proceso de preprocesamiento (si es que lo hubiera) Como por ejemplo: Se eliminaron variables? Se crearon nuevas? Se normalizaron valores (0,1)
Al ver que ambas clases estaban mal distribuidas, se realizaron algunas mejoras para intentar mejorar el modelo realizado. Primero, se eliminaron las filas pertenecientes a una especie que apareciera una sola vez en todo el conjunto de datos. Luego, se realizó undersampling eliminando filas del conjunto mayoritario hasta lograr una cantidad igual a 7.6 * filas del minoritario. Para el mejor resultado obtenido se utilizaron las siguientes columnas: especie, circ_tronco_cm, diametro_tronco, lat, long y seccion. Esta elección fue derivada de múltiples pruebas y se determinó que la adición o sustracción de parámetros conllevaría a decrementar la métrica lograda.

#### Resultados obtenidos sobre el conjunto de validación
Para obtener el mejor resultado no se utilizó un conjunto de validación, pues el conjunto entero de los datos fue utilizado para entrenar al modelo. Sin embargo, se hicieron muchas pruebas antes utilizando cross validation para determinar las columnas, cantidad de arboles que serían utilizados y parámetros útiles. En estas pruebas, el resultado fue de 0.7878.  
#### Resultados obtenidos en Kaggle 
En Kaggle el resultado obtenido fue de 0.78231 en la tabla pública. 

#### Descripción detallada del algoritmo propuesto
El algoritmo utilizado fue "Random Forest" de la librería Ranger. Para entrenar el modelo, se utilizaron las columnas especie, circ_tronco_cm, diametro_tronco, lat, long y seccion. Además se utilizó, luego de haber probado con cantidades inferiores y superiores, un número de árboles igual a 3000. Cabe aclarar que los datos utilizados fueron preprocesados realizando undersampling, pues se vió que daba mejores resultados. Por otro lado, se transformaron a categóricas las variables altura, diametro_tronco, especie y sección. Y también se modificaron algunos parámetros como el mtry en 2, el min.node.size en 3, el sample.fraction en 0.5 y el max.depth en 16. Otra modificación que se realizó es que se le otorgó pesos a las variables de inclinacion_peligrosa. Por último, para lograr la reproducibilidad, se seteó la semilla como "2024". Todo el código puede ser visualizado en el archivo kaggleChallengeDef.Rmd y las pruebas realizadas en el archivo kaggleChallengeTests.Rmd.
```
tree_model<- ranger(inclinacion_peligrosa ~ especie + circ_tronco_cm + diametro_tronco + lat + long  + seccion, data = dataUnder, num.trees = 3000, num.threads = 4, mtry = 2, min.node.size = 3, sample.fraction = 0.5, case.weights = dataUnder$weights, max.depth = 16)
```
