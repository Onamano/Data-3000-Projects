class FCFSAlgorithm:
    # Creates an array to hold the processes loaded into the queue, as well as initializing the current time variable which will hold arrival times of processes
    def run(self, queue):
        results = []
        current_time = 0

        # Ensures the results are being appended to the 
        while not queue.is_empty():
            results.append(queue.dequeue())

        # Sorts the processes based on their arrival time, ensuring the first ones to show up are the first ones completed
        results.sort(key=lambda p: p.get_arrival_time())

        # Iterates through the array holding the processes
        for p in results:
            # Sets the cureent time to the arrival time for each process in the results array if the processes have a gap in their arrival times
            if current_time < p.get_arrival_time():
                current_time = p.get_arrival_time()

            # Calculates the waiting time for each process in the array
            waiting_time = current_time - p.get_arrival_time()
            p.set_waiting_time(waiting_time)

            # Calculates the turnaround time for each process in the array
            turnaround_time = waiting_time + p.burst_time
            p.set_turnaround_time(turnaround_time)

            # Sets the current time to increment from the burst times of each process
            current_time += p.burst_time

        # Returns the array to main after sorting and calculations are complete
        return results
