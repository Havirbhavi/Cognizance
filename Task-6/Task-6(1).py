import re,csv
fh = open('onefileline.txt')
for i in fh:
        n = re.findall(r'[+-]?[0-9]+\.[0-9]+', i)
        a = re.findall(r'[a-zA-Z]+', i)
        j = 0
        for p in range(len(n)):
            with open('onefileline.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), a[j],n[p],a[j+1]])
            j += 2

with open('onefileline.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))
