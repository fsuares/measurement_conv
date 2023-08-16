

from menu import options
from convertions import *

def main():
  options()
  initial_unit = str(input("Unidade inicial: "))
  value = float(input("Valor: "))
  final_unit = str(input("Unidade final: "))
  convert(initial_unit, final_unit, value)



if __name__ == '__main__':
  main()

