##### Alumno: Tomás Rando
###### A)

create_folds()
```
create_folds <- function(dataFrame, num) {
  indexes <- sample(1: nrow(dataFrame))
  folds <- split(indexes, cut(seq_along(indexes), breaks = num, labels = FALSE))
  names(folds) <- paste0("Fold", 1:num)
  return(folds)
}
```

cross_validation()

```
cross_validation <- function(dataFrame, num) {
  dataFrame$inclinacion_peligrosa <- as.factor(dataFrame$inclinacion_peligrosa)
  train_formula<-formula(inclinacion_peligrosa~ altura + diametro_tronco + seccion )

  folds <- create_folds(dataFrame, num)

  predicList <- list()
  matrixList <- list()

  for (i in 1:num) {
    indexes <- folds[[i]]
    trainData <- dataFrame[-indexes, ]
    valData <- dataFrame[indexes, ]
    
    tree_model<-rpart(train_formula,data=trainData)

	  p<-predict(tree_model,valData,type='class') 
    maAux <- new_confusion_matrix(valData$inclinacion_peligrosa, p)
    matrixList[[i]] <- maAux
	  predicList[[paste0("Fold", i)]] <- p
  }
  return(list(predictions = predicList, matrices = matrixList))
}
```

Al ver que creando un modelo utilizando los datos sin ninguna modificación, los resultados no eran los esperados, es decir, siempre se predecía 0, se utilizó oversampling y undersampling para mejorar las predicciones que se realizaban.  

La primera tabla nos muestra las métricas que se obtuvieron al crear el modelo utilizando los datos sin ningún tipo de modificación. Se puede observar una accuracy muy buena junto a una specificity perfecta, sin embargo, esto es debido a que el modelo siempre predecía "no" ya que las clases estaban completamente desbalanceadas, por ello, si predecía no, la mayoría de las veces estaría en lo correcto. Para obtener los resultados se utilizó una cantidad de folds igual a 10 y se utilizó el método de cross-validation
  | Métrica | Media| Desviación Estándar| 
  |----------| -------- | --------- | 
  | Accuracy | 0.887853002245806 | 0.00751913036297008|
  | Precision | NA | NA |
  | Sensitivity | 0 | 0 |
  | Specificity | 1 | 0 |
    

Para resolver el problema de los datos desbalanceados, primero se utilizó oversampling, es decir, con ayuda de la librería "ROSE" se crearon datos sintéticos de la clase minoritaria hasta igualar a la clase mayoritaria, de esta manera, los datos quedaron balanceados. Luego de realizar el balanceo, se probó con diferente cantidad de folds (5, 10, 15, 20, 100) y se observó que las mejores métricas fueron obtenidas utilizando 10, por lo tanto, la siguiente tabla nos muestra dichos resultados.

| Métrica | Media| Desviación Estándar| 
  |----------| -------- | --------- | 
  | Accuracy | 0.645984112974404 | 0.0174869676972611|
  | Precision | 0.609101681425415 | 0.0186329262351551 |
  | Sensitivity | 0.815265547494726 | 0.0182448737861955 |
  | Specificity | 0.476926857992091 | 0.0184987264924394 |

Podemos observar que la sensibilidad y la precisión mejoraron considerablemente, sin embargo, la especificidad y la exactitud disminuyeron.  

Para comparar oversampling, se realizó el mismo procedimiento pero con undersampling, nuevamente utilizando la librería "ROSE", de esta manera, se fueron eliminando datos aleatoriamente de la clase mayoritaria hasta tener la misma cantidad de datos de ambas clases. Para este caso, la mejor cantidad de folds fue de 20, por lo que se realizó la tabla teniendo en cuenta dicho valor.

| Métrica | Media| Desviación Estándar| 
  |----------| -------- | --------- | 
  | Accuracy | 0.659252738654147 | 0.0528427067863052|
  | Precision | 0.620831416338423 | 0.0628696399100482 |
  | Sensitivity | 0.807678002582221 | 0.067343833447339 |
  | Specificity | 0.509068724614991 | 0.0633189501964714 |

Se puede observar como las métricas son bastante similares, sin embargo, mejoró ligeramente la especificidad y la precisión mientras que la sensitividad empeoró levemente.  

En el contexto de nuestro problema de árboles con la inclinación peligrosa, nos interesa detectar particularmente los árboles que la tienen, ya que de esta manera se pueden prevenir ciertos accidentes. Por ello, el modelo realizado con oversampling, al tener la sensibilidad más alta, sería el más adecuado para este. Sin embargo, se debe tener en cuenta que este modelo tiene una ligera mayor cantidad de falsos positivos, por lo que habría que evaluar que tanta importancia se le da a estos.