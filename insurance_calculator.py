# create the initial variables below
# age : age of the individual in years
# sex : 0 for female, 1 for male
# bmi : individual's body mass index
# num_of_children : number of children the individual has
# smoker : 0 for a non-smoker, 1 for a smoker

age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below

insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

print ("This person's insurance cost is "+str(insurance_cost)+" dollars.")

# Age Factor
age += 4

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is "+str(change_in_insurance_cost)+" dollars.")

# BMI Factor

age = 28
bmi += 3.1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is "+str(change_in_insurance_cost)+" dollars.")

# Male vs. Female Factor

bmi = 26.2
sex = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost of being male instead of female is "+str(change_in_insurance_cost)+" dollars.")

# Smoker vs Non-smoker

sex = 0
smoker = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost of being a smoker instead of a non-smoker is "+str(change_in_insurance_cost)+" dollars.")

# number of children

smoker = 0
num_of_children = 0

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost of no children instead of having 3 children is "+str(change_in_insurance_cost)+" dollars.")