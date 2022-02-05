import self as self


class Jobs:
    def __init__(self, cpu, start_time, end_time):
        self.cpu = cpu
        self.start_time = start_time
        self.end_time = end_time


def job_sort(job_list):
    # list = []
    # for i in passed:
    #     list.append(i)
    # print(sorted(list))
    job_list.sort(key=lambda x: x.start_time)
    return [jobs.start_time for jobs in job_list]


def job_queue(passed):
    sorted_list = job_sort(passed)




if __name__ == "__main__":
    job1 = Jobs(5, 2, 3)
    job2 = Jobs(15, 3, 1)
    job3 = Jobs(6, 10, 12)
    job4 = Jobs(30, 6, 15)
    job5 = Jobs(3, 8, 14)
    job6 = Jobs(6, 10, 18)
    job_list = [eval("job" + str(i)) for i in range(1, 7)]
    job_queue(job_list)
    # print(Jobs.job_sort(passed))
