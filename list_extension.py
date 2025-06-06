import subprocess 
def list_vscode_extension():
    try:
        result = subprocess.run(['code','--list-extensions'],capture_output=True,text=True,check=True)
        extensions = result.stdout.splitlines() 
        for ext in extensions:
            print(ext) 
    except subprocess.CalledProcessError as e: 
        print(f'an error occurred:{e}')
list_vscode_extension()