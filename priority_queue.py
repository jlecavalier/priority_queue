import argparse

class Pq:
  def __init__(self,size):
  	self.elts = []
  	for i in range(size):
  	  self.elts.append(float('inf'))

  def display(self):
  	print("Current queue:")
  	print(self.elts)

if __name__ == "__main__":
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--size", type=int, help="initial size of the queue", default=10, required=False)

  args = argparser.parse_args()

  # Initialize the queue and display its elements
  pq = Pq(args.size)
  pq.display()

  usr_choice = 0
  while usr_choice != 3:
  	print("\n1: push something onto the queue")
  	print("\n2: pop something from the queue")
  	print("\n3: exit")
  	print("\nWhat is your choice")