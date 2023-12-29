import sys

def listArgs():
  no_arg = len(sys.argv) -1
  ls_arg = sys.argv[1:]
  
  if no_arg == 1:
    print("{} argument:".format(no_arg))
  elif no_arg > 1:
    print("{} arguments:".format(no_arg))
  else:
    print("0 arguments.")
    
  for num, arg in enumerate(ls_arg, start=1):
    print("{}: {}".format(num, arg))
    
if __name__ == "__main__":
  listArgs()