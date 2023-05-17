jim = 'jimmy'
group1 = {'john': 1, 'doe': 2, 'tom': 6}
group2 = [{'kevin': 4, 'tom': 9}, {jim: 16}]
group3 = {'sara': 25, 'lisa': 36, 'anna':49}

for info in group2:
    for key in info.keys():
        group1[key] = info[key]

# What will group1 and group2 become after executing this program? Please write them down in the following lines (without actually running this program).
# group1: 
# group2: 