from sklearn.model_selection import GridSearchCV
import numpy as np

# Define a function to maximize (example: f(x, y) = -(x^2 + y^2))
def maximize_function(x, y):
    return -(x**2 + y**2)

# Create grids of possible values for x and y
x_grid = np.linspace(-10, 10, 100)
y_grid = np.linspace(-10, 10, 100)
param_grid = {'x': x_grid, 'y': y_grid}

# Convert the maximization problem to a minimization problem by negating the function
def negated_function(x, y):
    return -maximize_function(x, y)

# Create a grid search object for optimization
grid_search = GridSearchCV(estimator=None, param_grid=param_grid, scoring=negated_function)

# Fit the grid search
grid_search.fit(X=None, y=None)

# Get the results with the maximized values (by negating them)
maximized_x = grid_search.best_params_['x']
maximized_y = grid_search.best_params_['y']
maximized_value = -grid_search.best_score_

print(f"Maximized x: {maximized_x:.4f}")
print(f"Maximized y: {maximized_y:.4f}")
print(f"Maximized value: {maximized_value:.4f}")
