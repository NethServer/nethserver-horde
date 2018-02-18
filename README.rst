================
nethserver-horde
================

Horde is a full featured groupware written in PHP.

Features:

- Installed modules: core, imp, ingo, kronolith, nag
- Authentication: IMAP
- Automatic redirect to HTTPS
- Administrator user is set to ``admin``

The installation is accessible at ``http://<FQDN>/horde``.

Installation
============

Install using the command line: ::

  yum --enablerepo=nethforge-testing 

After installation, login with the admin user, go to ``Administration -> Configuration``
and apply the configuration.

TODO
====

Database
========

Configuration is saved in ``rhorde`` key inside ``configuration`` database.

Available properites:

* ``access``: can be ``public`` or ``private``, default is ``public``

  * *public*: webmail can be accessed from any networks
  * *private*: webmail can be accessed only from green interfaces and  trusted networks

Example: ::

  horde=configuration
    access=private


Configuration can be applied using: ::

  signal-event nethserver-horde-update

