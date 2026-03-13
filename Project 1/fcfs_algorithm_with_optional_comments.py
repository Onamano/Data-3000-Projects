
class FCFSAlgorithm:
    """
    Implements FCFS scheduling.

    This class takes in a queue instance (linked list of process objects),
    dequeues them into a list, then sorts the list by arival time,
    then performs the FCFS logic on the process objects based on their 
    attributes to calculate timing metrics and then returns the results 
    back to main.
    """
    def run(self, queue):
        results = []  #a list to hold processes once they are finished 
        current_time = 0 #acts like a clock that keeps track of the timeline, starts at 0, gets updated with the burst time (length of process execution) of the porevious process 

        #if the queue is not empty, 
        while not queue.is_empty():
            results.append(queue.dequeue()) #empty it into the results list by using the dequeue method to remove it from the queue and append it to the results list

        #now that the processes have been deququed from the queue, we can sort them by arival time of the process
        results.sort(key=lambda p: p.get_arrival_time()) #lambda acts as a temporary function to tell sort to sort by arival times

        #now that the results list of processes has been sorted, we loop thorugh each process in the results list
        for p in results: #for each process object in the list
            if current_time < p.get_arrival_time():  #if the current time (which will be updated to the previous processess finish time), is less than the arival time of the next process object (which would happen if there was a time gap between the next and previous process)
                current_time = p.get_arrival_time()  #set the current_time (the time the previous process finished) to be the arival time of the current process object
            #if we did not check this, if a process arived with a gap in between the previous, the next waiting time calculation would be incorrect and result in a negative value
            #because it would assume the current process arived directly after the previous one
            
            waiting_time = current_time - p.get_arrival_time() #calculates wait time by subtracting the arival time of a process from the current_time counter (which is the start time of the current process (the finish time of everything that came before it (cumulative burst times)))
            p.set_waiting_time(waiting_time) #now set the wait time of the process object by calling its class's set_waiting_time() method

            #turnaround time is the total duration from arival to completion 
            turnaround_time = waiting_time + p.burst_time #so if we add the burst time(length of time process took to execute), with how long the process waited we get the turnaround time
            p.set_turnaround_time(turnaround_time) #now set the turnaround time of this process object by calling its class's set_turnaround_time() method

            current_time += p.burst_time #add to the counter to keep track of when a process finishes and when the next one should start

        return results #after going thorugh all process objects in the sorted results list, return them back to main




