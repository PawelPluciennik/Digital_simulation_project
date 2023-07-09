import os
import csv

from Environment.WirelessNetwork import WirelessNetwork
from Generator.UniformGenerator import UniformGenerator
from Generator.GaussianGenerator import GaussianGenerator
from Generator.ExponentialGenerator import ExponentialGenerator
from Simulator.GenerateUserEvent import GenerateUserEvent
from sortedcontainers import SortedList
from Simulator.SimulationVariables import SimulationVariables

from Enums.ConnectionStatus import ConnectionStatus


def read_keys_from_folder(choice):
    keys = []
    folder_path = f"Seeds/KeyFolder{choice}"
    keys_file_path = os.path.join(folder_path, "keys.txt")

    with open(keys_file_path, "r") as keys_file:
        for line in keys_file:
            key = line.strip()
            keys.append(key)

    return keys

def save_to_csv(user, wireless_network):
    lables = ['User_id', 'Actual_connected_to', 'Actual_location', 'Handover_counter', 'Users_in_system', 'System_queue', 'Disconnected_users']
    values = [user.id, user.actualConnected, user.position, user.baseChanges, wireless_network.users_in_system, SimulationVariables.queue, SimulationVariables.disconnected]
    file_name = f'results_seed{SimulationVariables.choice}_l{SimulationVariables.l}_a{SimulationVariables.a}.csv'

    if not os.path.isfile(file_name) or os.stat(file_name).st_size == 0:
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(lables)
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(values)
        # print("OK")


class MainLoop:
    wireless_network: WirelessNetwork
    event_list: SortedList
    velocity_generator: UniformGenerator
    gauss_s1_generator: GaussianGenerator
    gauss_s2_generator: GaussianGenerator
    user_time_generator: ExponentialGenerator

    def __init__(self) -> None:
        self.wireless_network = WirelessNetwork()
        self.event_list = SortedList(key=lambda x: x.time)

        keys = read_keys_from_folder(SimulationVariables.choice)

        self.velocity_generator = UniformGenerator(keys[0])
        self.gauss_s1_generator = GaussianGenerator(keys[1])
        self.gauss_s2_generator = GaussianGenerator(keys[2])
        self.user_time_generator = ExponentialGenerator(seed=keys[3], lambda_value=SimulationVariables.l)

    def run(self, max_users):

        self.wireless_network.initialize()
        self.event_list.add(GenerateUserEvent(
            time=0,
            velocity_generator=self.velocity_generator,
            user_time_generator=self.user_time_generator)
        )

        # MAIN LOOP
        time = 0

        # time events
        while SimulationVariables.disconnected < max_users:
            # time = self.event_list[0].time
            # print(f'Simulation time:{time} ms')
            event = self.event_list.pop(index=0)

            if isinstance(event, GenerateUserEvent):
                event.execute(self.wireless_network, self.event_list,
                              s1_generator=self.gauss_s1_generator,
                              s2_generator=self.gauss_s2_generator
                              )
            else:
                user = event.execute(self.wireless_network, self.event_list)

                #  conditional events
                #  user left
                if user.actualConnected == ConnectionStatus.disconected:
                    SimulationVariables.disconnected += 1
                    #  20 db diff
                    if user.suddenDisconnection == True:
                        SimulationVariables.suddenDisconnectionCounter += 1
                    if SimulationVariables.disconnected > 60:
                        save_to_csv(user, self.wireless_network)
                    self.wireless_network.remove_user(user.id)
                #  user changed station
                elif user.changedStation == True:
                    SimulationVariables.handOverCounter += 1

        print(
            f'Users in system:{self.wireless_network.users_in_system}, disconnected: {SimulationVariables.disconnected}, sudden {SimulationVariables.suddenDisconnectionCounter}, changed {SimulationVariables.handOverCounter}, queue {SimulationVariables.queue}')

        # def save_keys_to_file(array):
        #       with open('klucze.txt', 'w') as file:
        #           for value in array:
        #               file.write(f'Klucz {array.index(value) + 1}: ' + str(value) + '\n')
        #       print(f"Utworzono plik z kluczami o nazwie klucze.txt")