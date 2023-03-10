import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 5

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count += 1
            print(name, "took a piece! Sushi remaining:", sushi_count)
        
        second_chopstick.release()
        first_chopstick.release()

if __name__ == "__main__":
    threading.Thread(target=philosopher, args=("Barron", chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=("Olivia", chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args("Steve", chopstick_c, chopstick_a)).start()

# Due to scheduling, there might only one philosopher to make it to eat all sushi.
# This is why deadlocks is tricky!
# To increase the probability of deadlock happening, try to increase the sushi to 500.