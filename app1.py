import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Function to compute dot product + bias
def neuron_output(inputs, weights, bias):
    weighted_sum = bias
    for input_value, weight in zip(inputs, weights):
        weighted_sum += input_value * weight
    output = sigmoid(weighted_sum)
    return output

# Prediction function
def predict(temp, duration):
    # Inputs
    inputs = [temp, duration]

    # Hidden layer: 3 neurons
    hidden_weights = [
        [1.2, 1.4],  # weights for neuron 1
        [1.5, 2.0],  # weights for neuron 2
        [2.0, 2.5]   # weights for neuron 3
    ]
    hidden_biases = [0.0, -1.0, 0.5] 

    # Calculate hidden layer outputs
    hidden_outputs = []
    
    for weights, bias in zip(hidden_weights, hidden_biases):
        output = neuron_output(inputs, weights, bias)
        hidden_outputs.append(output)

    # Output layer: 1 neuron
    output_weights = [1.5, 1.2, 1.0]  # Adjusted weights for output layer
    output_bias = -1.5  # Strong negative bias to push output lower

    final_output = neuron_output(hidden_outputs, output_weights, output_bias)

    # Apply threshold
    prediction = 1 if final_output >= 0.5 else 0

    return prediction, final_output

# Take input from user
temperature = float(input("Enter roasting temperature (°C): "))
duration = float(input("Enter roasting duration (minutes): "))

# Normalizing values
temp_norm = (temperature - 100) / (250 - 100)
duration_norm = (duration - 5) / (20 - 5)

# Predict result
pred, probability = predict(temp_norm, duration_norm)

# Show result
print(f"\nPrediction: {'Good Roast' if pred == 1 else 'Bad Roast'}")
print(f"Probability score: {probability:.4f}")