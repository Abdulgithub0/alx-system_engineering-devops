# Resolve open files limit isssues for user holberton.
exec { 'increase hard limit':
  command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/bin/'
}

exec { 'increase soft limit':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/bin/'
}
