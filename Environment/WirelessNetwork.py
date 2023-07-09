from Environment.User import User
from Const import Const
from Simulator.SimulationVariables import SimulationVariables


class WirelessNetwork:

    def __init__(self):
        self.buffer = []
        self.no_users = 0
        self.users_in_system = 0

    def initialize(self):
        self.buffer = []
        self.no_users = 0
        self.users_in_system = 0

    def generate_packet(self, velocity, start_time):
        if self.users_in_system >= Const.N:
            SimulationVariables.queue += 1
            return -1
        else:
            self.no_users += 1
            self.users_in_system += 1
            self.buffer.append(User(self.no_users, velocity=velocity, start_time=start_time))

            # Use number of users as user ID
            return self.no_users

    def get_user(self, id):
        for user in self.buffer:
            if user.id == id:
                return user

    def remove_user(self, id):
        for user in self.buffer:
            if user.id == id:
                self.buffer.remove(user)
                self.users_in_system -= 1
                break
