def recursiveCanReach(arr, current_index, solution_trace = []):
    if (current_index >= len(arr) or current_index < 0 or current_index in solution_trace):
        return False
    if arr[current_index] == 0:
        return True
    else:
        return (recursiveCanReach(arr, current_index + arr[current_index], solution_trace + [current_index])
        or recursiveCanReach(arr, current_index - arr[current_index], solution_trace + [current_index]))

def queueCanReach(arr, current_index):
    index_tracker = []
    queue = [0]
    while(len(queue) > 0):
        latest_index = queue.pop()
        if 0 <= latest_index < len(arr) and latest_index not in index_tracker:
            if arr[latest_index] == 0:
                return True
            index_tracker.append(latest_index)
            queue.append(latest_index + arr[latest_index])
            queue.append(latest_index - arr[latest_index])
    return False


a1 = [1,3,3,4,0]
a2 = [4,8,5,2,3,5,1,6,4,0]
a3 = [4,2,3,0,3,1,0]
a4 = [1]
a5 = [2,0]

print(recursiveCanReach(a1, 0))
print(recursiveCanReach(a2, 0))
print(recursiveCanReach(a3, 0))
print(recursiveCanReach(a4, 0))
print(recursiveCanReach(a5, 0))

print("-----------------")

print(queueCanReach(a1, 0))
print(queueCanReach(a2, 0))
print(queueCanReach(a3, 0))
print(queueCanReach(a4, 0))
print(queueCanReach(a5, 0))
