import os

def validate_output(input_filename, output_filename):
    # Read input file
    with open(input_filename, "r") as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())  # number of tasks
    tasks = []
    
    # Read processing times and due dates
    for i in range(1, n+1):
        p, d = map(int, lines[i].strip().split())
        tasks.append((p, d))  # tasks[i] = (processing_time, due_date)
    
    # Read setup times matrix
    setup_times = []
    for i in range(n+1, 2*n+1):
        setup_times.append(list(map(int, lines[i].strip().split())))
    
    # Read output file
    with open(output_filename, "r") as f:
        lines = f.readlines()
    
    # Read sum of delays from output
    reported_sum_of_delays = int(lines[0].strip())
    
    # Read the order of jobs
    order = list(map(int, lines[1].strip().split()))
    
    # Validate the sum of delays
    total_delay = 0
    current_time = 0
    
    for i in range(n):
        
        job_index = order[i]-1  # the job is indexed 1-based in the output
        #print(f"jobindex: {job_index}")
        p, d = tasks[job_index]  # processing time and due date for this job
        #print(f"p: {p}")
        #print(f"d: {d}")
        # Add setup time if it's not the first job
        if i > 0:
            prev_job_index = order[i-1] -1
            current_time += setup_times[prev_job_index][job_index]
        
        # Add processing time for the current job
        current_time += p
        
        # Calculate the delay for this job
        delay = max(0, current_time - d)
        total_delay += min(p, delay)  # Min is used to limit delay by processing time
    
    # Check if the calculated sum matches the reported sum
    if total_delay == reported_sum_of_delays:
        return "Valid: The sum of delays is correct."
    else:
        return f"Invalid: The calculated sum of delays is {total_delay}, but the reported sum is {reported_sum_of_delays}."

# Example usage
def main():
    input_folder = "input"
    output_folder = "output"

    input_files = os.listdir(input_folder)
    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, input_file.replace(".in", ".out"))
        print(validate_output(input_path, output_path))
main()