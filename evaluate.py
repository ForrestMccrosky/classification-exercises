ef run_metrics(model, data_set):
    """
    This function takes in a model and ouputs metrics. 
    model = name of class model
    data_set = train, validate, test (AS A STRING)
    Will output the Precision Score, the classification report, and the confusion matrix
    It is advisable to print the name of the model you're working with before hand for clarity
    i.e. print('Metrics for Model 1 with Train data\n')
    """
    if data_set == 'train':
        score = model.score(X_train, y_train)
        X = X_train
        df = train
    if data_set == 'validate':
        score = model.score(X_validate, y_validate)
        X = X_validate
        df = validate
    if data_set == 'test':
        score = model.score(X_test, y_test)
        X = X_test
        df = test
    print(f'{data_set} Set Precision Score: {score:.2%}')
    class_report = classification_report(df.survived, model.predict(X), zero_division=True)
    print('-------------------------------')
    print(f'Classification report')
    print(class_report)
    print ('-------------------------------')
    print('Confusion Matrix')
    print(confusion_matrix(df.survived, model.predict(X)))