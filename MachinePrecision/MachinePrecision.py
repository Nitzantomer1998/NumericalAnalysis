# Machine Precision Finder


def find_machine_precision():
   
    computer_accuracy = 1

    loop_counter = 1

    while 1.0 + (computer_accuracy / 2) > 1.0:

        print_into_file([loop_counter, computer_accuracy, '\\', 2, '=', computer_accuracy / 2], None)

        computer_accuracy = computer_accuracy / 2
        loop_counter = loop_counter + 1

    print_into_file(None, f'\nThis Machine Maximum Accuracy --> {computer_accuracy}')

    print(f'This Machine Maximum Accuracy --> {computer_accuracy}')


def print_into_file(data, message):
    
    with open('Calculation.txt', 'a+') as file:

        if message:
            file.write(message)

        if data:
            for i in range(len(data)):
                if i == 0:
                    file.write('{: ^25}'.format(f'({data[0]})'))

                else:
                    file.write(f'{data[i]} ')
            file.write('\n')

def reset_file():
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Machine Precision Method -------------------------------\n')
        file.write('{: ^25}Calculation\n'.format('Iteration'))

# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Running the program
    print('---------- Machine Precision Method ----------')
    MachinePrecision()
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
