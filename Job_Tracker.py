# job_tracker.py

def add_job(jobs, company, role, status="Applied"):
    jobs.append({
        "company": company,
        "role": role,
        "status": status
    })

def list_jobs(jobs):
    if not jobs:
        print("No job applications yet.")
        return
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['company']} - {job['role']} [{job['status']}]")

def update_status(jobs, index, new_status):
    if 0 <= index < len(jobs):
        jobs[index]['status'] = new_status
        print("Status updated.")
    else:
        print("Invalid job number.")

def main():
    jobs = []
    while True:
        print("\nJob Tracker")
        print("1. Add a job")
        print("2. List all jobs")
        print("3. Update job status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            company = input("Enter company name: ")
            role = input("Enter role/title: ")
            add_job(jobs, company, role)

        elif choice == '2':
            list_jobs(jobs)

        elif choice == '3':
            list_jobs(jobs)
            try:
                index = int(input("Enter job number to update: ")) - 1
                new_status = input("Enter new status (e.g., Interview, Offer, Rejected): ")
                update_status(jobs, index, new_status)
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
```

Let me know if you want a **README**, tags, or a version with file saving.
