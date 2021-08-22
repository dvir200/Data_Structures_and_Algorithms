
""" Queue - First in, First out """

queue = []

queue.append("data1")
queue.append("data2")
queue.append("data3")
queue.append(5)

print(queue)

""" deleting data1 """
queue.pop(0) 
print(queue)

""" deleting data2 """
queue.pop(0)
print(queue)