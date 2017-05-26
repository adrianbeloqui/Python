def checkFraud(coefficients, values):
    total = coefficients[0]
    i = 0
    while (i<len(values)):
        total += coefficients[i+1]*values[i]
        i+=1
    return total

def processPayment(coefficients):
    endOfFile = False
    while (not endOfFile):
        try:
            values = map(float, raw_input().strip().split(','))
        except:
            return
        result = checkFraud(coefficients, values)
        if result > 0:
            print("suspect fraud")
        elif result <= 0:
            print("not fraud")
        
coefficients = map(float, raw_input().strip().split(','))
processPayment(coefficients)
