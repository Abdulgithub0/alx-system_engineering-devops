#!/usr/bin/env bash
# install mysql version 5.7.x on web-01 and web-02
touch install_mysql.sh
chmod u+x install_mysql.sh
content=$(cat <<EOF
sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

EOF
)

echo "$content" >install_mysql.sh
scp install_mysql.sh signature.key ubuntu@35.153.18.178:~/
scp install_mysql.sh signature.key ubuntu@52.201.158.90:~/
rm {install_mysql.sh,signature.key}
echo "success"

