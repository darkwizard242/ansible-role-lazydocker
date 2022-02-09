[![build-test](https://github.com/darkwizard242/ansible-role-lazydocker/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-lazydocker/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-lazydocker/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-lazydocker/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/49118?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/49118?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/49118?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-lazydocker&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-lazydocker) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-lazydocker&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-lazydocker) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-lazydocker&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-lazydocker) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-lazydocker&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-lazydocker) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-lazydocker?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-lazydocker?color=orange&style=flat-square)

# Ansible Role: lazydocker

Role to install (_by default_) [lazydocker](https://github.com/jesseduffield/lazydocker) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
lazydocker_app: lazydocker
lazydocker_version: '0.12'
lazydocker_dl_url: https://github.com/jesseduffield/{{ lazydocker_app }}/releases/download/v{{ lazydocker_version }}/{{ lazydocker_app }}_{{ lazydocker_version }}_{{ ansible_system }}_{{ ansible_architecture }}.tar.gz
lazydocker_bin_path: /usr/local/bin
lazydocker_file_owner: root
lazydocker_file_group: root
lazydocker_file_mode: '0755'
```

### Variables table:

Variable              | Description
--------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------
lazydocker_app        | Defines the app to install i.e. **lazydocker**
lazydocker_version    | Defined to dynamically fetch the desired version to install. Defaults to: **0.12**
lazydocker_dl_url     | Defines URL to download the lazydocker binary from.
lazydocker_bin_path   | Defined to dynamically set the appropriate path to store lazydocker binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
lazydocker_file_owner | Owner for the binary file of lazydocker.
lazydocker_file_group | Group for the binary file of lazydocker.
lazydocker_file_mode  | Mode for the binary file of lazydocker.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **lazydocker**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.lazydocker
```

For customizing behavior of role (i.e. specifying the desired **lazydocker** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.lazydocker
  vars:
    lazydocker_version: 0.8
```

For customizing behavior of role (i.e. placing binary of **lazydocker** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.lazydocker
  vars:
    lazydocker_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-lazydocker/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
