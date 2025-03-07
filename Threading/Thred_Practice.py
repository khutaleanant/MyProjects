# import threading
# import time

# def print_cube(num):
#     print("Cube:{}".format(num*num*num))
    

# def print_square(num):
#     print("Square:{}".format(num*num))

# # Create threads
# t1 = threading.Thread(target=print_square,args=(5,))
# t2 = threading.Thread(target=print_cube,args=(5,))
    
# # Start the threads
# t1.start()
# time.sleep(2)
# t2.start()
# time.sleep(2)
# # Wait for both threads to finish
# t1.join()
# t2.join()

# print("Done!")
# ##===================================================================
    
import threading
import queue
import time
import random

# Task function that simulates processing with a given priority
def process_task(q):
    while True:
        # Wait until there is a task in the queue
        priority, task = q.get()
        if task == "exit":  # Check for the exit signal
            break
        print(f"Thread {threading.current_thread().name} processing task: {task} with priority {priority}")
        time.sleep(random.uniform(0.5, 2))  # Simulate processing time
        q.task_done()  # Indicate that the task is done

# Create a priority queue
task_queue = queue.PriorityQueue()

# List of tasks to add to the priority queue
tasks = [
    (2, "Task 2"),  # Priority 2
    (1, "Task 1"),  # Priority 1 (higher priority)
    (3, "Task 3"),  # Priority 3
    (1, "Task 4"),  # Priority 1
    (4, "Task 5"),  # Priority 4 (lowest priority)
]

# Add tasks to the priority queue
for task in tasks:
    task_queue.put(task)

# Number of worker threads
num_workers = 3

# Create worker threads
threads = []
for i in range(num_workers):
    thread = threading.Thread(target=process_task, args=(task_queue,))
    threads.append(thread)
    thread.start()

# Wait for all tasks in the queue to be processed
task_queue.join()  # Blocks until all tasks are processed

# Send exit signal to worker threads
for _ in range(num_workers):
    task_queue.put((0, "exit"))  # The "exit" task will signal the threads to stop

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All tasks are processed.")

