month_details = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']


# Function to calculate the average number of steps for each month.
def calculate_avg_steps(steps):
    avg_no_of_steps = [0] * 12
    no_of_days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculating total steps for each month
    for i, count in enumerate(steps):
        month_value = i % 12
        avg_no_of_steps[month_value] += count

    # Calculating the average steps for each month
    for i in range(12):
        avg_no_of_steps[i] //= no_of_days_month[i]

    return avg_no_of_steps


# Function to write average steps per month to a file.
def write_avg_steps(avg_no_of_steps):
    # Writes the average steps per month to a file.
    filename = "Avg Steps.txt"
    with open(filename, 'w') as f:
        f.write('Month        Average Steps\n')
        f.write('------------------------\n')
        for i in range(12):
            f.write(f'{month_details[i]:<10}: {avg_no_of_steps[i]:>8}\n')
        f.write('\nBy: Ashita Vemulapalli')


# Function to print average steps per month.
def print_avg_steps(avg_no_of_steps):
    # Prints the average steps per month.
    print('Month       Average Steps')
    print('------------------------')
    for i in range(12):
        print(f'{month_details[i]:<9}   {avg_no_of_steps[i]:>8}')


# Main function to calculate and print average steps per month.
def main_function():
    with open('steps.txt', 'r') as f:
        steps = [int(line.strip()) for line in f]

    avg_no_of_steps = calculate_avg_steps(steps)
    write_avg_steps(avg_no_of_steps)
    print_avg_steps(avg_no_of_steps)


# calling the main funtion to go through the process accomplish the given task
main_function()
