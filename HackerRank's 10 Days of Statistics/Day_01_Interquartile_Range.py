def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    n = len(values)
    s = []
    for i in range(n):
        s += [values[i]] * freq[i]
    n = sum(freq)
    s.sort()
    q1 = median(s[:n//2])
    q3 = median(s[(n+1)//2:])
    iq = float(q3-q1)
    print(round(iq,1))