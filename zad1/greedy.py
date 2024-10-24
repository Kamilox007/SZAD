import os

def greedy(n,tasks,setup_times):
    
    isTaskDone = [False]*n
    task_order = []
    total_processing_time = 0
    total_lateness = 0
    current_task = 0  # Start with the first task

    while not all(isTaskDone):
        # Mark the current task as done
        isTaskDone[current_task] = True
        # Add the current task to the task order
        task_order.append(current_task+1)
        # Update the total processing time and lateness
        task = tasks[current_task]
        processing_time, due_date = task
        total_processing_time += processing_time
        lateness = min(processing_time,max(0, total_processing_time - due_date))
        total_lateness += lateness

        if not all(isTaskDone):
            # Split tasks into those that can be completed on time and overdue tasks
            not_overdue_tasks = []
            overdue_tasks = []
            for i in range(n):
                if not isTaskDone[i]:
                    setup_time = setup_times[current_task][i]
                    # Check if the task's due date is >= total_processing_time + setup_time
                    if tasks[i][1] >= total_processing_time + setup_time:
                        not_overdue_tasks.append((i, tasks[i][1]))  # Store task index and due date
                    else:
                        overdue_tasks.append((i, tasks[i][1]))  # Store task index and due date

            if not_overdue_tasks:
                # Select the task with the smallest due date from non-overdue tasks
                next_task = min(not_overdue_tasks, key=lambda x: x[1])[0]
            else:
                # If all tasks are overdue, select the one with the smallest due date
                next_task = min(overdue_tasks, key=lambda x: x[1])[0]
            total_processing_time += setup_times[current_task][next_task]
            current_task = next_task

    return total_lateness,task_order



def main():

    input_folder = "input"
    output_folder = "output"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    input_files = os.listdir(input_folder)

    for root, dirs, files in os.walk(input_folder):
        for input_file in files:
            # Full path of the input file
            file_path = os.path.join(root, input_file)

            # Read input file
            with open(file_path, "r") as f:
                lines = f.readlines()

            n = int(lines[0].strip())  # number of tasks
            tasks = []

            # Read processing times and due dates
            for i in range(1, n + 1):
                p, d = map(int, lines[i].strip().split())
                tasks.append((p, d))

            # Read setup times matrix
            setup_times = []
            for i in range(n + 1, 2 * n + 1):
                setup_times.append(list(map(int, lines[i].strip().split())))

            # Run the greedy algorithm
            total_late_work, task_order = greedy(n, tasks, setup_times)

            # Extract the <nr_albumu_zad> part from the input file name (before the underscore '_')
            input_file_name = os.path.basename(input_file).split(".")[0]
            nr_albumu_zad = input_file_name.split("_")[0]

            # Create a subfolder in the output folder named after nr_albumu_zad
            subfolder_path = os.path.join(output_folder, nr_albumu_zad)
            os.makedirs(subfolder_path, exist_ok=True)

            # Create the output file name in the format 151776_<nr_albumu_zad>_<rozmiar>.out
            output_file = f"{subfolder_path}/151776_{input_file_name}.out"

            # Write the results to the output file
            with open(output_file, "w") as f_out:
                f_out.write(f"{total_late_work}\n")
                f_out.write(f"{' '.join(map(str, task_order))}\n")


if __name__ == "__main__":
    main()