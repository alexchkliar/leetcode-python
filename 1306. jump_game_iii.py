def recursiveCanReach(arr, start_index, solution_trace = []):
    if (start_index >= len(arr) or start_index < 0):
        return False
    new_index_up = start_index + arr[start_index]
    new_index_down = start_index - arr[start_index]
    print("Array: ", arr, "New index up: ", new_index_up, "New index down: ", new_index_down, "Trace: ", solution_trace)
    if solution_trace is None:
        if ((new_index_up < 0 or new_index_up >= len(arr)) and
        (new_index_down < 0 or new_index_down >= len(arr))):
            return False
    if ((new_index_up < 0 or new_index_up >= len(arr) or new_index_up in solution_trace) and
    (new_index_down < 0 or new_index_down >= len(arr) or new_index_down in solution_trace)):
        return False
    if new_index_up == len(arr) - 1 or new_index_down == len(arr) - 1:
        return [True, start_index, new_index_down, new_index_up]
    else:
        return (recursiveCanReach(arr, new_index_up, solution_trace + [new_index_up])
        or recursiveCanReach(arr, new_index_down, solution_trace + [new_index_down]))

# print(recursiveCanReach([1,2,3,4,5], 0, []))
print(recursiveCanReach([4,8,5,2,3,5,1,6,4,0], 0, [0]))
