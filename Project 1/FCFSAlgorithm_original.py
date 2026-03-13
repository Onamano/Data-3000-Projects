# from Process import Process
# from QueueImplentation import QueueImplementation

# Test dataset dictionary
p1 = {"Arrival": 0, "Burst": 4},
p2 = {"Arrival": 1, "Burst": 3},
p3 = {"Arrival": 2, "Burst": 2},
p4 = {"Arrival": 3, "Burst": 6},
p5 = {"Arrival": 4, "Burst": 5}
testArray = [p1, p2, p3, p4, p5]


class FCFSAlgorithm:
    def FCFSAlgorithm():
        # Creates an empty dictionary object, then asks the user for input into the number of processes which will be added to the dictionary
        processDictionary = dict()
        print("\n")
        processNumber = int(input("Please enter the number of processes ► "))

        # Iterates through the processes, first creating variables for the Process ID, Arrival Time, and Burst Time. These are then added into an empty array. The array is then added to the dictionary using the Process ID as the key
        for index in range(processNumber):
            processID = "P" + str(index + 1)
            arrivalTime = int(input("Please enter the arrival time for process " + str(index+1) + " ► "))                   
            burstTime = int(input("Please enter the burst time for process "+ str(index+1) + " ► "))
            
            # Creates an array to hold the values for the arrival time and burst time of each process
            processArray = []
            processArray.append(arrivalTime)
            processArray.append(burstTime)
            processDictionary[processID] = processArray


        # Sorts the dictionary based on the arrival time of the process
        processDictionary = sorted(processDictionary.items(), key=lambda item: item[1][0])


        # Calculating the exit time for each process
        # Create an array for the exit times of all the processes
        exitTimeArray = []

        # Iterates through each process in the dictionary, setting the first process based on whether the index is 0
        for index in range(len(processDictionary)):
            if(index == 0):
                exitTimeArray.append(processDictionary[index][1][1])
            
            # Appends other processes in order (previous exit time + new burst time)
            else:
                exitTimeArray.append(exitTimeArray[index-1] + processDictionary[index][1][1])


        # Calculating the turnaround time for each process
        # Create an array for the turnaround time
        turnAroundTimeArray = []


        # Calculating the turnaround time and appending to the array, based on the calculation for exit time - arrival time
        for index in range (len(processDictionary)):
            turnAroundTimeArray.append(exitTimeArray[index] - processDictionary[index][1][0])


        # Calculating the waiting time for each process
        # Create an array to hold the wait times
        waitTimeArray = []

        # Appending the wait times into the array, based on the calculation for turnaround time - arrival time
        for index in range (len(processDictionary)):
            waitTimeArray.append(turnAroundTimeArray[index] - processDictionary[index][1][1])


        # Calculate the average wait time for all processes, essentially dividing the wait times by the number of processes for a rough average number
        averageWaitTime = 0
        for index in waitTimeArray:
            averageWaitTime += index
        averageWaitTime = (averageWaitTime / processNumber)


        # Calculates the average turnaround time for all processes, using the same formula we used to find the average waiting time
        averageTurnaroundTime = 0
        for index in turnAroundTimeArray:
            averageTurnaroundTime += index
        averageTurnaroundTime = (averageTurnaroundTime / processNumber)


        print("\n")
        for index in range(processNumber):
            print("Process ", processDictionary[index][0], " <<...>> Arrival Time ► ", processDictionary[index][1][0], " <<...>> Waiting Time ► ", waitTimeArray[index], " <<...>> Turnaround Time ► ", turnAroundTimeArray[index])
        print("\n")
        print("Average Waiting Time ► ", averageWaitTime)
        print("Average Turnaround Time ► ", averageTurnaroundTime)
    FCFSAlgorithm()





# References
# [1] https://www.askpython.com/python/examples/first-come-first-serve
# [2] https://codepal.ai/code-generator/query/KuETMQsU/python-code-for-fcfs-scheduling-algorithm
# [3] https://www.geeksforgeeks.org/operating-systems/program-for-fcfs-cpu-scheduling-set-1/
# [4] https://www.w3schools.com/python/python_dictionaries.asp


# Notes
# Need to calculate waiting time and turnaround time for each process as well as the avg waiting time and avg turnaround time
# Arrival time - when the process arrives in the queue
# Burst Time - Time when the process completes its execution
# Turnaround Time - The difference between the arrival time and the burst time (BT - AT)
# Waiting Time - The difference between turnaround time and burst time (TAT - BT)
# 
# 
#
