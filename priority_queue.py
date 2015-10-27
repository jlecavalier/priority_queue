import argparse
import math

class Pq:
  def __init__(self):
  	self.elts = []

  def display(self):
  	print("\nCurrent queue:")
  	print(self.elts)

  def assert_correctness(self):
    if len(self.elts) > 1:
      for i in range(len(self.elts)-1):
        if i % 2 == 0:
          # Check the predicate P
          assert self.elts[i] <= self.elts[i+1]
          if i+2 < len(self.elts):
            # Check the predicate Q
            assert self.elts[i] <= self.elts[i+2]
    print("Queue is correct!\n")

  def push(self,to_push):
    if len(self.elts) < 1:
      # Queue is empty, so just add the first element
      self.elts = [to_push]
    elif len(self.elts) == 1:
      # Just one element in queue. 
      # First element becomes the min of
      # the first element and the item to push.
      # Second element becomes other one.
      even = min(self.elts[0],to_push)
      odd = max(self.elts[0],to_push)
      self.elts[0] = even
      self.elts.append(odd)
    else:
      # Place the new element in the second place
      temp = [0]
      for i in range(len(self.elts)):
        temp.append(self.elts[i])
      # Inductively correct the queue
      for i in range(len(self.elts)):
        if i == 0:
          temp[i] = min(to_push,self.elts[i])
          temp[i+1] = max(to_push,self.elts[i])
        elif i % 2 == 0:
          if i == len(self.elts) - 1:
            temp[i] = self.elts[i-1]
          else:
            temp[i] = min(self.elts[i],self.elts[i-1])
            if i + 1 < len(self.elts):
              temp[i+1] = max(self.elts[i],self.elts[i-1])
      self.elts = temp

  def pop(self):
    # Queue is empty, so can't pop
    if len(self.elts) < 1:
      print("\nNothing to pop!")
      return None
    # Queue only has one element, so pop it
    elif len(self.elts) == 1:
      popped = self.elts[0]
      self.elts = []
      return popped
    # Queue only has two elements, pop the first one.
    elif len(self.elts) == 2:
      popped = self.elts[0]
      self.elts = [self.elts[1]]
      return popped
    else:
      # Inductively handle the queue
      popped = self.elts[0]
      temp = []
      for i in range(len(self.elts)):
        temp.append(self.elts[i])
      for i in range(len(self.elts)-1):
        if i % 2 == 0:
          if i+2 >= len(self.elts):
            temp[i] = self.elts[i+1]
          else:
            temp[i] = min(self.elts[i+1],self.elts[i+2])
            temp[i+1] = max(self.elts[i+1],self.elts[i+2])
      # Last element is leftover. Get rid of it.
      del temp[-1]
      self.elts = temp
      return popped

if __name__ == "__main__":
  # Initialize the queue
  pq = Pq()

  # Give the user a friendly menu
  usr_choice = 0
  while usr_choice != 3:
    # Display the queue
    pq.display()
    # Check that the queue is correct
    pq.assert_correctness()
    # Give the user a friendly menu
    print("\n1: push something onto the queue")
    print("2: pop something from the queue")
    print("3: exit")
    usr_choice = input("\nEnter your choice: ")

    # Push something
    if usr_choice == 1:
      pq.push(input("\nEnter the number you want to push: "))

    # Pop something
    elif usr_choice == 2:
      popped = pq.pop()
      if popped != None:
        print("\nPopped %d off the queue" % popped)