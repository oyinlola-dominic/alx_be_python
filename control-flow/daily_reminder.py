def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process task based on priority using match-case
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Note: '{task}' has an unknown priority level"

    # Modify message if time-bound
    if time_bound == "yes":
        if priority in ["high", "medium"]:
            message += " that requires immediate attention today!"
        elif priority == "low":
            message += ". Consider completing it soon if possible."
    else:
        if priority in ["high", "medium"]:
            message += ". Consider scheduling it for today."
        elif priority == "low":
            message += ". Consider completing it when you have free time."

    print(message)

if __name__ == "__main__":
    main()
