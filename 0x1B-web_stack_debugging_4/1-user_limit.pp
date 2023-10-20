# Resolve open files limit isssues for user holberton.

exec { 'increase soft limit':
  command => "sed -i '/holberton        soft  nofile  10000/' /etc/security/limits.conf",
  path    => '/usr/bin',
}

exec { 'increase hard limit':
  command => "sed -i '/holberton        hard  nofile  20000/' /etc/security/limits.conf",
  path    => '/usr/bin',
}

