#!/bin/bash

#apple_api_domain
#ls -l /etc/nginx/conf.d/api/apple | grep conf | grep -v test | awk -F ' ' '{print $9}' | sed 's/^api\.//; s/^appapi\.//; s/\.conf$//' > ./domain.txt

#xindaxiang_api_domain
#ls -l /etc/nginx/conf.d/api/xindaxiang | grep conf | grep -v test | awk -F ' ' '{print $9}' | sed 's/^api\.//; s/^appapi\.//; s/\.conf$//' >> ./domain.txt


function renew_cert() {
    certbot renew \
        --config-dir ./cert \
        --work-dir ./cert \
        --logs-dir ./cert
        #--dry-run
    	#--force-renewal \
}

function create_cert() {
    echo "create cert for $dn"
    certbot certonly \
    -m testkd@gmail.com \
    -d *.$dn \
    --manual \
    --non-interactive \
    --agree-tos \
    --preferred-challenges dns \
    --manual-public-ip-logging-ok \
    --work-dir ./cert \
    --config-dir ./cert \
    --logs-dir ./cert \
    --manual-auth-hook ./dns_script/${dns_auth_script} \
    --manual-cleanup-hook ./dns_script/${dns_clean_script}
    #--dry-run
    #--force-renew
}

function create_cert_cloudflare() {
    echo "create cert for $dn"
    certbot certonly \
        --dns-cloudflare \
        --dns-cloudflare-credentials ../../config/cdn/certbot-cloudflare.ini \
        -d *.$dn \
        -m testkd@gmail.com \
        --agree-tos \
        --non-interactive \
        --work-dir ./cert \
        --config-dir ./cert \
        --logs-dir ./cert
        # --force-renewal
        # --dry-run
}

function machine_ports() {
    if [ "$machine" == "web-api-guide" ]; then
        ports=(32275 32276)
    elif [ "$machine" == "console-web" ]; then
        ports=(32196)
    elif [ "$machine" == "nginx-console" ]; then
        ports=(32195)
    elif [ "$machine" == "web-api2" ]; then
        ports=(32155)
    fi
}

function send_file() {
    for port in "${ports[@]}"; do
        rsync -avzh -e "ssh -p ${port}" "${ssl_dir}" root@ip-address:/home/ubuntu/ssl/ > /dev/null
        echo "sending ${dn} files to $machine machines"
    done
}



function nginx_reload() {
    for port in "${ports[@]}"; do
        if ssh -p "${port}" root@ip-address 'nginx -t &> /dev/null'; then
            echo "Port ${port}: Nginx config test passed"
            ssh -p "${port}" root@ip-address 'nginx -s reload'
            ssh -p "${port}" root@ip-address 'systemctl status nginx'
        else
            echo "Port ${port}: Nginx config test failed"
            ssh -p "${port}" root@ip-address 'nginx -t'
            return 1
        fi
    done
}

function dns_sort() {
    local resolve=$(dig +noall +answer "$dn" -t ns | head -n 1 | awk -F ' ' '{print $5}')

    case "$resolve" in
        *cloudflare*)
            dns="cloudflare"
            ;;

        *domaincontrol*)
            dns="godaddy"
            dns_auth_script="godaddy_account1_add_record.py"
            dns_clean_script="godaddy_account1_del_record.py"
            ;;

        *dnspod*)
            dns="dnspod"
            if [ "$txt_file" == "web-api-guide.txt_dnspod_account1" ]; then
                dns_auth_script="dnspod_add_record_account1.py"
                dns_clean_script="dnspod_del_record_account1.py"
            elif [ "$txt_file" == "web-api-guide.txt_dnspod_account2" ]; then
                dns_auth_script="dnspod_add_record_account2.py"
                dns_clean_script="dnspod_del_record_account2.py"
            else
                dns_auth_script="dnspod_add_record.py"
                dns_clean_script="dnspod_del_record.py"
            fi
            ;;

        *ns1global*)
            dns="nsone"
            dns_auth_script="ns1_add_record.py"
            dns_clean_script="ns1_del_record.py"
            ;;

        *nsone*)
            dns="nsone"
            dns_auth_script="ns1_add_record.py"
            dns_clean_script="ns1_del_record.py"
            ;;

        "") #match empty resolve
            echo "Error: The nameserver resolve is empty for $dn" | tee -a /data/logs/resolve_error.log
            dns=""
            ;;

        *)
            echo "Unknown provider for $dn" | tee -a /data/logs/resolve_error.log
            dns=""
            ;;
    esac

}

#main process:starting with renew cert, then check cert_dir exist or not, if not create cert,
#then send new-cert or renew-cert to guid_host

renew_cert

if [[ ! -d /data/script/tool/certbot/send-cert ]]; then
  mkdir -p /data/script/tool/certbot/send-cert
fi

#get domain_name from txt files in the botton line
txt_files=(
    "web-api-guide.txt_dnspod_account1"
    "web-api-guide.txt_dnspod_account2"
    "web-api-guide.txt"
    "web-api2.txt"
    "nginx-console.txt"
    "console-web.txt"
)

for txt_file in "${txt_files[@]}"; do
    echo "Processing with file: $txt_file"
    machine=$(echo "$txt_file" | awk -F "." '{print $1}')
    echo "Machine: $machine"
    machine_ports

    # Check if file exists
    if [[ ! -f "/data/script/tool/certbot/txt_files/$txt_file" ]]; then
        echo "Warning: $txt_file not found" | tee -a /data/logs/certbot/process.log
        continue
    fi

    while IFS= read -r dn
    do
        work_dir="/data/script/tool/certbot"
        cert_dir="/data/script/tool/certbot/cert"
        dn_dir="/data/script/tool/certbot/cert/live/${dn}" #the latest cert is in live dir
        ssl_dir="/data/script/tool/certbot/send-cert/${machine}/${dn}"

        dns_sort #first check domain belongs to which dns

        #to check a cert_dir exist,example: doamin or domain-0001
        if [[ -d "$dn_dir" || -d "$(ls -d ${dn_dir}-* 2>/dev/null)" ]]; then
            rm -rf ${ssl_dir}
            mkdir -p ${ssl_dir}

            key_path=$(realpath "${dn_dir}/privkey.pem")
            pem_path=$(realpath "${dn_dir}/fullchain.pem")

            cp "$key_path" "$ssl_dir/privkey.pem"
            cp "$pem_path" "$ssl_dir/fullchain.pem"

        else

            if [[ "$dns" == "nsone" || "$dns" == "dnspod" || "$dns" == "godaddy" ]]; then
                create_cert

                # to check only one cert_dir exists
                if [[ $(cd ${cert_dir}/live && ls -l -t | grep $dn | wc -l) -gt 1 ]]; then
                    cd ${cert_dir}/live
                    old_dir=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_dir

                    cd ${cert_dir}/archive
                    old_dir=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_dir

                    cd ${cert_dir}/renewal
                    old_conf=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_conf

                    cd $work_dir
                fi

                rm -rf ${ssl_dir}
                mkdir -p ${ssl_dir}

                key_path=$(realpath "${dn_dir}/privkey.pem")
                pem_path=$(realpath "${dn_dir}/fullchain.pem")

                cp "$key_path" "$ssl_dir/privkey.pem"
                cp "$pem_path" "$ssl_dir/fullchain.pem"

            elif [[ "$dns" == "cloudflare" ]]; then
                create_cert_cloudflare

                # to check only one cert_dir exists
                if [[ $(cd ${cert_dir}/live && ls -l -t | grep $dn | wc -l) -gt 1 ]]; then
                    cd ${cert_dir}/live
                    old_dir=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_dir

                    cd ${cert_dir}/archive
                    old_dir=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_dir

                    cd ${cert_dir}/renewal
                    old_conf=$(ls -l -t | grep $dn | tail -n 1 | awk -F ' ' '{print $9}')
                    rm -rf $old_conf

                    cd $work_dir
                fi

                rm -rf ${ssl_dir}
                mkdir -p ${ssl_dir}

                key_path=$(realpath "${dn_dir}/privkey.pem")
                pem_path=$(realpath "${dn_dir}/fullchain.pem")

                cp "$key_path" "$ssl_dir/privkey.pem"
                cp "$pem_path" "$ssl_dir/fullchain.pem"

            else
                echo "Can't resolve the dns or unknown for $dn , continue to next one"
            fi

        fi

        send_file


    done < "/data/script/tool/certbot/txt_files/$txt_file"

    nginx_reload

    #gave it some time to reload nginx,due to the 3 successive web-api-guide files
    if [ "$machine" == "web-api-guide" ]; then
        sleep 10
    fi

done