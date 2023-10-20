# Resolve open files limit isssues for user holberton.

exec { 'increase soft limit':
  path    => '/usr/bin/',
  command => 'sed -i "/holberton	soft  nofile  10000/" /etc/security/limits.conf',
}

exec { 'increase hard limit':
  command => 'sed -i "/holberton	hard  nofile  20000/" /etc/security/limits.conf',
  path    => '/usr/bin'
}
