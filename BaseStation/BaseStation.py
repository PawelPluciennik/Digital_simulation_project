import Const.Const as cst

class BaseStation():
  
  def __init__(self):
    self._queue = []
    self.actualUsers = 0

  def enqueue(self, element):
    if(self.actualUsers + 1 <= cst.N):
      self._queue.insert(0, element)
    return self

  def dequeue(self):
      return self._queue.pop()

  def __len__(self):
      return len(self._queue)