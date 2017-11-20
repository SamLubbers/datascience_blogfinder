from blog_classifier.classifier import *

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

correct_negative_predictions = cm[0, 0]
correct_positive_predictions = cm[1, 1]
total_correct_predictions = correct_negative_predictions + correct_positive_predictions
test_set_size = len(y_test)

accuracy = total_correct_predictions / test_set_size

print('accuracy of our data science blog classifier is: %f' % accuracy)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier,
                             X = X_train,
                             y = y_train,
                             cv = 10)

print('accruacy with cross validations is: %f, with a standard error of %f' %
      (accuracies.mean(), accuracies.std()))
