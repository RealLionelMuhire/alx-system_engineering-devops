#killing a running process in another window

exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
