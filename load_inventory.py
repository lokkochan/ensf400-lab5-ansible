'''
This one is to look at the inventory of ansible, not the file
So we can check if the inventory of the thingy is what we want after we do the config.
Ping is also done here to check if connection to the container is set up correctly.
'''
import ansible_runner
import json

def display_all_host_ip_groups(inventory):
    """
    Displays all inventory hosts, IPs and groups
    """
    #Host and ip first, get the hosts dict
    hosts = inventory["_meta"]["hostvars"]
    #loop to print
    for name in hosts:
        ip = hosts[name]["ansible_host"]
        print(f"{name} ip : {ip}")

    #get the dict of groups
    groups = inventory["all"]["children"]
    #loop to print
    for group_name in groups:
        hosts = inventory[group_name]["hosts"]
        print(f"{group_name}:")
        #loop for the host
        for host_name in hosts:
            print(f"\t - {host_name}")


def cmd_ping_all():
    """
    Executes command "ansible all:localhost -m ping" and return the result.
    """
    #ping command
    command_to_run = "ansible all:localhost -m ping"

    # After the command is run, there are 3 elements returns [response, error_string, return_code]
    # response (str) - Message from execution
    # error_string (str) - Error message 
    # return_code (int)- Return code for performance or state of command execution
    response, error_string, return_code = ansible_runner.interface.run_command(executable_cmd=command_to_run)

    print(f"Response: \n{response}")


def main():
    inventory_file = "./hosts.yml"

    #Get inventory from the inventory file 
    inventory_str, warning = ansible_runner.interface.get_inventory(action="list",inventories=[inventory_file]) 
    # Use json.loads to convert str to dict.
    inventory = json.loads(inventory_str) #Runner interpretation of inventory file as json, similar to dict
    
    #print the names, IP addresses, and group names of all hosts.
    display_all_host_ip_groups(inventory)

    # ping
    cmd_ping_all()

if __name__ == "__main__":
    main()