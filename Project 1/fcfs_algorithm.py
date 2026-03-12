from process import Process
from queue_implementation import QueueImplementation

class FCFSAlgorithm:
    
    def run(self, queue):
        results = []
        current_time = 0

        
        while not queue.is_empty():
            results.append(queue.dequeue())

        
        results.sort(key=lambda p: p.get_arrival_time())

        
        for p in results:
            if current_time < p.get_arrival_time():
                current_time = p.get_arrival_time()

            
            waiting_time = current_time - p.get_arrival_time()
            p.set_waiting_time(waiting_time)

            turnaround_time = waiting_time + p.burst_time
            p.set_turnaround_time(turnaround_time)

            current_time += p.burst_time

        return results
