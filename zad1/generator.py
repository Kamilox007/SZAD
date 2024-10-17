import random

def generate_instance(n, filename="plik_wejsciowy.txt", due_date_factor=1.5):
    with open(filename, "w") as f:
        # Write the number of tasks
        f.write(f"{n}\n")
        
          # Track total processing time of all tasks so far
        
        # Generate and write processing times (p) and due dates (d)
        for _ in range(n):
            p = random.randint(1, 20)  # Processing time between 10 and 100
              # Update total processing time
            d = random.randint(p, n*10)
            f.write(f"{p} {d}\n")
        
        # Generate and write the setup times matrix (S)
        for i in range(n):
            setup_times = [random.randint(0, 15) if i != j else 0 for j in range(n)]
            f.write(" ".join(map(str, setup_times)) + "\n")


for i in range(1, 11):
    generate_instance(i * 50, f"input/151776_{i*50}.in")  # Generates instances with 50, 100, ..., 500 tasks
