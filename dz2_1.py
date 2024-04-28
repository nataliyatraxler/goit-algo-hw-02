import queue
import time
import threading
import random

def generate_request(q, lock, request_id):
    """ Generates a new request and adds it to the queue """
    with lock:
        print(f"Generating request {request_id}")
        q.put(request_id)
        time.sleep(random.randint(2, 4))  # Simulating time taken to generate a request

def process_request(q, lock):
    """ Processes a request by removing it from the queue """
    while True:
        with lock:
            if not q.empty():
                request_id = q.get()
                print(f"Processing request {request_id}")
                time.sleep(random.randint(1, 2))  # Simulating time taken to process a request
            else:
                break

def main_loop():
    q = queue.Queue()
    lock = threading.Lock()
    request_id = 0

    # Thread to generate requests
    def request_generator():
        nonlocal request_id
        while request_id < 20:  # Generate requests only up to a certain limit
            generate_request(q, lock, request_id)
            request_id += 1

    # Thread to process requests
    def request_processor():
        process_request(q, lock)  # Continue processing until no more requests

    generator_thread = threading.Thread(target=request_generator)
    processor_thread = threading.Thread(target=request_processor)

    generator_thread.start()
    processor_thread.start()

    # Wait for the generator thread to finish
    generator_thread.join()
    # Wait for the processor thread to finish processing all requests
    processor_thread.join()

    print("Main loop ending...")

if __name__ == "__main__":
    main_loop()
