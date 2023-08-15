from main import main

##--------------------------------------------------------------------------------------------------------
# ------------------------------------- Convertions functions --------------------------------------------
def ft_yard(value):
  return round(value / 3, 3)

def ft_meter(value):
  return round(value / 3.281, 3)

def yard_ft(value):
  return round(value * 3, 3)

def yard_meter(value):
  return round(value / 1.094, 3)

def  meter_yard(value):
  return round(value * 1.094, 3)

def meter_ft(value):
  return round(value * 3.281, 3)


## -------------------------------------------------------------------------------------------------------
# ------------------------------------- Final convertion function -----------------------------------------
def convert(init_unit, final_unit, valor):
  if init_unit == "Jardas" or init_unit == "jardas" or init_unit == "jarda" or init_unit == "Jarda":
    if final_unit == "Metros" or final_unit == "metros" or final_unit == "metro" or final_unit == "Metro":
      print("Resultado: " + yard_meter(valor) + "m")
    elif final_unit == "Pés" or final_unit == "pés" or final_unit == "pes" or final_unit == "Pes":
      print("Resultado: " + yard_ft(valor) + "'")
    else:
      print("Error...")
      main()

  elif init_unit == "Metros" or init_unit == "metros" or init_unit == "Metro" or init_unit == "metro":
    if final_unit == "Jardas" or final_unit == "Jardas":
      print("Resultado: " + meter_yard(valor) + "jardas")
    elif final_unit == "Pés" or final_unit == "pés" or final_unit == "pes" or final_unit == "Pes":
      print("Resultado: " + meter_ft(valor) + "'")
    else:
      print("Error...")
      main()

  elif init_unit == "Pés" or init_unit == "pés" or init_unit == "pes" or init_unit == "Pes":
    if final_unit == "Jardas" or final_unit == "Jardas":
      print("Resultado: " + ft_yard(valor) + "jardas")
    elif final_unit == "Metros" or final_unit == "metros" or final_unit == "metro" or final_unit == "Metro":
      print("Resultado: " + ft_meter(valor) + "m")
    else:
      print("Error...")
      main()
  else:
    print("Error...")
    main()


