import random
import numpy as np
import matplotlib.pyplot as plt


class ExponentialGenerator:
    def __init__(self, seed, lambda_value: float = 1):
        self.lambda_value = lambda_value
        random.seed(seed)  # initialize new seed

    def generate_random_number(self):
        return random.expovariate(float(self.lambda_value))  # lambda param

    def plot_samples(self, num_samples):
        samples = [self.generate_random_number() for _ in range(num_samples)]

        # tworzenie wykresu
        plt.hist(samples, bins='auto', density=True, alpha=0.75)
        plt.xlim(0, np.max(samples))
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(f'Exponential Distribution for λ = {self.lambda_value}')
        plt.grid(True)
        plt.show()