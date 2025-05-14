import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Function to compute dot product + bias
# This function calculates the output of a single neuron
def neuron_output(inputs, weights, bias):
    # Start with the bias value
    weighted_sum = bias

    # Add each input multiplied by its corresponding weight
    for input_value, weight in zip(inputs, weights):
        weighted_sum += input_value * weight

    # Pass the weighted sum through the sigmoid activation function
    output = sigmoid(weighted_sum)

    # Return the final output of the neuron
    return output

# Prediction function
def predict(temp, duration):
    # Inputs
    inputs = [temp, duration]

    # Hidden layer: 3 neurons
    hidden_weights = [
        [0.2, 0.4],  # weights for neuron 1
        [0.3, 0.7],  # weights for neuron 2
        [0.6, 0.5]   # weights for neuron 3
    ]
    hidden_biases = [0.1, -0.3, 0.2]

    # Calculate hidden layer outputs
    hidden_outputs = []
    for weights, bias in zip(hidden_weights, hidden_biases):
        output = neuron_output(inputs, weights, bias)
        hidden_outputs.append(output)

    # Output layer: 1 neuron
    output_weights = [0.5, 0.3, 0.2]
    output_bias = -0.1

    final_output = neuron_output(hidden_outputs, output_weights, output_bias)

    # Apply threshold
    prediction = 1 if final_output >= 0.5 else 0

    return prediction, final_output

# Take input from user
temperature = float(input("Enter roasting temperature (°C): "))
duration = float(input("Enter roasting duration (minutes): "))

# Predict result
pred, probability = predict(temperature, duration)

# Show result
print(f"\nPrediction: {'Good Roast' if pred == 1 else 'Bad Roast'}")
print(f"Probability score: {probability:.4f}")