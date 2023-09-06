# Configure Nginx so that its HTTP response contains a custom header on web-01 and web-02 servers

	exec {'update system':
		provider => 'shell';
		command  => 'sudo apt-get update';
	} ->
	
	package {'nginx':
		provider => 'apt';
		ensure => 'installed';
	} ->
	
	service {'nginx':
		ensure => 'running';
		enable => 'true';
	} ->

	file_line {'custom header':
		path   => '/etc/nginx/sites-available/default';
		ensure => 'present';
		after  => 'listen 80 default_server;';
		line   => 'add_header X-Served-By $hostname;';
	} ->
	
	exec {'restart nginx':
		provider  => 'shell';
		command => 'sudo service nginx restart';
	}
