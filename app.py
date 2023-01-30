import sys
import time
import random
import os

from lib.FlexUnlimited import FlexUnlimited

if __name__ == "__main__":
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("***Amazon Flex Unlimited v2*** \n")
    flexUnlimited = FlexUnlimited()
    if (len(sys.argv) > 1):
      arg1 = sys.argv[1]
      if (arg1 == "getAllServiceAreas" or arg1 == "--w"):
        print("\n Your service area options:")
        print(flexUnlimited.getAllServiceAreas())
      else:
        print("Invalid argument provided.")
    else:
      flexUnlimited.run()
      seconds = random.randint(30, 60)
      while seconds > 0:
          print(seconds)
          time.sleep(1)
          seconds -= 1