from sklearn.model_selection import GridSearchCV

# Define the hyperparameter grid
param_grid = {'param1': [value1, value2], 'param2': [value3, value4]}

# Create the model
model = create_neural_network()

# Use GridSearchCV to find the best combination
grid_search = GridSearchCV(model, param_grid, scoring='accuracy', cv=3)
grid_search.fit(X_train, y_train)

# Access the best hyperparameters
best_params = grid_search.best_params_
