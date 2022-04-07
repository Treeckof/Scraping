import sys

def greet(name):
   print('Hello, {0}!'.format(name))

if len(sys.argv) > 1:
   name = sys.argv[1]

   for i in range(len(sys.argv)):
      print(sys.argv[i])
   #greet(name)

else:
   greet('world')