# PYTHON AREA UNIT CONVERSION CODE 
area=float(input("Enter your area:"))
unit=input("What is your Unit? Inches, Feet, Meter, Kilometer, Miles. I, FT, M, KM, MI:")
target_unit=input("Enter the unit to which you will like to covert:")

if unit == "KM":
     if target_unit == "M":
         area *= 1000
         unit, target_unit = "Kilometers", "meters"
     elif target_unit == "FT":
          area *= 3280.84
          unit, target_unit = "Kilometers", "Feet"
     elif target_unit == "MI":
          area /= 1.60934
          unit, target_unit= "Kilometers" , "Miles"
     elif target_unit == "I":
          area *= 39370.1
          unit, target_unit = "Kilometers" , "Inches"
     else:
          print(f"Conversion to {target_unit} is not supported")
elif unit == "M":
     if target_unit == "KM":
          area /= 1000
          unit, target_unit = "Meters" , "Kilometers"
     elif target_unit == "FT":
          area *= 3.28084
          unit, target_unit = "Meters" , "Feet"
     elif target_unit == "MI":
          area *= 0.000621371
          unit, target_unit = "Meters" , "Miles"
     elif target_unit == "I":
          area *= 39.3701
          unit, target_unit = "Meters" , "Inches"
     else: 
          print(f"Conversion to {target_unit} is not supported")
elif unit == "MI":
     if target_unit == "KM":
          area *= 1.60934
          unit, target_unit = "Miles" , "Kilometers"
     elif target_unit == "M":
          area *= 1609.34
          unit, target_unit = "Miles" , "Meters"
     elif target_unit == "FT":
          area *= 5279.98687656
          unit, target_unit = "Miles" , "Feet"
     elif target_unit == "I":
          area *= 63359.84251872
          unit, target_unit = "Miles" , "Inches"
     else:
          print(f"Conversion to {target_unit} is not supported")
elif unit == "FT":
     if target_unit == "KM":
          area *= 0.0003048
          unit, target_unit = "Feet" , "Kilometers"
     elif target_unit == "M":
          area *= 0.3048
          unit, target_unit = "Feet" , "Meters"
     elif target_unit == "MI":
          area *= 0.000189394
          unit,target_unit = "Feet" , "Miles"
     elif target_unit == "I":
          area *= 12
          unit, target_unit = "Feet" , "Inches"
     else:
          print(f"Conversion to {target_unit} is not supported")
elif unit == "I":
     if target_unit == "KM":
          area /= 39370.1
          unit, target_unit = "Inches" , "Kilometers"
     elif target_unit == "M":
          area /= 39.3701
          unit, target_unit = "Inches" , "Meters"
     elif target_unit == "FT":
          area /= 12
          unit, target_unit = "Inches" , "Feet"
     elif target_unit == "MI":
          area /= 63360
          unit, target_unit = "Inches" , "Miles"
     else:
          print(f"Conversion to {target_unit} is not supported")
  
print(f"Your converted area is: {area} {target_unit}")    