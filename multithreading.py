import threading
import queue
import time

def your_function(task_data):
    """The function you want to execute with each task."""
    print(f'Hiii {task_data}')
    time.sleep(2)  # Simulating some work

def worker():
    while True:
        task_data = task_queue.get()
        if task_data is None:
            break
        your_function(task_data)
        task_queue.task_done()

if __name__ == "__main__":
    MAX_THREADS = 10 
    NUM_TASKS = 10
    
    task_queue = queue.Queue()

    # Create and start worker threads
    threads = []
    for _ in range(MAX_THREADS):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)  

    # Add tasks to the queue
    for i in range(NUM_TASKS):
        task_queue.put(i) 

    # Wait for all tasks to complete
    task_queue.join()   # Moved here to ensure tasks are done

    # Add sentinel values to signal stopping to worker threads
    for _ in range(MAX_THREADS):
        task_queue.put(None)   

    # Wait for all threads to finish
    for thread in threads:
        thread.join()  

    print("All tasks completed!")
