import math

def plus():
    while True:
        try:
            print("\nYOU CHOOSE '+' OPERATOR")
            a = int(input("FIRST NUMBER: "))
            b = int(input("SECOND NUMBER :"))
            result = a+b
            print(f"RESULT {a} + {b} =", result)
            return
        except ValueError:
            print('INVALID, PLEASE ENTER THE NUMBER.') 

def min():
     while True:
        try:
            print("\nYOU CHOOSE '-' OPERATOR")
            a = int(input("FIRST NUMBER: "))
            b = int(input("SECOND NUMBER :"))
            result = a-b
            print(f"RESULT {a} - {b} =", result)
            return
        except ValueError:
            print('INVALID, PLEASE ENTER THE NUMBER.') 

def multiply():
     while True:
        try:
            print("\nYOU CHOOSE '*' OPERATOR")
            a = int(input("FIRST NUMBER: "))
            b = int(input("SECOND NUMBER :"))
            result = a*b
            print(f"RESULT {a} * {b} =", result)
            return
        except ValueError:
            print('INVALID, PLEASE ENTER THE NUMBER.') 

def div():
     while True:
        try:
            print("\nYOU CHOOSE \ OPERATOR")
            a = float(input("FIRST NUMBER: "))
            b = float(input("SECOND NUMBER :"))
            result = a/b
            print(f"RESULT {a} \ {b} =", result)
            return
        except ValueError:
            print('INVALID, PLEASE ENTER THE NUMBER.')
        except ZeroDivisionError:
            print("CANNOT DEVIDE BY ZERO")

def exponential():
        try:
            print("\nYOU CHOOSE ** OPERATOR")
            a = int(input("FIRST NUMBER: "))
            b = int(input("SECOND NUMBER :"))
            result = a**b
            print(f"RESULT {a} ** {b} =", result)
            return
        except ValueError:
            print('INVALID, PLEASE ENTER THE NUMBER.')

def square_root():
    try:
        num = float(input("NUMBER: "))
        result = math.sqrt(num)
        print(f"THE SQUARE ROOT OF {num} IS {result:.2f}")
    except ValueError:
        print("Error: INPUT MUST BE A NUMBER >= 0")

def logaritm():
        try:
            number = float(input("ENTER A NUMBER (MUST BE > 0): "))
            base = input("ENTER A LOGARITHM BASE (leave empty for natural log): ")

            if number <= 0:
                print("Error: LOGARITHM IS DEFINED NEGATIVE!")
                return

            if base.strip() == "":
                result = math.log(number)  
                print(f"lN({number}) = {result:.4f}")
            else:
                base = float(base)
                if base <= 0 or base == 1:
                    print("Error: LOGARITHM MUST BE > 0 AND NOT EQUAL 1")
                    return
                result = math.log(number, base)
                print(f"log base {base} of {number} = {result:.4f}")
        except ValueError:
            print("Error: INPUT MUST BE A NUMBER!")

#TRIGONOMETRIC SIN COS TAN
def sine(angle_deg: float) -> float:
    return math.sin(math.radians(angle_deg))

def cosine(angle_deg: float) -> float:
    return math.cos(math.radians(angle_deg))

def tangent(angle_deg: float) -> float:
    return math.tan(math.radians(angle_deg))

def scientific_calculator():
    operations = {
        "1": ("Sine", sine),
        "2": ("Cosine", cosine),
        "3": ("Tangent", tangent),
    }

    print("=== Scientific Calculator ===")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("0. EXIT")

    while True:
        choice = input("\nCHOOSE OPERATION: ").strip()
        if choice == "0":
            print("GOODBYE!")
            break

        if choice in operations:
            try:
                angle = float(input("ENTER ANGLE IN DEGRESS: "))
                func = operations[choice][1]
                result = func(angle)
                print(f"{operations[choice][0]}({angle}°) = {result:.4f}")
            except ValueError:
                print("Error: PLEASE ENTER A VALID NUMBER.")
        else:
            print("INVALID CHOICE!")

def choose():
    while True:
        try:
            print("\n=================")
            print("MY CALCULATOR")
            print("=================")
            print("OPERATOR:")
            print("1. + PLUS")
            print("2. - MIN")
            print("3. * MULTIPLY")
            print("4. / DIVISION")
            print("5. ** EXPONENTIAL")
            print("6. SQUARE ROOT ")
            print("7. LOGARITHM")
            print("8. TRIGONOMETRY")
            print("0. EXIT PROGRAM")
            user = int(input("CHOOSE OPERATOR 1/2/3/4/6/7/8/0: "))
            if user == 1:
                plus()
            elif user == 2:
                min()
            elif user == 3:
                multiply()
            elif user == 4:
                div()
            elif user == 5:
                exponential()
            elif user == 6:
                square_root()
            elif user == 7:
                logaritm()
            elif user == 8:
                scientific_calculator()
            elif user == 0:
                print("THANKYOU, HAPPY A NICEDAY.")
                exit()
            if user > 8:
                print("ENTER A NUMBER, NO MORE THAN 8.")
        except ValueError:
            print('invalid: PLEASE ENTER THE NUMBER')
choose()

