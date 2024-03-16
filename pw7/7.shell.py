import subprocess

while True:
    command = input('$ ')  # User inputs command

    # Check for IO redirection operators: < (input from file), > (output to file)
    input_file = None
    output_file = None
    if '<' in command:
        parts = command.split('<', 1)
        command = parts[0].strip()
        input_file = parts[1].strip()
    if '>' in command:
        parts = command.split('>', 1)
        command = parts[0].strip()
        output_file = parts[1].strip()

    # Execute the command and handle IO redirection
    if input_file:
        with open(input_file, 'r') as f:
            input_data = f.read()
        result = subprocess.run(command, input=input_data, capture_output=True, shell=True, text=True)
    else:
        result = subprocess.run(command, capture_output=True, shell=True, text=True)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(result.stdout)
    else:
        print(result.stdout)