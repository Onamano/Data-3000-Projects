# This is a Unit test specifically for fcfs_algorithm.py

import unittest
from fcfs_algorithm import FCFSAlgorithm

# Creating a fake interface to test the FCFS algorithm, mimicking the interface from queue_interface and initializing variables to be used by the fake processes
class MockProcess:
    def __init__(self, arrivalTime, burstTime):
        self.arrival_time = arrivalTime
        self.burst_time = burstTime
        self.waiting_time = None
        self.turnaround_time = None

    # Creates an instance for the arrival time
    def get_arrival_time(self):
        return self.arrival_time

    # Creates an instance for the waiting time
    def set_waiting_time(self, waitingTime):
        self.waiting_time = waitingTime

    # Creates an instance for the turnaround time
    def set_turnaround_time(self, turnaroundTime):
        self.turnaround_time = turnaroundTime

# Creating a fake queue
class MockQueue:
    def __init__(self, processes):
        self.items = processes

    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        return self.items.pop(0)

#Verifies the algorithm is correctly ordering the processes
class TestFCFS(unittest.TestCase):
    def test_fcfs(self):
        # Creating a mock instance to test the algorithm
        mockInstance = FCFSAlgorithm()

        # Creating fake processes to denote the arrival and burst times
        process1 = MockProcess(arrivalTime=0, burstTime=5)
        process2 = MockProcess(arrivalTime=2, burstTime=3)

        # Appending mock procceses to the mock queue
        fakeQueue = MockQueue([process1, process2])

        # Execution
        mockExecution = mockInstance.run(fakeQueue)

        # Process verification. Should show waiting time as 0 and turnaround time as 5
        self.assertEqual(process1.waiting_time, 0)
        self.assertEqual(process1.turnaround_time, 5)

        # Process 2 verification. Should show waiting time as 3 and turnaround time as 6
        self.assertEqual(process2.waiting_time, 3)
        self.assertEqual(process2.turnaround_time, 6)

if __name__ == '__main__':
    unittest.main()
