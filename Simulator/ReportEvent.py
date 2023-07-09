from Enums.ConnectionStatus import ConnectionStatus
from Environment.WirelessNetwork import WirelessNetwork
from sortedcontainers import SortedList
from Const import Const
from Simulator.SimulationVariables import SimulationVariables


class ReportEvent:
    device_id: int = None
    time: int = 0  # time of execution

    def __init__(self, device_id: int, time: int, s1_generator, s2_generator) -> None:
        self.time = time
        self.device_id = device_id
        self.s1_generator = s1_generator
        self.s2_generator = s2_generator

    def execute(self, wireless_network: WirelessNetwork, event_list: SortedList):

        # return user by id
        user = wireless_network.get_user(self.device_id)

        # move user
        user.move(self.time)

        # calculate user power
        user.calculateAllPowers(sA=self.s1_generator.generate_random_number(),
                                sB=self.s2_generator.generate_random_number())

        if user.actualConnected == ConnectionStatus.stationA and user.power_A - user.power_B <= -Const.DELTA:
            user.suddenDisconnection = True
            user.actualConnected = ConnectionStatus.disconected
        elif user.actualConnected == ConnectionStatus.stationB and user.power_B - user.power_A <= -Const.DELTA:
            user.suddenDisconnection = True
            user.actualConnected = ConnectionStatus.disconected
        elif user.actualConnected == ConnectionStatus.stationA and user.power_A - user.power_B <= -int(SimulationVariables.a):
            user.handoverCounter += 1
            if user.handoverCounter == 5:
                user.changeStatus(ConnectionStatus.stationB)
                user.changedStation = True
                user.baseChanges += 1
        elif user.actualConnected == ConnectionStatus.stationB and user.power_B - user.power_A <= -int(SimulationVariables.a):
            user.handoverCounter += 1
            if user.handoverCounter == 5:
                user.changeStatus(ConnectionStatus.stationA)
                user.changedStation = True
                user.baseChanges += 1
        elif user.position >= Const.DISTANCE:
            user.actualConnected = ConnectionStatus.disconected
        else:
            user.handoverCounter = 0
            user.changedStation = False

        if user.actualConnected != ConnectionStatus.disconected:
            event_list.add(ReportEvent(device_id=self.device_id, time=self.time + 20, s1_generator=self.s1_generator,
                                       s2_generator=self.s2_generator))

        return user
