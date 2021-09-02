def weightedMean(X, W):
    # Write your code here
    w_sum = sum(W)
    w_mean = 0.0
    for num, weight in zip(X,W):
        w_mean += (num * weight) / w_sum
    w_mean = round(w_mean, 1)
    print(w_mean)
