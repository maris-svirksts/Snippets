#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    # [[1, 5], [10, 3], [3, 4]] amount of petrol, distance / 1 
    result = 0
    tank   = 0

    for i in range(len(petrolpumps)):
        tank += petrolpumps[i][0]

        if tank < petrolpumps[i][1]:
            tank   = 0
            result = i + 1 if i < len(petrolpumps) else i
        else:
            tank -= petrolpumps[i][1]

    return result
