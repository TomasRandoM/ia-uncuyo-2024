## TP 7 - Introducción a Machine Learning
**Alumno: Tomás Rando**


##### 1) For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.


- a) Un método inflexible sería mejor ya que el flexible requiere de una gran cantidad de parámetros. Además, los modelos flexibles pueden conducir al fenómeno de overfitting


- b) Al contrario que en el punto anterior, el mejor sería un método flexible, ya que, como se mencionó, este se beneficia de un gran número de parámetros. Gracias a esto, el método flexible puede lograr obtener una forma más cercana a la verdadera forma de f.
- c)  Si la relación entre los predictores y las respuestas son altamente no-lineales, el mejor método sería un modelo flexible, ya que estos son mejores en capturar las relaciones no-lineales.
- d) Si la varianza del error es muy alta, el mejor método sería uno más inflexible, ya que los métodos flexibles tienden a aumentar la varianza, lo que disminuye la precisión.
##### 2) Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.


- a) Estamos ante un problema de regresión y estamos interesados en la inferencia (ya que queremos entender los factores que afectan el salario del CEO). n = 500, p = 4.
- b) Es un problema de clasificación y estamos interesados en la predicción (Si será exitoso o no). n = 20, p = 14.
- c) Es un problema de regresión y estamos interesados en la predicción. n = 48, p = 4.


##### 5) What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?
Las ventajas de un método flexible son:
- Es más preciso, se ajusta mejor a los datos
- Es más adaptable, se adapta a diferentes datos que pueden no seguir una estructura definida.  
   
Las desventajas de los métodos flexibles frente a sus opuestos son:
- Necesita más parámetros para lograr ajustarse con precisión
- Pueden llevar al fenómeno de overfitting


Generalmente, cuando se está interesado en inferir, se utilizan métodos más inflexibles, ya que son más "interpretables", en cambio, si se está interesado en la predicción, se suele preferir métodos flexibles.


##### 6) Describe the diﬀerences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?


En los enfoques paramétricos se asume la forma de la función (Por ejemplo, una f lineal) y se reduce el problema a estimar los coeficientes. Entonces, este enfoque será más simple o sencillo, sin embargo, una gran desventaja es que generalmente el modelo no será igual a la verdadera forma de f, y, si es muy diferente, la estimación será pobre. En los enfoques no-paramétricos no se asume la forma de f, si no que se busca una estimación de f que se acerque a los datos lo más posible sin ser demasiado compleja o irregular. La ventaja de este último es que se puede ajustar a muchas más formas posibles de f, sin embargo, tiene la desventaja que es necesario un gran número de observaciones.


##### 7) The table below provides a training data set containing six observations, three predictors, and one qualitative response variable. (TABLE). Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.


- a)
  | Obs | Dist Eucl |
  |-----| ----------|
  | 1   |   3       |
  | 2   |   2       |
  | 3   |\(\sqrt{10}\)|
  | 4   |\(\sqrt{5}\)|
  | 5   |\(\sqrt{2}\)|
  | 6   |\(\sqrt{3}\)|




- b) Cuando K=1 la predicción será Green, esto es puesto que el vecino más cercano es el dado en la observación 5, cuya respuesta es Green.
- c) Con K=3 la predicción será Red, esto es debido a que los 3 vecinos más cercanos son los dados en las observaciones 2, 5 y 6, de estos, 2 de 3 son Red, por lo tanto, la predicción será ese mismo valor.
- d) Esperaríamos que el valor de K sea chico, esto es debido a que un valor pequeño ayuda a capturar la gran cantidad de variaciones mejor, ya que toma decisiones basadas en los datos muy cercanos. Además, al tomar los puntos más cercanos se pueden representar mejor los patrones locales con sus complejidades.

