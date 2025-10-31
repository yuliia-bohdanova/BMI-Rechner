# BMI_Rechner
# Author: Yuliia Bohdanova
# 28.10.2025


# Eliza Brudkovitch
nameEB = "Eliza Brudkovitch"
heightEB_m = 1.7  # in Meter
weightEB_kg = 60  # in Kilogramm

# Mischell Prumis
nameMP = "Mischell Prumis"
heightMP_m = 1.65 
weightMP_kg = 53  

# Adam Richers
nameAR = "Adam Richers"
heightAR_m = 1.93 
weightAR_kg = 105


def bmi_calc(name, height_m,weight_kg):
    bmi = weight_kg / (height_m ** 2)
    bmi_round= f"{bmi: .2f}"

    if bmi < 25:
        return name + " is not overweight." + " BMI is:" + str(bmi_round)
    else:
        return name + " is overweight." + " BMI is:" + str(bmi_round)
    
resultEB = bmi_calc(nameEB, heightEB_m, weightEB_kg)
resultMP = bmi_calc(nameMP, heightMP_m, weightMP_kg)
resultAR = bmi_calc(nameAR, heightAR_m, weightAR_kg)

print(resultEB)
print(resultMP)
print(resultAR)
