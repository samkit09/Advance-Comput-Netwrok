class Queue:
	def __init__(self):
		self.queue = list()

	def enqueue(self, element):
		self.queue.append(element)

	def dequeue(self):
		if not self.isEmpty():
			return self.queue.pop(0)
		return None
	
	def isEmpty(self) -> bool:
		return len(self.queue) == 0