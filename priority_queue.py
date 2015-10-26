import argparse
import math

class Pq:
  def __init__(self):
  	self.elts = []

  def display(self):
  	print("\nCurrent queue:")
  	print(self.elts)

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
      self.elts.append(to_push)
      temp = []
      for i in range(len(self.elts)):
        temp.append(self.elts[i])
      # Inductively correct the queue
      for i in range(len(self.elts)):
        if i % 2 == 0:
          temp[i] = min(self.elts[i],self.elts[i-1])
          if i+1 < len(self.elts):
            temp[i+1] = max(self.elts[i-1],self.elts[i])
      self.elts = temp
    # Everything okay!
    print("\nDone")

if __name__ == "__main__":
  # Initialize the queue
  pq = Pq()

  # Give the user a friendly menu
  usr_choice = 0
  while usr_choice != 3:
    # Display the queue
    pq.display()
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
      print("2")