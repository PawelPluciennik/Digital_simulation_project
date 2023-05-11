from Enums.ConnectionStatus import ConnectionStatus
from Const import Const

class User:
    def __init__(self, velocity, power_a, power_b):
        self.id = id(self)
        self.position = Const.START_DISTANCE
        self.velocity = velocity
        self.power_A = power_a
        self.power_B = power_b
        self.actualConnected = ConnectionStatus.notConnected
        self.isConnected = False

    def changeStatus(self, status):
        self.actualConnected = status
        return

    def disconnect(self):
        self.changeStatus(ConnectionStatus.disconected)
