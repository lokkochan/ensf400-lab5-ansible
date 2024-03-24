"""
Use runner to run the command to run the ansible playbook ($ ansible-playbook hello.yml)
"""
import ansible_runner
import requests

def main():
    command = "ansible-playbook ./hello.yml"
    # Executes the playbook running command 'ansible-playbook /path/to/playbook.yml'
    # save the return result
    response, error_string, return_code = ansible_runner.interface.run_command(executable_cmd=command)
    print(f"Response: {response}")

    # verify the response of the servers
    for i in range(3):
        response = requests.get('http://0.0.0.0')
        expected_string = f"Hello World from managedhost-app-{i+1} !"
        if response.text == expected_string:
            print("Response matches the expected string:", response.text)
        else:
            print("Response doesn't match the expected string. Expected:", expected_string, "but got:", response.text)

if __name__ == "__main__":
    main()