import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
    def __init__(self, k=3):
        self.k = k
    
    def fit(self, X, y):
        """
        Fit the k-NN model using the given training data.
        Parameters:
        X (array-like): Training data features, shape (n_samples, n_features).
        y (array-like): Training data labels, shape (n_samples,).
        Returns:
        None
        """
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        """
        Predict the class labels for the given input data.
        Parameters:
        X (array-like): Input data of shape (n_samples, n_features).
        Returns:
        list: Predicted class labels for each input sample.
        """
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self, x):
        """
        Predict the class label for a given input sample.
        Parameters:
        x (array-like): The input sample for which the class label is to be predicted.
        Returns:
        int: The predicted class label for the input sample.
        """
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]

        # Extract the labels of the k nearest neighbor training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Return the most common class label
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common