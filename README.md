# **Coffee Roasting Prediction using Neural Network**

This project demonstrates a **simple neural network** built from scratch in Python to predict whether a coffee roast is "Good" or "Bad" based on the **roasting temperature** and **duration**. The neural network consists of:

* **1 hidden layer** with 3 neurons.
* **1 output layer** that determines if the roast is "Good" or "Bad".
* **Sigmoid activation function** is used to make the prediction output between 0 and 1.

---

## **How It Works:**

### **1. Input:**

The neural network takes two inputs:

* **Roasting Temperature**: The temperature at which coffee beans are roasted (in Celsius).
* **Roasting Duration**: The time for which the coffee is roasted (in minutes).

### **2. Hidden Layer:**

The network processes these inputs in a hidden layer with 3 neurons. Each neuron in the hidden layer has its own set of weights and biases.

### **3. Output Layer:**

The output layer has 1 neuron that takes the output from the hidden layer, processes it, and uses a threshold value of **0.5**:

* If the output is greater than or equal to 0.5, the roast is predicted to be "Good".
* Otherwise, it’s predicted to be "Bad".

---

## **Getting Started:**

### **Prerequisites:**

* Python 3.x
* `math` library (This is built into Python, so no installation is needed!)

### **Installation:**

You can run this project locally by following these simple steps:

1. **Clone this repository** (if using Git):

   ```bash
   git clone https://github.com/Nayanpatel48/CoffeeRoasting.git
   cd coffee-roast-prediction
   ```

2. **Run the Python script**:

   ```bash
   python coffee_roast_prediction.py
   ```

---

## **How to Use:**

1. You will be prompted to input the **roasting temperature** (in °C) and **roasting duration** (in minutes).
2. The neural network will process these inputs and provide the output prediction:

   * **Good Roast** if the network predicts a value greater than or equal to 0.5.
   * **Bad Roast** if the network predicts a value below 0.5.
3. The program will also display the **probability score** indicating the certainty of the prediction (from 0 to 1).

---

## **Example Use Case:**

Let's assume you input the following values:

* **Temperature**: 220°C
* **Duration**: 15 minutes

The program might output something like this:

```
Prediction: Good Roast
Probability score: 0.8587
```

---

## **Code Overview:**

* **sigmoid(x)**: This function calculates the sigmoid activation value, which squashes the result to between 0 and 1.
* **neuron\_output(inputs, weights, bias)**: This function computes the output of a single neuron by calculating the weighted sum of the inputs and applying the sigmoid function.
* **predict(temp, duration)**: This is the main prediction function. It calculates the hidden layer outputs and computes the final output from the network using the given weights and biases.

---

## **Acknowledgments:**

* This project is built using basic concepts of neural networks, without using any machine learning libraries like TensorFlow or PyTorch.
* You can improve this model by training it on a dataset of roasting conditions and adjusting the weights and biases accordingly.

---

## **Future Improvements:**

* Use real data for training the neural network to make it more accurate.
* Implement additional hidden layers and neurons for more complexity.
* Use popular ML libraries (like TensorFlow or PyTorch) to improve model performance.

---

Feel free to modify and experiment with the code! 😊 Happy coding! 🚀