import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import GridSearchCV
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

# Create a simple dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the create_neural_network function
def create_neural_network(param1=32, param2=16, input_dim=20, output_dim=1):
    model = Sequential()
    model.add(Dense(units=param1, activation='relu', input_dim=input_dim))
    model.add(Dense(units=param2, activation='relu'))
    model.add(Dense(units=output_dim, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Wrap the Keras model using KerasClassifier
neural_network = KerasClassifier(build_fn=create_neural_network, epochs=10, batch_size=32, verbose=0)

# Define the hyperparameter grid
param_grid = {'param1': [16, 32, 64], 'param2': [8, 16, 32]}

# Use GridSearchCV for hyperparameter optimization
grid_search = GridSearchCV(neural_network, param_grid=param_grid, scoring='accuracy', cv=3)
grid_result = grid_search.fit(X_train, y_train)

# Access the best hyperparameters and the best model
best_params = grid_result.best_params_
best_model = grid_result.best_estimator_

# Evaluate the best model on the test set
test_accuracy = best_model.score(X_test, y_test)

print("Best Hyperparameters:", best_params)
print("Test Accuracy:", test_accuracy)
