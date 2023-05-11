import time
from User.User import User
from Queue.Queue import Queue
from Tree.Tree import Tree

stationA = Queue()
stationB = Queue()

tree1 = Tree()
user1 = User(1, 1, 1)


def generate_id():
    # Get the current time in seconds
    current_time = int(time.time())

    # Convert to hexadecimal and add some padding
    hex_id = hex(current_time)[2:].zfill(8)

    return current_time

while 1 != 0:
    # user1 = User(1, 2, 3)
    # user2 = User(3, 4, 5)

    # print(user1.id)
    # tree1.add(user1)
    # tree1.add(user2)
    # tree1.remove(user2.id)
    # tree1.print_tree()
    dupa = generate_id()

    print(dupa)

    time.sleep(0.1)