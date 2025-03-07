import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')
    continue_calc = 'y'
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ').strip().lower()
        while continue_calc not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = input('Enter more (y/n): ').strip().lower()
        if continue_calc == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'Current result: {ans}')
        values_entered += 1
        
    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')
    continue_calc = 'y'
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 - num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ').strip().lower()
        while continue_calc not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = input('Enter more (y/n): ').strip().lower()
        if continue_calc == 'n':
            break
        num = float(input('Enter another number: '))
        ans -= num
        print(f'Current result: {ans}')
        values_entered += 1
        
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')
    continue_calc = 'y'
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ').strip().lower()
        while continue_calc not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = input('Enter more (y/n): ').strip().lower()
        if continue_calc == 'n':
            break
        num = float(input('Enter another number: '))
        ans *= num
        print(f'Current result: {ans}')
        values_entered += 1
        
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')
    continue_calc = 'y'
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number (non-zero): '))
    
    while num_2 == 0.0:
        print('Please enter a number greater than 0')
        num_2 = float(input('Enter another number: '))
        
    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ').strip().lower()
        while continue_calc not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = input('Enter more (y/n): ').strip().lower()
        if continue_calc == 'n':
            break
        num = float(input('Enter another number (non-zero): '))
        while num == 0.0:
            print('Please enter a number greater than 0')
            num = float(input('Enter another number: '))
        ans /= num
        print(f'Current result: {ans}')
        values_entered += 1
        
    return [ans, values_entered]

def calculator():
    while True:
        print('\nSimple Calculator in Python!')
        print('Enter "a" for addition')
        print('Enter "s" for subtraction')
        print('Enter "m" for multiplication')
        print('Enter "d" for division')
        print('Enter "q" to quit')
        
        choice = input('Selection: ').strip().lower()
        
        if choice == 'q':
            print("Thank you for using the calculator!")
            break
        
        if choice == 'a':
            results = addition()
        elif choice == 's':
            results = subtraction()
        elif choice == 'm':
            results = multiplication()
        elif choice == 'd':
            results = division()
        else:
            print('Invalid selection. Please try again.')
            continue
        
        print(f'Ans = {results[0]}, Total inputs: {results[1]}')

if __name__ == '__main__':
    calculator()