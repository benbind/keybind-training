import os
import shutil

def reset_task(task_number):
    task_dir = f"tasks/"
    backup_dir = f"backup/"
    
    if not os.path.exists(backup_dir):
        print(f"Backup for Task {task_number} does not exist.")
        return
    
    code_file = os.path.join(backup_dir, f"task{task_number}.py")
    if not os.path.exists(code_file):
        print(f"Original code file for Task {task_number} is missing in backup.")
        return
    
    shutil.copy(code_file, task_dir)
    print(f"Task {task_number} has been reset.")

def main():
    task_number = 1
    total_tasks = len([name for name in os.listdir("tasks")])
    
    for task_number in range(1, total_tasks + 1):
        reset_task(task_number)

    # Create a flag file to indicate that the tasks have been reset
    with open("logs/reset_flag.txt", "w") as f:
        f.write("reset")

    print("All tasks have been reset.")

if __name__ == "__main__":
    main()
