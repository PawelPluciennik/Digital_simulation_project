import random
import string


class KeyGenerator:
    def __init__(self, length: int = 50):
        self.length = length

    def generate_key(self):
        characters = string.ascii_letters + string.digits
        key = ''.join(random.choice(characters) for _ in range(self.length))
        return key




# from Const import Const
#
#
# class KeyGenerator:
#
#     def __init__(self, kernel):
#         self.kernel = kernel
#
#     def generate_random_number(self):
#         h = self.kernel / Const.kQ
#         self.kernel = Const.kA * (self.kernel - Const.kQ * h) - Const.kR * h
#         if self.kernel < 0:
#             self.kernel = self.kernel + int(Const.kM)
#         return self.kernel / Const.kM
