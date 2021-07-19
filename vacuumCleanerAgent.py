import random
class Environment(object):
    def init(self):
         # instantiate locations and conditions
         # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = {'A': '0', 'B': '0'}
     # randomize conditions in locations A and B     
        self.locationCondition['A'] = random.randint(0, 1)     
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def init(self, Environment):
        print(Environment.locationCondition)
         # Instantiate performance measurement
        Score = 0
         # place vacuum at random location
        vacuumLocation = random.randint(0, 1)
         # if vacuum at A
        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A.")
             # and Location A is Dirty.
            if Environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
                 # suck the dirt  and mark it clean
                Environment.locationCondition['A'] = 0
                Score += 1
                print("Location A has been Cleaned.")
                 # move to B
                print("Moving to Location B…")
                Score -= 1
                 # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                     # suck and mark clean
                    Environment.locationCondition['B'] = 0
                    Score += 1
                    print("Location B has been Cleaned.")
            else:
                 # move to B
                Score -= 1
                print("Moving to Location B…")
                 # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                     # suck and mark clean
                    Environment.locationCondition['B'] = 0
                    Score += 1
                    print("Location B has been Cleaned.")
        elif vacuumLocation == 1:
            print("Vacuum randomly placed at Location B.")         # and B is Dirty         
            if Environment.locationCondition['B'] == 1:             
                print("Location B is Dirty.")             # suck and mark clean             
                Environment.locationCondition['B'] = 0             
                Score += 1             
                print("Location B has been Cleaned.")             # move to A             
                Score -= 1             
                print("Moving to Location A...")             # if A is Dirty             
                if Environment.locationCondition['A'] == 1:                 
                    print("Location A is Dirty.")                 # suck and mark clean                 
                    Environment.locationCondition['A'] = 0               
                    Score += 1                 
                    print("Location A has been Cleaned.")         
            else:             # move to A             
                print("Moving to Location A...")             
                Score -= 1             # if A is Dirty             
                if Environment.locationCondition['A'] == 1:                 
                    print("Location A is Dirty.")                                 
                    Environment.locationCondition['A'] = 0                
                    Score += 1                 
                    print("Location A has been Cleaned.")     # done cleaning     
                    print(Environment.locationCondition)     
                    print("Performance Measurement: " + str(Score))

theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)

















# #INSTRUCTIONS
# #Enter LOCATION A/B in captial letters
# #Enter Status O/1 accordingly where 0 means CLEAN and 1 means DIRTY

# def vacuum_world():
#         # initializing goal_state
#         # 0 indicates Clean and 1 indicates Dirty
#     goal_state = {'A': '0', 'B': '0'}
#     cost = 0

#     location_input = input("Enter Location of Vacuum:") #user_input of location vacuum is placed
#     status_input = input("Enter status of " + location_input+":") #user_input if location is dirty or clean
#     status_input_complement = input("Enter status of other room:")
#     print("Initial Location Condition " + str(goal_state))

#     if location_input == 'A':
#         # Location A is Dirty.
#         print("Vacuum is placed in Location A")
#         if status_input == '1':
#             print("Location A is Dirty.")
#             # suck the dirt  and mark it as clean
#             goal_state['A'] = '0'
#             cost += 1                      #cost for suck
#             print("Cost for CLEANING A" + str(cost))
#             print("Location A has been Cleaned.")

#             if status_input_complement == '1':
#                 # if B is Dirty
#                 print("Location B is Dirty.")
#                 print("Moving right to the Location B. ")
#                 cost += 1                       #cost for moving right
#                 print("COST for moving RIGHT" + str(cost))
#                 # suck the dirt and mark it as clean
#                 goal_state['B'] = '0'
#                 cost += 1                       #cost for suck
#                 print("COST for SUCK " + str(cost))
#                 print("Location B has been Cleaned. ")
#             else:
#                 print("No action" + str(cost))
#                 # suck and mark clean
#                 print("Location B is already clean.")

#         if status_input == '0':
#             print("Location A is already clean ")
#             if status_input_complement == '1':# if B is Dirty
#                 print("Location B is Dirty.")
#                 print("Moving RIGHT to the Location B. ")
#                 cost += 1                       #cost for moving right
#                 print("COST for moving RIGHT" + str(cost))
#                 # suck the dirt and mark it as clean
#                 goal_state['B'] = '0'
#                 cost += 1                       #cost for suck
#                 print("Cost for SUCK" + str(cost))
#                 print("Location B has been Cleaned. ")
#             else:
#                 print("No action" + str(cost))
#                 print(cost)
#                 # suck and mark clean
#                 print("Location B is already clean.")

#     else:
#         print("Vacuum is placed in location B")
#         # Location B is Dirty.
#         if status_input == '1':
#             print("Location B is Dirty.")
#             # suck the dirt  and mark it as clean
#             goal_state['B'] = '0'
#             cost += 1  # cost for suck
#             print("COST for CLEANING " + str(cost))
#             print("Location B has been Cleaned.")

#             if status_input_complement == '1':
#                 # if A is Dirty
#                 print("Location A is Dirty.")
#                 print("Moving LEFT to the Location A. ")
#                 cost += 1  # cost for moving right
#                 print("COST for moving LEFT" + str(cost))
#                 # suck the dirt and mark it as clean
#                 goal_state['A'] = '0'
#                 cost += 1  # cost for suck
#                 print("COST for SUCK " + str(cost))
#                 print("Location A has been Cleaned.")

#         else:
#             print(cost)
#             # suck and mark clean
#             print("Location B is already clean.")

#             if status_input_complement == '1':  # if A is Dirty
#                 print("Location A is Dirty.")
#                 print("Moving LEFT to the Location A. ")
#                 cost += 1  # cost for moving right
#                 print("COST for moving LEFT " + str(cost))
#                 # suck the dirt and mark it as clean
#                 goal_state['A'] = '0'
#                 cost += 1  # cost for suck
#                 print("Cost for SUCK " + str(cost))
#                 print("Location A has been Cleaned. ")
#             else:
#                 print("No action " + str(cost))
#                 # suck and mark clean
#                 print("Location A is already clean.")

#     # done cleaning
#     print("GOAL STATE: ")
#     print(goal_state)
#     print("Performance Measurement: " + str(cost))


# vacuum_world()