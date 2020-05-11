import heapq
heap=[]
heapq.heappush(heap,('V', 24))
heapq.heappush(heap,('V', 45))
heapq.heappush(heap,('V', 100))
print("numbers in the heap are--->>> ")
for x in heap:
    print(x)
print(">>>>>>>>>>")
print("     smallest number of heap")
print("     ",heap[0])
print(">>>>>>>>>>")
print("     Popping this number HEAP BECOMES")
heapq.heappop(heap)
for x in heap:
    print("      ",x)



#   #output
    #python prg1.py
    #numbers in the heap are--->>>
    #('V', 24)
    #('V', 45)
    #('V', 100)
    #>>>>>>>>>>
    #     smallest number of heap
    #  ('V', 24)
    #>>>>>>>>>>
    #Popping this number HEAP BECOMES
    #  ('V', 45)
    #  ('V', 100)