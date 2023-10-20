# increase total open file for nginx

exec {'increase open files':
	command => ' sudo sed -i "s/15/4096/" /etc/default/nginx',
     }
     ->
exec {'restart nginx':
	command => 'sudo service nginx restart'
     }
