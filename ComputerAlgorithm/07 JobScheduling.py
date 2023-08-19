N=10
M=4

job = [5, 2, 4, 3, 4, 7, 9, 2, 4, 1]

start_time = [0 for _ in range(M)]
machine = [[] for _ in range(M)]

for i in range(N):
    j = start_time.index(min(start_time))
    machine[j].append([i, job[i]])
    start_time[j] += job[i]

print('Finish Time for all: ', max(start_time))

for i in range(M):
    print("Machine:", i)
    for j in range(len(machine[i])):
        print('job', machine[i][j][0], "time:", machine[i][j][1])

