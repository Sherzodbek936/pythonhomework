def enrollment_stats(x):
    c=0
    d=0
    for i in range(len(x)):
        c+=x[i][1]
        d+=x[i][2]
    print(f"Total students: {c}")
    print(f"Total tuition: ${d}")
            
def mean(x):
    a=0
    b=0
    for i in range(len(x)):
        a+=x[i][1]
        b+=x[i][2]
    print(f"Student mean: {a/len(x):.2f}")
    print(f"Tuition mean: ${b/len(x):.2f}")

def median(x):
    a=[]
    for i in range(len(x)):
        a.append(x[i][1])
    a.sort()
    print(f"Student median: {a[int(len(x)/2)]}")
    b=[]
    for i in range(len(x)):
        b.append(x[i][2])
    b.sort()
    print(f"Tuition median: ${b[int(len(x)/2)]}")

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollment_stats(universities)
mean(universities)
median(universities)