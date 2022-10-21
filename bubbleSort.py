arr = [4,1,2,22,34,2,100]

for i in range(len(arr)):

    for j in range(0,len(arr)-i-1):

        if arr[j]>arr[j+1]:

            arr[j], arr[j+1] = arr[j], arr[j+1]



    print(arr)