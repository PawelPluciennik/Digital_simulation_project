from Simulator.MainLoop import MainLoop
from Simulator.SimulationVariables import SimulationVariables

# main_loop = []
# if __name__ == "__main__":
#     for i in range(10):
#         SimulationVariables.choice = i+1
#
#         SimulationVariables.a = 5
#
#         SimulationVariables.l = 0.0007
#
#
#         print('Started Simulation')
#         main_loop.append(MainLoop())
#         main_loop[i].run(300)
#
#         SimulationVariables.a = 0
#         SimulationVariables.l = 0
#         SimulationVariables.queue = 0
#         SimulationVariables.suddenDisconnectionCounter = 0
#         SimulationVariables.disconnected = 0
#         SimulationVariables.handOverCounter = 0
#         SimulationVariables.choice = 0


if __name__ == "__main__":
    print('Enter seed folder:')
    SimulationVariables.choice = input()

    print('Enter alpha:')
    SimulationVariables.a = input()

    print('Enter lambda:')
    SimulationVariables.l = input()

    print('Started Simulation')
    main_loop = MainLoop()
    main_loop.run(200)
