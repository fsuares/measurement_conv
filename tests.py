

# Some modules require
from convertions import *
from time import sleep

# CONSTS for prints
p = "PASSED!"
f = "FAILED!"


# INPUTS
initial_values = [1.42, 123, 421, 3.12, 6.34, 43.7]

## -----------------------------------FEAT-------------------------------------------
# --- Feat to yards ----
ft_final_values1 = [0.473333, 41, 140.33333, 1.04, 2.11333, 14.5666]
# --- Feat to meters ---
ft_final_values2 = [0.432794, 37.48857, 128.31453, 0.95092, 1.93233, 13.31911]

## -----------------------------------YARD-------------------------------------------
# --- Yard to meters ---
yard_final_values1 = [1.297989, 112.43144, 384.82632, 2.85191, 5.79524, 39.945155]
# --- Yard to feats ----
yard_final_values2 = [4.26, 369, 1263, 9.36, 19.02, 131.1]

## -----------------------------------METER------------------------------------------
# --- Meter to feat ---
meter_final_values1 = [4.65902, 403.563, 1381.301, 10.23672, 20.80154, 143.3797]
# --- Meter to yard ---
meter_final_values2 = [1.55348, 134.562, 460.574, 3.41328, 6.93596, 47.8078]


##
# Feat test function
def feat_test():
  print("\nTESTING FEATS TO YARDS")
  sleep(1)
  for i in range(len(initial_values)):
    if ft_yard(initial_values[i]) == round(ft_final_values1[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

  print("TESTING FEATS TO METERS")
  for i in range(len(initial_values)):
    if ft_meter(initial_values[i]) == round(ft_final_values2[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

##
# Yard test function
def yard_test():
  print("\nTESTING YARD TO METER")
  sleep(1)
  for i in range(len(initial_values)):
    if yard_meter(initial_values[i]) == round(yard_final_values1[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

  print("TESTING YARD TO FEAT")
  for i in range(len(initial_values)):
    if yard_ft(initial_values[i]) == round(yard_final_values2[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

##
# Meters test function
def meter_test():
  print("\nTESTING METER TO FEAT")
  sleep(1)
  for i in range(len(initial_values)):
    if meter_ft(initial_values[i]) == round(meter_final_values1[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

  print("TESTING METER TO YARD")
  for i in range(len(initial_values)):
    if meter_yard(initial_values[i]) == round(meter_final_values2[i], 3):
      print("{} of {}: \033[32m{}\033[m".format(i+1, len(initial_values), p))
      sleep(0.5)
    else:
      print("{} of {}: \033[31m{}\033[m".format(i+1, len(initial_values), f))
      sleep(0.5)
  print()

def maint_test():
  choice = int(input("""TEST OPTIONS
1 - Yards tests
2 - Meters tests
3 - Feats tests
"""))

  match(choice):
    case(1): yard_test()
    case(2): meter_test()
    case(3): feat_test()

maint_test()

