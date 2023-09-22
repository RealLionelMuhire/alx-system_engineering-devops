#ensuring and installing the flask and its version

package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3'
}
