import random
import math

def exp_distribution(lamda):
  return random.expovariate(lamda)

def gauss_distribution(mean, std_dev): #mean - średnia, std_dev - odchylenie standardowe podawane w dB
  # konwersja wartości odchylenia standardowego do wartości amplitudy
  std_dev = math.pow(10, std_dev/20)

  return random.gauss(mean, std_dev) 