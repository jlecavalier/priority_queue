# Instructions for running:
To run the program, navigate to the location of the enclosed .py file and type:

python priority_queue.py

The program will start up and give you some options.

# Notable Features:
1. The queue is printed to the screen every time you push or pop something.
2. Whenever you pop something, you will be told what was popped.
3. Every time you push or pop, the queue calls a special function called assert_correctness, which checks if the following two predicates are satisfied for all i >= 0:
P(i): X2i <= X2i+1
Q(i): X2i <= X2i+2
