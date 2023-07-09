import random
import matplotlib.pyplot as plt


class UniformGenerator:
    def __init__(self, seed):
        random.seed(seed)  # initialize new seed

    def generate_random_number(self):
        return random.uniform(5, 50)  # generate new random between 5 to 50 (velocity)

    def plot_samples(self, num_samples):
        samples = [self.generate_random_number() for _ in range(num_samples)]  # generate selected number od values

        # tworzenie wykresu
        plt.hist(samples, bins=45, density=True, alpha=0.75)
        plt.xlim(5, 50)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Normal Distribution')
        plt.grid(True)
        plt.show()
