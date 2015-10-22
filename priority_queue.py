import argparse
import math

class Pq:
  def __init__(self,size):
  	self.elts = []
  	for i in range(size):
  	  self.elts.append(float('inf'))

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
      # First, update the first two elements
      even = min(self.elts[0],to_push)
      odd = max(self.elts[0],to_push)
      if len(self.elts) == 2:
        self.elts.append(self.elts[1])
      self.elts[0] = even
      self.elts[1] = odd
      # Inductively update the rest of the queue
      self.elts.append(float('inf'))
      for i in range(1, int(math.ceil(len(self.elts)/2))-1):
        even = min(self.elts[2*i],self.elts[(2*i)-1])
        odd = max(self.elts[2*i],self.elts[(2*i)-1])
        self.elts[2*i] = even
        self.elts[(2*i)+1] = odd
    # Everything okay!
    print("\nDone")

if __name__ == "__main__":
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--size", type=int, help="initial size of the queue", default=10, required=False)

  args = argparser.parse_args()

  # Initialize the queue
  pq = Pq(args.size)

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