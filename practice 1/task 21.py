def bmi(weight: float, height: float):
    return weight / height / height * 10000

def print_bmi(bmi: float):
    if bmi < 18.5:
        print('Underweight')
        return
    if bmi < 25:
        print('Normal')
        return
    if bmi < 30:
        print('Overweight')
        return
    print('Obesity')

inp = input().split(' ')
print_bmi(bmi(float(inp[0]), float(inp[1])))
