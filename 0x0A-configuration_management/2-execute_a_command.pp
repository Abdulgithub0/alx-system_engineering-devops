#This manifests kill a running process call killmenow

exec { 'killer killmenow':
  command  => '/usr/bin/pkill killmenow',
}
