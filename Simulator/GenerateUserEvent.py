from Simulator.ReportEvent import ReportEvent
from Environment.WirelessNetwork import WirelessNetwork
from sortedcontainers import SortedList


class GenerateUserEvent:
    time: int = 0  # time of execution

    def __init__(self, time: int, velocity_generator, user_time_generator) -> None:
        self.time = time
        self.velocity_generator = velocity_generator
        self.user_time_generator = user_time_generator

    def execute(self, wireless_network: WirelessNetwork, event_list: SortedList, s1_generator, s2_generator):

        # add statistics
        id = wireless_network.generate_packet(self.velocity_generator.generate_random_number(), start_time=self.time)

        # generate new event
        time = self.user_time_generator.generate_random_number() + self.time
        event_list.add(GenerateUserEvent(time=time, velocity_generator=self.velocity_generator, user_time_generator=self.user_time_generator))

        # id == -1 -> system is full
        if id != -1:
            # generate user report event
            # print(f'Generated user with id {id}')
            event_list.add(ReportEvent(device_id=id, time=self.time + 20, s1_generator=s1_generator,
                                       s2_generator=s2_generator))