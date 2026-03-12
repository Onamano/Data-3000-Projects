import tkinter as tk
from tkinter import simpledialog, messagebox
from process import Process
from queue_implementation import QueueImplementation
from fcfs_algorithm import FCFSAlgorithm

def run_simulation():
    """
    Orchestrates the FCFS simulation by gathering user input about number of processes,
    process arival and burst time, populates the queue linked list with the processes, 
    and displays the calculated results.
    """
    #initializes an instance of QueueImplementation class and stores in variable
    queue = QueueImplementation() 

    #here we are getting the total number of processes from the user 
    n = simpledialog.askinteger("FCFS Simulation", "Enter the number of processes: ")
    if not n: #if the user clicks cancel or enters nothing 
        return #we exit the function early 

    #loop for collecting data and adding it top the QueueImplementation instance
    for i in range(1, n+1): #for each process in range starting at number 1 to the number of processes + 1 (n+1 because otherwise this would stop at n but not include n, so we use n+1 for it to stop at n+1 but not include it)
        process_id = f"P{i}" #store its process number in this variable
        arrival = simpledialog.askinteger("FCFS Simulation", f"Enter arrival time for process {process_id}: ") #prompt user for arival time of each process
        burst = simpledialog.askinteger("FCFS Simulation", f"Enter burst time for process {process_id}: ") #prompt user for burst time of each process (how long CPU takes to execute process)
        process = Process(process_id, arrival, burst) #create an instance of the process class passing the process id, its arival, and burst times and store in this variable
        queue.enqueue(process) #now add each process instance to the queue linked list instance by calling enqueue() from QueueImplementation and passing it each process instance

    fcfs = FCFSAlgorithm()    #now we initialize the FCFS algorithm class, we create this instance to access its run method
    results = fcfs.run(queue) #then we pass the entire queue (containing all our process instances) to the FCFS class's run method

    #this prepares a header string for display separated by tabs so everything is neatly spaced
    output = "Process\tArrival\tBurst\tWaiting\tTurnaround\n"
    total_waiting = 0 #initializes total waiting and turnaround variables starting them at 0
    total_turnaround = 0
    for p in results: #start looping though each process instance that gets returned from the FCFS algorithms run method
        output += f"{p.process_id}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\n" #now add the data from each Process instance into the table string separated by tabs so it lines up nicely with the headers
        total_waiting += p.waiting_time #add up all of the waiting times for each process instance and store it here
        total_turnaround += p.turnaround_time #add up all of the turnaround times for each process instance and store it here

    #now we can calculate the averages by deviding the totals by the number of process instances (n)
    avg_waiting = total_waiting / n 
    avg_turnaround = total_turnaround / n

    output += f"\nAverage Waiting Time: {avg_waiting:.2f}\n"     #format the output for the avaverage wait and turnaround times calculated above
    output += f"Average Turnaround Time: {avg_turnaround:.2f}"

    #now we can use a tkinter message box to show the final calculated results 
    messagebox.showinfo("FCFS Simulation Results", output)

def main():
    """
    The entry point for the application. Starts the tkinder GUI root window and triggers the 
    simmulation to start. Destorys and closes the tkinter root window when simulation finishes.
    """
    root = tk.Tk() #initializes the tkinter root window which is required for any GUI 
    root.withdraw() #tthis then hides the empty main tkinter window so the user only will see the dialog boxes we want them to see
    messagebox.showinfo("FCFS Simulation", "Press OK to initiate the simulation!") #shows the welcoming popup to let the user kow the program is starting
    run_simulation() #calls the run_simulation() function where all of the main logic happens
    root.destroy() #closes the backgroud root window after run_simulation() and all message boxes are finished

#runs the main program, ensures that main() function only runs if this file is executed dirtectly (not if its imported elsewhere)
if __name__ == "__main__":
    main()