#test_process.py
#This file will test the Process class in process.py file using unittest module

import unittest
from process import Process

#This class will group all tests together
class TestProcess(unittest.TestCase):
    
    #Test that the Process object is created, creates a sample process
    def test_process_creation(self):
        p1 = Process("P1", 0, 4) #(Process ID, arrival time, burst time)

        #This will check that all values were stored correctly
        self.assertEqual(p1.get_process_id(), "P1")
        self.assertEqual(p1.get_arrival_time(), 0)
        self.assertEqual(p1.get_burst_time(), 4)

        #Check that waiting times and turnarounf times start at 0
        self.assertEqual(p1.get_waiting_time(), 0)
        self.assertEqual(p1.get_turnaround_time(), 0)

    #Method that tests waiting time setter
    def test_set_waiting_time(self):

        #Create sample
        p1 = Process("P1", 0, 4)
        #Update waiting time to 3 time units
        p1.set_waiting_time(3)
        #Check waiting time was updated properly
        self.assertEqual(p1.get_waiting_time(), 3)

    #Method that tests the turnaround time setter
    def test_set_turnaround_time(self):
        #Create sample process
        p1 = Process("P1", 0, 4)
        #Update turnaround time to 7 time units
        p1.set_turnaround_time(7)
        #Check that turnaround time was updated 
        self.assertEqual(p1.get_turnaround_time(), 7)
    
#Make test file runnable directly, unittest wille execute all methods
if __name__ == "__main__":
    unittest.main()
    