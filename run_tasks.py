import os
import subprocess
import time
from log_utils import *

def run_task(task_number):
    task_dir = "tasks/"
    code_file = os.path.join(task_dir, f"task{task_number}.py")

    if not os.path.exists(code_file):
        print(f"Task {task_number} is complete or does not exist.")
        return True

    try:
        subprocess.check_call(["python", code_file])
        print(f"Task {task_number} is complete. Move on to the next task.")
        return True
    except subprocess.CalledProcessError:
        print(f"Task {task_number} has an error. Please fix it and try again.")
        return False


def reset_tasks():
    reset_script = "reset_tasks.py"
    try:
        subprocess.check_call(["python", reset_script])
        print("Tasks have been reset.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reset tasks: {e}")


def main():
    global INITIAL_RUN

    if not os.path.exists("logs"):
        os.makedirs("logs")

    start_time = get_start_time()

    if os.path.exists(RESET_FLAG_FILE):
        log("Starting Timer")
        start_time = time.time()
        set_start_time(start_time)
        os.remove(RESET_FLAG_FILE)  # Remove the reset flag file after reading it
        INITIAL_RUN = False
    elif start_time is not None:
        start_time = float(start_time)
    task_number = 1
    total_tasks = len(
        [
            name
            for name in os.listdir("tasks")
            if name.startswith("task") and name.endswith(".py")
        ]
    )
    all_tasks_completed = True

    while task_number <= total_tasks:
        if not run_task(task_number):
            all_tasks_completed = False
            break
        task_number += 1

    if all_tasks_completed:
        end_time = time.time()
        elapsed_time = end_time - start_time
        log(
            f"All tasks completed successfully. Total time: {elapsed_time:.2f} seconds."
        )
        print(
            f"Congratulations! All tasks completed successfully in {elapsed_time:.2f} seconds."
        )

        clear_start_time()  # Clear the start time after successful completion

        best_run = get_best_run()
        if best_run is None or elapsed_time < best_run:
            print("That was your fastest run yet!")
            set_best_run(elapsed_time)
            print("Your time has been logged as the fastest run.")
            post_to_slack = input("Do you want to post your time to Slack? (y/n): ")
            if post_to_slack.lower() == "y":
                name = input("Enter your name: ")
                send_slack_message(
                    f"{name} got a new personal best of {elapsed_time:.2f} seconds on v0!"
                )
        else:
            time_difference = elapsed_time - best_run
            print(
                f"This run was {time_difference:.2f} seconds slower than your best run."
            )

        # Reset tasks after successful completion and logging
        reset_tasks()
    else:
        print("Not all tasks were completed successfully. Please try again.")


if __name__ == "__main__":
    main()
