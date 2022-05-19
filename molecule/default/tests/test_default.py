import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssm_package(host):
    assert host.package("amazon-ssm-agent").is_installed


def test_ssm_files(host):
    assert host.file("/etc/amazon/ssm").is_directory
    assert host.file("/usr/bin/amazon-ssm-agent").is_file
    assert host.file("/usr/bin/amazon-ssm-agent").mode == 0o755
