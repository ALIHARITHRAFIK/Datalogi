    
def skräp():
    bubble = timeit.timeit(stmt = lambda: bubble_sort(lista), number = 1)
    print("bubble tog", round(bubble, 4) , "sekunder")
    merge = timeit.timeit(stmt = lambda: merge_sort(lista), number = 1)
    print("merge tog", round(merge, 4) , "sekunder")
    return None
