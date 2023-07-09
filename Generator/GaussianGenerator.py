import random
import matplotlib.pyplot as plt


class GaussianGenerator:
    def __init__(self, seed):
        random.seed(seed)  # initialize new seed

    def generate_random_number(self):
        return random.gauss(0, 4)  # Mu = 0, Sigma = 4

    def plot_samples(self, num_samples):
        samples = [self.generate_random_number() for _ in range(num_samples)]

        # create chart
        plt.hist(samples, bins='auto', density=True, alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Gaussian Distribution')
        plt.grid(True)
        plt.show()
