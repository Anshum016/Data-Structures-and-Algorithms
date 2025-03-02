def Job(id,deadline,profit):
    jobs = sorted(zip(id,deadline,profit), key=lambda x: x[2] , reverse=True )

    max_deadline =  max(deadline)
    schedule = [-1] * (max_deadline + 1)

    total_profit=0
    job_count=0

    for job in jobs:
        job_id,job_deadline,job_profit=job

        for j in range(min(max_deadline,job_deadline),0,-1):
         if schedule[j] == -1:
            schedule[j] = job_id
            total_profit += job_profit
            job_count += 1
            break

    return job_count, total_profit


id = [1, 2, 3, 4]
deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]

print(Job(id,deadline,profit))
