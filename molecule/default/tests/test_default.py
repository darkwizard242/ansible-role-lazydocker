import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lazydocker_binary_exists(host):
    assert host.file('/usr/local/bin/lazydocker').exists


def test_lazydocker_binary_file(host):
    assert host.file('/usr/local/bin/lazydocker').is_file


def test_lazydocker_binary_which(host):
    assert host.check_output('which lazydocker') == '/usr/local/bin/lazydocker'
