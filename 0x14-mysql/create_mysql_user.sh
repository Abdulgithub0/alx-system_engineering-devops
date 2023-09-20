#!/usr/bin/env bash
# create a user and password for MySQL databases instance on web-01 and web-02 for checker to work with
new_user=$(cat <<EOF
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
EOF
)
echo "$new_user" >holberton_user.sql
scp holberton_user.sql ubuntu@35.153.18.178:~/
scp holberton_user.sql ubuntu@52.201.158.90:~/
rm holberton_user.sql
echo "success"
