#!/usr/bin/python3
import os
import subprocess
import inquirer

#domain_text input
questions = [
        inquirer.Editor('domain_text', message="type in the domain(Press enter to in edit mode,no need for https://"),
        inquirer.List('dns',
                      message="choose dns",
                      choices=["ns1","godaddy","dnspod"]
                      ),

    ]
answers = inquirer.prompt(questions)
dns = answers['dns']

if answers['domain_text'] == '':
    print("Type in the domain,empty is not allowed")
    exit(1)

domain_text = answers['domain_text'].strip(' ')

if dns == "ns1":
    dns_add_script = "ns1_add_record.py"
    dns_clean_script = "ns1_del_record.py"

elif dns == "godaddy":
    dns_add_script = "godaddy_account1_add_record.py"
    dns_clean_script = "godaddy_account1_del_record.py"

elif dns == "dnspod":
    questions = [
        inquirer.List('account',
                    message="choose account",
                    choices=["account1","account2"]
                    )
    ]
    answers = inquirer.prompt(questions)
    account = answers['account']

    if account == "account1":
        dns_add_script = "dnspod_add_record_account1.py"
        dns_clean_script = "dnspod_del_record_account1.py"
    elif account == "account2":
        dns_add_script = "dnspod_add_record_account2.py"
        dns_clean_script = "dnspod_del_record_account2.py"
    else:
        print("pls choose one of the option.")

else:
    print("error happened,pls check.")
    exit (1)

#for multiple domain processing together
for dn in domain_text.split('\n'):
    if dn == "":
        continue
    certbot_command = [
        "certbot",
        "certonly",
        "-m", "testkd@gmail.com",
        "-d", "*." + dn,
        "--manual",
        "--non-interactive",
        "--agree-tos",
        "--preferred-challenges", "dns",
        "--manual-public-ip-logging-ok",
        "--work-dir", "./cert",
        "--config-dir", "./cert",
        "--logs-dir", "./cert",
        "--manual-auth-hook", "./dns_script/" + dns_add_script,
        "--manual-cleanup-hook", "./dns_script/" + dns_clean_script,
        "--force-renew"
    ]

# Run the command
try:
    result = subprocess.run(certbot_command,check=True,capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error from output:", e)
    print("Try again,because it has chances to failure")
    print("Pls also check the TXT record existed or not in the domain")