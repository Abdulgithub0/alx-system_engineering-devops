# manifests to install flask on a puppet host

package { 'install flask V2.1.0':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
