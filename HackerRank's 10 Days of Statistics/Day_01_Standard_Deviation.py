def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    N= int(len(arr))
    # Find the mean
    mean = 0.0
    for num in arr:
        mean += num/N
    # Square distance
    sd=0.0
    for num in arr:
        sd += (num - mean)**2 / N
    sd = round(math.sqrt(sd),1)
    print(sd)