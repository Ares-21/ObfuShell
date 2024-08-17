import re
import uuid
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_ascii_art():
    """Prints the custom ASCII art."""
    print(Fore.CYAN + """
     
┌─┐┌┐ ┌─┐┬ ┬┌─┐┬ ┬┌─┐┬  ┬  
│ │├┴┐├┤ │ │└─┐├─┤├┤ │  │  
└─┘└─┘└  └─┘└─┘┴ ┴└─┘┴─┘┴─┘ v1.3 by aakash
                                                 
    """)  

def get_file_content(path):
    """Reads the content of a file."""
    with open(path, 'r') as f:
        return f.read()

def randomize_variables(payload):
    """Randomizes the variable names in a PowerShell script."""
    used_var_names = []

    # Identify variables definitions in script
    variable_definitions = re.findall(r'\$[a-zA-Z0-9_]*[\ ]{0,}=', payload)
    variable_definitions.sort(key=len)
    variable_definitions.reverse()

    # Replace variable names
    for var in variable_definitions:
        var = var.strip("\n \r\t=")

        while True:
            new_var_name = uuid.uuid4().hex

            if (new_var_name in used_var_names) or (re.search(new_var_name, payload)):
                continue
            else:
                used_var_names.append(new_var_name)
                break

        payload = payload.replace(var, f'${new_var_name}')
    
    return payload

def main():
    print_ascii_art()
    
    print(Fore.YELLOW + "Welcome to ObfusShell v1.3")
    print(Fore.YELLOW + "This tool will help you randomize variable names to obfuscate your script.")
    print(Fore.GREEN + "\nEnter your PowerShell script content or path to file:")

    # Input for PowerShell script content
    script_content = input(Fore.BLUE + "> ")

    # Check if it's a path or direct content
    if script_content.strip().startswith("/") or "\\" in script_content:
        payload = get_file_content(script_content.strip())
    else:
        payload = script_content.strip()

    obfuscated_payload = randomize_variables(payload)
    
    print(Fore.CYAN + "\nObfuscated PowerShell script:\n")
    print(Fore.WHITE + obfuscated_payload)
    print(Fore.GREEN + "\nObfuscation complete!")

if __name__ == "__main__":
    main()
