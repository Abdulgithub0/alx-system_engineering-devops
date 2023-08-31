# Install and configure Nginx server with a 301 redirect

package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => "Hello World!\n",
  require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  hasstatus => true,
  hasrestart => true,
  require   => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}

