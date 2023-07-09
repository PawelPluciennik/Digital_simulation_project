import os

from Generator.GaussianGenerator import GaussianGenerator
from Generator.UniformGenerator import UniformGenerator
from Generator.ExponentialGenerator import ExponentialGenerator

def read_keys_from_folder(choice):
    keys = []
    folder_path = f"Seeds/KeyFolder{choice}"
    keys_file_path = os.path.join(folder_path, "keys.txt")

    with open(keys_file_path, "r") as keys_file:
        for line in keys_file:
            key = line.strip()
            keys.append(key)

    return keys

def generate_charts(choice, l):
    keys = read_keys_from_folder(choice)
    num_samples = 100_000

    uniformGenerator = UniformGenerator(keys[0])
    uniformGenerator.plot_samples(num_samples=num_samples)

    gaussianGenerator = GaussianGenerator(keys[1])
    gaussianGenerator.plot_samples(num_samples=num_samples)

    exponentialGenerator = ExponentialGenerator(keys[3], lambda_value=l)
    exponentialGenerator.plot_samples(num_samples=num_samples)

print('Enter seed folder:')
choice = input()
print('Enter lambda:')
l = input()
generate_charts(choice, l)
