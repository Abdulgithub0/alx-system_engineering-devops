# Configure SSH client to use the private key
# Configure SSH client to refuse authenticate

file_line {'used_school_as_pk':
	ensure => 'present',
	path   => '~/.ssh/config',
	line   => '    IdentityFile ~/.ssh/school',
}

file_line {'disable_pw_format':
	ensure	=> 'present',
	path	=> '~/.ssh/config',
	line   	=> '    PasswordAuthentication no',
}
