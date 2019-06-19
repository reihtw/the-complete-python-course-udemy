def countdown(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = task[0]
    task.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task fineshed')
