import math
class Channel:
  def calculatePower(distance, s): # distance [m], s [dB]
    power = 4.51 - 22 * math.log10(distance) + s # Power [dBm]
    print(power)
    return power

