random_values = np.random.rand(100) 
normalized_values = (random_values - random_values.min()) / (random_values.max() - random_values.min())
print(normalized_values)
