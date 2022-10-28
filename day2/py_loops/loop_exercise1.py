import time

start = time.time()

while time.time() - start <= 15:
    time.sleep(1)
    elapsed_time = time.time() - start
    print(f"time since the start {elapsed_time:.1f}")

elapsed_time = time.time() - start
print(f"Total time elapsed {elapsed_time:.1f}")
