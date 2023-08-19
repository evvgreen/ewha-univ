N = 8
BIN_SIZE = 10
item = [7, 5, 6, 4, 2, 3, 7, 5]
bins = [[] for i in range(N)]
remnant = [BIN_SIZE for _ in range(N)]
bin_count = 1

for i in range(N):
    j = 0
    packed = False
    while j < bin_count:
        if item[i] <= remnant[j]:
            bins[j].append([i, item[i]])
            remnant[j] -= item[i]
            packed = True
            break
        j+=1
    if not packed:
        bins[j].append([i, item[i]])
        remnant[j] -= item[i]
        bin_count += 1

print('First Fit # of bins: ', bin_count)

for i in range(bin_count):
    print('Bin:', i)
    for j in range(len(bins[i])):
        print("Item=", bins[i][j][0], "Size=", bins[i][j][1])