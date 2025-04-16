# Certbot Automation

## Installation

### Certbot

1. Install snapd via apt  
    sudo apt update  
    sudo apt install snapd  

2. Install certbot  
    sudo snap install --classic certbot  
    sudo ln -s /snap/bin/certbot /usr/bin/certbot  

3. Install plugin (If you need to install other plugin,need to re run this part)  
    sudo snap set certbot trust-plugin-with-root=ok  
    sudo snap install certbot-dns-cloudflare  
    eg. sudo snap install certbot-dns-<PLUGIN>  

### Dnspod-sdk  

1. Using the dnspod package in dns_package folder need to install the tencentcloud-sdk-python in the dnspod [README.md](./dns_package/dnspod/README.md)

---

## Summary  
Certbot is a tool for applying certificate and auto-renew the certificate.  
The Certbot using in here is in a main machine to generate certificate for other machine in this project.
[Official-site](https://certbot.eff.org/)  

***
## Certbot folder tree explain  
| cert_dir_path | - |
| - | - |
| ./cert/live | Include link file which are private pem and key using for the domain. |
| ./cert/archive | The actuall files of pem and key. |
| ./cert/renewal | Including the information needed for certificate renewal process. |
***

## Instructions

1. Combine certbot and dns python script to create a auto-process,which can auto-generate certificate and renew certificate,also can choose different dns and account.  

    - 1-1. usage: ./create_ssl_new.py  
    Then type in domain ,and choose dns and account.  

2. certbot-renew.sh execute on Monday 10AM.  
    - 2-1. Auto checking the domain in ./cert/renewal folder will be expire in 30 days or not. If the validity period less than 30 days,the process renew the certificate,and also delete the txt record automatically after the process.  

    - 2-2. If the txt file contains new domain, it will generate the certificate automatically in the process.  

    - 2-3. If you want to delete the expired domain,you need to delete the domain part in the correspnding txt file,and the domain folder in the live,renewal,archive folder in the /certbot/cert path, that calls a complete deleting process.  

    - 2-4. Depending on different txt-files,the process send the pem and key to /home/ubuntu/ssl/domain_dir folder in the chosen machine to change the certificate.  

    - 2-5. If there is a new machine which wants auto-generated pem and key, just add a new txt file in the txt dir,and add the txt_file machine_port in the code.  
    
    - 2-6. txt-file format：machine.txt_dns_account (Only the domain in dnspod need the tail part like that(dns_account),which is for choosing the right dns_script to use,other dns would be just using machine.txt)

    - 2-7. Be careful when copy domains to txt-file,can't have a new line symble in the bottem,or the process could lead to fail on reading the last domain in the txt-file,it just ignore the last one.(Error: line 173)  


3. Crontab rule.  
    - Update the certificate in all machines.  
        0 10 * * 1  cd /data/script/tool/certbot && ./certbot-renew.sh >> /data/logs/certbot/process.log 2>&1  
        (Log is in "/data/logs/certbot/process.log" set by crontab.)  
---

# All the import in project need to be modified , wait for me!! ><