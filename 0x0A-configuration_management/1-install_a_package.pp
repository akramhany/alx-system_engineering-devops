# A puppet script that installs flask from pip3 with version 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  name     => 'werkzeug',
  provider => 'pip3',
}
