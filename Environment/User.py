import math

from Const import Const
from Enums.ConnectionStatus import ConnectionStatus


def calculatePower(distance, s):  # distance [m], s [dB]
    power = 4.51 - 22 * math.log10(distance) + s  # Power [dBm]
    return power


class User:

    def __init__(self, id: int, velocity: float, start_time: int):
        self.id: int = id
        self.position = Const.START_DISTANCE
        self.velocity: float = velocity
        self.actualConnected = ConnectionStatus.stationA
        self.power_A = 0
        self.power_B = 0
        self.handoverCounter = 0
        self.start_time = start_time
        self.changedStation: bool = False
        self.suddenDisconnection: bool = False
        self.baseChanges = 0

    def changeStatus(self, status):
        self.actualConnected = status
        return

    def disconnect(self):
        self.changeStatus(ConnectionStatus.disconected)

    def calculateAllPowers(self, sA, sB):
        self.power_A = calculatePower(self.position, sA)
        self.power_B = calculatePower(abs(Const.DISTANCE - self.position), sB)

    def move(self, time):
        self.position = Const.START_DISTANCE + (self.velocity * (time - self.start_time) * 1 / 1000)
