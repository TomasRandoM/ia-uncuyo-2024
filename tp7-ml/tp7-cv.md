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
  train_formula<-formula(inclinacion_peligrosa~diametro_tronco + altura)

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


  | Métrica | Media| Desviación Estándar| 
  |----------| -------- | --------- | 
  | Accuracy | 0.887853002245806 | 0.00751913036297008|
  | Precision | NA | NA |
  | Sensitivity | 0 | 0 |
  | Specificity | 1 | 0 |