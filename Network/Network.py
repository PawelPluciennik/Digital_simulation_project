import math
from User.User import User
from Enums.ConnectionStatus import ConnectionStatus


class Network:
    def changeStation(user):
        if (user.actualConnected == ConnectionStatus.stationA):
            status = ConnectionStatus.stationB
        else:
            status = ConnectionStatus.stationA
        user.changeStatus(status)
        return
