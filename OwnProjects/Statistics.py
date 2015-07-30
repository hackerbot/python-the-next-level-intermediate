import statistics as s

def statanalysis():
    string = input('Insert data (separate each entry with space):\n').split(' ')
    data = list(map(int, string))
    x = s.mean(data)
    print(x)
    x = s.median(data)
    print(x)
    x = s.stdev(data)
    print(x)
    x = s.variance(data)
    print(x)
    try:
        x = s.mode(data)
        print(x)
    except Exception as e:
            print(str(e))
statanalysis()