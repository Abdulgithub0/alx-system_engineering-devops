# increase total open file for nginx

exec {'/usr/bin/sed':
  path    => '/usr/bin/',
  command => 'sed -i "s/15/4096/" /etc/default/nginx'
}

-> exec { 'restart':
  path    => '/etc/init.d/',
  command => 'nginx restart'
}
