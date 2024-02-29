import tensorflow as tf
import numpy as np

class CelsiusFahrenheitModel:
    model = {}

    def __init__(self):
        self.train()
        
    def train(self):
        celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
        fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

        layer = tf.keras.layers.Dense(units=1, input_shape=[1])
        model = tf.keras.Sequential([layer])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )

        print("Starting traininig...")
        model.fit(celsius, fahrenheit, epochs=1000, verbose=False)
        print("Training ended.")

        self.model = model
    
    def predict(self, input):
        result = self.model.predict(x=np.array([input], dtype=float))

        return result[0][0].__str__()

    