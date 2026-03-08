#process.py

class Process:
    """
    This class represents a single process in the FCFS sheduling, storing data for one process
    Attributes: 
    process_id (string): This is a unique name/identifier for the process (P1)
    arrival_time (int): The time at which the process arrives
    burst_time (int): This is the CPU time required to complete the process
    waiting_time (int): The time process spent in queue 
    turnaround_time (int): Total time spent from arrival to completion of process

    """
    def __init__(self, process_id, arrival_time, burst_time):
        """
        Creating a Process object

        """
        self.process_id = process_id #Stores the unique process identifier
        self.arrival_time = arrival_time #Stores time process arrives
        self.burst_time = burst_time #Stores CPU burst time

        #Will be calculated later by FCFS Algorithm
        self.waiting_time = 0
        self.turnaround_time = 0

    #Setting the waiting time for process
    #Allows for FCFS algorithm to update later
    def set_waiting_time(self, waiting_time):
        self.turnaround_time = waiting_time
    
    #Setter method for the turnaround time
    #FCFS algorithm will update later
    def set_turnaround_time(self, turnaround_time):
        self.turnaround_time = turnaround_time

    #Getter method for process ID, acts as reference to specific instance, calling the method
    def get_process_id(self):
        return self.process_id
    
    #Getter method for arrival time
    def get_arrival_time(self):
        return self.arrival_time
    
    #Getter method for waiting time
    def get_waiting_time(self):
        return self.waiting_time
    
    #Getter method for turnaround time
    def get_turnaround_time(self):
        return self.turnaround_time
    
    #String method
    #This will control exactly what gets displayed when you print a Process object
    def __str__(self):
        return (
            f"Process ID:{self.process_id}"
            f"Arrival Time:{self.arrival_time}"
            f"Burst Time: {self.burst_time}"
            f"Waiting Time: {self.waiting_time}"
            f"Turnaround Time: {self.turnaround_time}"
        )
