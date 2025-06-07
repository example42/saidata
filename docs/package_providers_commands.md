# Chocolatey actions

```
PS C:\Windows\system32> choco -?
This is a listing of all of the different things you can pass to choco.

Options and Switches

 -v, --version
     Version - Prints out the Chocolatey version.

Commands

 * apikey - retrieves, saves or deletes an API key for a particular source
 * cache - Manage the local HTTP caches used to store queries (v2.1.0+)
 * config - Retrieve and configure config file settings
 * export - exports list of currently installed packages
 * feature - view and configure choco features
 * features - view and configure choco features (alias for feature)
 * find - searches remote packages (alias for search)
 * help - displays top level help information for choco
 * info - retrieves package information. Shorthand for choco search pkgname --exact --verbose
 * install - installs packages using configured sources
 * list - lists local packages
 * new - creates template files for creating a new Chocolatey package
 * outdated - retrieves information about packages that are outdated. Similar to upgrade all --noop
 * pack - packages nuspec, scripts, and other Chocolatey package resources into a nupkg file
 * pin - suppress upgrades for a package
 * push - pushes a compiled nupkg to a source
 * rule - view or list implemented package rules (v2.3.0+)
 * search - searches remote packages
 * setapikey - retrieves, saves or deletes an API key for a particular source (alias for apikey)
 * source - view and configure default sources
 * sources - view and configure default sources (alias for source)
 * template - get information about installed templates
 * templates - get information about installed templates (alias for template)
 * uninstall - uninstalls a package
 * unpackself - [DEPRECATED] will be removed in v3.0.0 - re-installs Chocolatey base files
 * upgrade - upgrades packages from various sources
```


# Winget

```
PS C:\Windows\system32> winget
Windows Package Manager v1.1.12986
Copyright (c) Microsoft Corporation. All rights reserved.

The winget command line utility enables installing applications and other packages from the command line.

usage: winget [<command>] [<options>]

The following commands are available:
  install    Installs the given package
  show       Shows information about a package
  source     Manage sources of packages
  search     Find and show basic info of packages
  list       Display installed packages
  upgrade    Upgrades the given package
  uninstall  Uninstalls the given package
  hash       Helper to hash installer files
  validate   Validates a manifest file
  settings   Open settings or set administrator settings
  features   Shows the status of experimental features
  export     Exports a list of the installed packages
  import     Installs all the packages in a file

For more details on a specific command, pass it the help argument. [-?]

The following options are available:
  -v,--version  Display the version of the tool
  --info        Display general info of the tool
```

# Scoop

```
PS C:\Users\al> scoop
Usage: scoop <command> [<args>]

Available commands are listed below.

Type 'scoop help <command>' to get more help for a specific command.

Command    Summary
-------    -------
alias      Manage scoop aliases
bucket     Manage Scoop buckets
cache      Show or clear the download cache
cat        Show content of specified manifest.
checkup    Check for potential problems
cleanup    Cleanup apps by removing old versions
config     Get or set configuration values
create     Create a custom app manifest
depends    List dependencies for an app, in the order they'll be installed
download   Download apps in the cache folder and verify hashes
export     Exports installed apps, buckets (and optionally configs) in JSON format
help       Show help for a command
hold       Hold an app to disable updates
home       Opens the app homepage
import     Imports apps, buckets and configs from a Scoopfile in JSON format
info       Display information about an app
install    Install apps
list       List installed apps
prefix     Returns the path to the specified app
reset      Reset an app to resolve conflicts
search     Search available apps
shim       Manipulate Scoop shims
status     Show status and check for new app versions
unhold     Unhold an app to enable updates
uninstall  Uninstall an app
update     Update apps, or Scoop itself
virustotal Look for app's hash or url on virustotal.com
which      Locate a shim/executable (similar to 'which' on Linux)
```


# pip on windows

```
PS C:\Windows\system32> pip

Usage:
  C:\Users\al\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging
                              them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user
                              configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding
                              to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or
                              any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See
                              'SSL Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is
                              available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```


# pip on mac

```
MacBookPro:~ al$ pip3

Usage:   
  pip3 <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging
                              levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [auto, disabled,
                              import, subprocess]. (default: auto)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip
                              documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```


# brew

```
MacBookPro:~ al$ brew commands
==> Built-in commands
--cache          alias            commands         doctor           install          nodenv-sync      readall          tap-info         update-report
--caskroom       analytics        completions      fetch            leaves           options          reinstall        tap              update-reset
--cellar         autoremove       config           formulae         link             outdated         search           unalias          update
--env            bundle           deps             gist-logs        list             pin              services         uninstall        upgrade
--prefix         casks            desc             help             log              postinstall      setup-ruby       unlink           uses
--repository     cleanup          developer        home             migrate          pyenv-sync       shellenv         unpin            vendor-install
--version        command          docs             info             missing          rbenv-sync       tab              untap

==> Built-in developer commands
audit                     create                    generate-cask-api         pr-publish                style                     update-python-resources
bottle                    debugger                  generate-cask-ci-matrix   pr-pull                   tap-new                   update-sponsors
bump-cask-pr              determine-test-runners    generate-formula-api      pr-upload                 test                      update-test
bump-formula-pr           dispatch-build-bottle     generate-man-completions  prof                      tests                     vendor-gems
bump-revision             edit                      install-bundler-gems      release                   typecheck                 verify
bump-unversioned-casks    extract                   irb                       rubocop                   unbottled
bump                      formula-analytics         linkage                   ruby                      unpack
cat                       formula                   livecheck                 rubydoc                   update-license-data
contributions             generate-analytics-api    pr-automerge              sh                        update-maintainers
```


# apt

```
al@lab:~$ apt --help
apt 2.4.13 (amd64)
Usage: apt [options] command

apt is a commandline package manager and provides commands for
searching and managing as well as querying information about packages.
It provides the same functionality as the specialized APT tools,
like apt-get and apt-cache, but enables options more suitable for
interactive use by default.

Most used commands:
  list - list packages based on package names
  search - search in package descriptions
  show - show package details
  install - install packages
  reinstall - reinstall packages
  remove - remove packages
  autoremove - Remove automatically all unused packages
  update - update list of available packages
  upgrade - upgrade the system by installing/upgrading packages
  full-upgrade - upgrade the system by removing/installing/upgrading packages
  edit-sources - edit the source information file
  satisfy - satisfy dependency strings
```

# gem

```
 GEM commands are:

    build             Build a gem from a gemspec
    cert              Manage RubyGems certificates and signing settings
    check             Check a gem repository for added or missing files
    cleanup           Clean up old versions of installed gems
    contents          Display the contents of the installed gems
    dependency        Show the dependencies of an installed gem
    environment       Display information about the RubyGems environment
    fetch             Download a gem and place it in the current directory
    generate_index    Generates the index files for a gem server directory
    help              Provide help on the 'gem' command
    info              Show information for the given gem
    install           Install a gem into the local repository
    list              Display local gems whose name matches REGEXP
    lock              Generate a lockdown list of gems
    mirror            Mirror all gem files (requires rubygems-mirror)
    open              Open gem sources in editor
    outdated          Display all gems that need updates
    owner             Manage gem owners of a gem on the push server
    pristine          Restores installed gems to pristine condition from files
                      located in the gem cache
    push              Push a gem up to the gem server
    rdoc              Generates RDoc for pre-installed gems
    search            Display remote gems whose name matches REGEXP
    server            Starts up a web server that hosts the RDoc (requires
                      rubygems-server)
    signin            Sign in to any gemcutter-compatible host. It defaults to
                      https://rubygems.org
    signout           Sign out from all the current sessions.
    sources           Manage the sources and cache file RubyGems uses to search
                      for gems
    specification     Display gem specification (in yaml)
    stale             List gems along with access times
    uninstall         Uninstall gems from the local repository
    unpack            Unpack an installed gem to the current directory
    update            Update installed gems to the latest version
    which             Find the location of a library file you can require
    yank              Remove a pushed gem from the index
```

# yum

```
usage: yum [options] COMMAND

List of Main Commands:

alias                     List or create command aliases
autoremove                remove all unneeded packages that were originally installed as dependencies
check                     check for problems in the packagedb
check-update              check for available package upgrades
clean                     remove cached data
deplist                   [deprecated, use repoquery --deplist] List package's dependencies and what packages provide them
distro-sync               synchronise installed packages to the latest available versions
downgrade                 Downgrade a package
group                     display, or use, the groups information
help                      display a helpful usage message
history                   display, or use, the transaction history
info                      display details about a package or group of packages
install                   install a package or packages on your system
list                      list a package or groups of packages
makecache                 generate the metadata cache
mark                      mark or unmark installed packages as installed by user.
module                    Interact with Modules.
provides                  find what package provides the given value
reinstall                 reinstall a package
remove                    remove a package or packages from your system
repolist                  display the configured software repositories
repoquery                 search for packages matching keyword
repository-packages       run commands on top of all packages in given repository
search                    search package details for the given string
shell                     run an interactive YUM shell
swap                      run an interactive YUM mod for remove and install one spec
updateinfo                display advisories about packages
upgrade                   upgrade a package or packages on your system
upgrade-minimal           upgrade, but only 'newest' package match which fixes a problem that affects your system

List of Plugin Commands:

builddep                  Install build dependencies for package or spec file
changelog                 Show changelog data of packages
config-manager            manage yum configuration options and repositories
copr                      Interact with Copr repositories.
debug-dump                dump information about installed rpm packages to file
debug-restore             restore packages recorded in debug-dump file
debuginfo-install         install debuginfo packages
download                  Download package to current directory
groups-manager            create and edit groups metadata file
kpatch                    Toggles automatic installation of kpatch-patch packages
needs-restarting          determine updated binaries that need restarting
playground                Interact with Playground repository.
repoclosure               Display a list of unresolved dependencies for repositories
repodiff                  List differences between two sets of repositories
repograph                 Output a full package dependency graph in dot format
repomanage                Manage a directory of rpm packages
reposync                  download all packages from remote repo
uploadprofile             Upload combined profile to Satellite server (list of installed rpms, enabled repositories and modules

General YUM options:
  -c [config file], --config [config file]
                        config file location
  -q, --quiet           quiet operation
  -v, --verbose         verbose operation
  --version             show YUM version and exit
  --installroot [path]  set install root
  --nodocs              do not install documentations
  --noplugins           disable all plugins
  --enableplugin [plugin]
                        enable plugins by name
  --disableplugin [plugin]
                        disable plugins by name
  --releasever RELEASEVER
                        override the value of $releasever in config and repo
                        files
  --setopt SETOPTS      set arbitrary config and repo options
  --skip-broken         resolve depsolve problems by skipping packages
  -h, --help, --help-cmd
                        show command help
  --allowerasing        allow erasing of installed packages to resolve
                        dependencies
  -b, --best            try the best available package versions in
                        transactions.
  --nobest              do not limit the transaction to the best candidate
  -C, --cacheonly       run entirely from system cache, don't update cache
  -R [minutes], --randomwait [minutes]
                        maximum command wait time
  -d [debug level], --debuglevel [debug level]
                        debugging output level
  --debugsolver         dumps detailed solving results into files
  --showduplicates      show duplicates, in repos, in list/search commands
  -e ERRORLEVEL, --errorlevel ERRORLEVEL
                        error output level
  --obsoletes           enables yum's obsoletes processing logic for upgrade
                        or display capabilities that the package obsoletes for
                        info, list and repoquery
  --rpmverbosity [debug level name]
                        debugging output level for rpm
  -y, --assumeyes       automatically answer yes for all questions
  --assumeno            automatically answer no for all questions
  --enablerepo [repo]   Enable additional repositories. List option. Supports
                        globs, can be specified multiple times.
  --disablerepo [repo]  Disable repositories. List option. Supports globs, can
                        be specified multiple times.
  --repo [repo], --repoid [repo]
                        enable just specific repositories by an id or a glob,
                        can be specified multiple times
  --enable              enable repos with config-manager command
                        (automatically saves)
  --disable             disable repos with config-manager command
                        (automatically saves)
  -x [package], --exclude [package], --excludepkgs [package]
                        exclude packages by name or glob
  --disableexcludes [repo], --disableexcludepkgs [repo]
                        disable excludepkgs
  --repofrompath [repo,path]
                        label and path to an additional repository to use
                        (same path as in a baseurl), can be specified multiple
                        times.
  --noautoremove        disable removal of dependencies that are no longer
                        used
  --nogpgcheck          disable gpg signature checking (if RPM policy allows)
  --color COLOR         control whether colour is used
  --refresh             set metadata as expired before running the command
  -4                    resolve to IPv4 addresses only
  -6                    resolve to IPv6 addresses only
  --destdir DESTDIR, --downloaddir DESTDIR
                        set directory to copy packages to
  --downloadonly        only download packages
  --comment COMMENT     add a comment to transaction
  --bugfix              Include bugfix relevant packages, in updates
  --enhancement         Include enhancement relevant packages, in updates
  --newpackage          Include newpackage relevant packages, in updates
  --security            Include security relevant packages, in updates
  --advisory ADVISORY, --advisories ADVISORY
                        Include packages needed to fix the given advisory, in
                        updates
  --bz BUGZILLA, --bzs BUGZILLA
                        Include packages needed to fix the given BZ, in
                        updates
  --cve CVES, --cves CVES
                        Include packages needed to fix the given CVE, in
                        updates
  --sec-severity {Critical,Important,Moderate,Low}, --secseverity {Critical,Important,Moderate,Low}
                        Include security relevant packages matching the
                        severity, in updates
  --forcearch ARCH      Force the use of an architecture


```


# dnf

```
[al@macone-redhat9 ~]$ dnf
Not root, Subscription Management repositories not updated

This system is not registered with an entitlement server. You can use subscription-manager to register.

  
usage: dnf [options] COMMAND

List of Main Commands:

alias                     List or create command aliases
autoremove                remove all unneeded packages that were originally installed as dependencies
check                     check for problems in the packagedb
check-update              check for available package upgrades
clean                     remove cached data
deplist                   [deprecated, use repoquery --deplist] List package's dependencies and what packages provide them
distro-sync               synchronise installed packages to the latest available versions
downgrade                 Downgrade a package
group                     display, or use, the groups information
help                      display a helpful usage message
history                   display, or use, the transaction history
info                      display details about a package or group of packages
install                   install a package or packages on your system
list                      list a package or groups of packages
makecache                 generate the metadata cache
mark                      mark or unmark installed packages as installed by user.
module                    Interact with Modules.
provides                  find what package provides the given value
reinstall                 reinstall a package
remove                    remove a package or packages from your system
repolist                  display the configured software repositories
repoquery                 search for packages matching keyword
repository-packages       run commands on top of all packages in given repository
search                    search package details for the given string
shell                     run an interactive DNF shell
swap                      run an interactive DNF mod for remove and install one spec
updateinfo                display advisories about packages
upgrade                   upgrade a package or packages on your system
upgrade-minimal           upgrade, but only 'newest' package match which fixes a problem that affects your system

List of Plugin Commands:

builddep                  Install build dependencies for package or spec file
changelog                 Show changelog data of packages
config-manager            manage dnf configuration options and repositories
copr                      Interact with Copr repositories.
debug-dump                dump information about installed rpm packages to file
debug-restore             restore packages recorded in debug-dump file
debuginfo-install         install debuginfo packages
download                  Download package to current directory
groups-manager            create and edit groups metadata file
kpatch                    Toggles automatic installation of kpatch-patch packages
needs-restarting          determine updated binaries that need restarting
playground                Interact with Playground repository.
repoclosure               Display a list of unresolved dependencies for repositories
repodiff                  List differences between two sets of repositories
repograph                 Output a full package dependency graph in dot format
repomanage                Manage a directory of rpm packages
reposync                  download all packages from remote repo
uploadprofile             Upload combined profile to Satellite server (list of installed rpms, enabled repositories and modules

General DNF options:
  -c [config file], --config [config file]
                        config file location
  -q, --quiet           quiet operation
  -v, --verbose         verbose operation
  --version             show DNF version and exit
  --installroot [path]  set install root
  --nodocs              do not install documentations
  --noplugins           disable all plugins
  --enableplugin [plugin]
                        enable plugins by name
  --disableplugin [plugin]
                        disable plugins by name
  --releasever RELEASEVER
                        override the value of $releasever in config and repo
                        files
  --setopt SETOPTS      set arbitrary config and repo options
  --skip-broken         resolve depsolve problems by skipping packages
  -h, --help, --help-cmd
                        show command help
  --allowerasing        allow erasing of installed packages to resolve
                        dependencies
  -b, --best            try the best available package versions in
                        transactions.
  --nobest              do not limit the transaction to the best candidate
  -C, --cacheonly       run entirely from system cache, don't update cache
  -R [minutes], --randomwait [minutes]
                        maximum command wait time
  -d [debug level], --debuglevel [debug level]
                        debugging output level
  --debugsolver         dumps detailed solving results into files
  --showduplicates      show duplicates, in repos, in list/search commands
  -e ERRORLEVEL, --errorlevel ERRORLEVEL
                        error output level
  --obsoletes           enables dnf's obsoletes processing logic for upgrade
                        or display capabilities that the package obsoletes for
                        info, list and repoquery
  --rpmverbosity [debug level name]
                        debugging output level for rpm
  -y, --assumeyes       automatically answer yes for all questions
  --assumeno            automatically answer no for all questions
  --enablerepo [repo]   Enable additional repositories. List option. Supports
                        globs, can be specified multiple times.
  --disablerepo [repo]  Disable repositories. List option. Supports globs, can
                        be specified multiple times.
  --repo [repo], --repoid [repo]
                        enable just specific repositories by an id or a glob,
                        can be specified multiple times
  --enable              enable repos with config-manager command
                        (automatically saves)
  --disable             disable repos with config-manager command
                        (automatically saves)
  -x [package], --exclude [package], --excludepkgs [package]
                        exclude packages by name or glob
  --disableexcludes [repo], --disableexcludepkgs [repo]
                        disable excludepkgs
  --repofrompath [repo,path]
                        label and path to an additional repository to use
                        (same path as in a baseurl), can be specified multiple
                        times.
  --noautoremove        disable removal of dependencies that are no longer
                        used
  --nogpgcheck          disable gpg signature checking (if RPM policy allows)
  --color COLOR         control whether colour is used
  --refresh             set metadata as expired before running the command
  -4                    resolve to IPv4 addresses only
  -6                    resolve to IPv6 addresses only
  --destdir DESTDIR, --downloaddir DESTDIR
                        set directory to copy packages to
  --downloadonly        only download packages
  --comment COMMENT     add a comment to transaction
  --bugfix              Include bugfix relevant packages, in updates
  --enhancement         Include enhancement relevant packages, in updates
  --newpackage          Include newpackage relevant packages, in updates
  --security            Include security relevant packages, in updates
  --advisory ADVISORY, --advisories ADVISORY
                        Include packages needed to fix the given advisory, in
                        updates
  --bz BUGZILLA, --bzs BUGZILLA
                        Include packages needed to fix the given BZ, in
                        updates
  --cve CVES, --cves CVES
                        Include packages needed to fix the given CVE, in
                        updates
  --sec-severity {Critical,Important,Moderate,Low}, --secseverity {Critical,Important,Moderate,Low}
                        Include security relevant packages matching the
                        severity, in updates
  --forcearch ARCH      Force the use of an architecture

```

# snap

```
parallels@ubuntu-linux-2404:~$ snap help --all
The snap command lets you install, configure, refresh and remove snaps.
Snaps are packages that work across many different Linux distributions,
enabling secure delivery and operation of the latest apps and utilities.

Usage: snap <command> [<options>...]

Commands can be classified as follows:

  Basics (basic snap management):
    find             Find packages to install
    info             Show detailed information about snaps
    install          Install snaps on the system
    remove           Remove snaps from the system
    list             List installed snaps
    components       List available and installed components for installed snaps

  ...more (slightly more advanced snap management):
    refresh          Refresh snaps in the system
    revert           Reverts the given snap to the previous state
    switch           Switches snap to a different channel
    disable          Disable a snap in the system
    enable           Enable a snap in the system
    create-cohort    Create cohort keys for a set of snaps

  History (manage system change transactions):
    changes          List system changes
    tasks            List a change's tasks
    abort            Abort a pending change
    watch            Watch a change in progress

  Daemons (manage services):
    services         Query the status of services
    start            Start services
    stop             Stop services
    restart          Restart services
    logs             Retrieve logs for services

  Permissions (manage permissions):
    connections      List interface connections
    interface        Show details of snap interfaces
    connect          Connect a plug to a slot
    disconnect       Disconnect a plug from a slot

  Configuration (system administration and configuration):
    get              Print configuration options
    set              Change configuration options
    unset            Remove configuration options
    wait             Wait for configuration

  App Aliases (manage aliases):
    alias            Set up a manual alias
    aliases          List aliases in the system
    unalias          Remove a manual alias, or the aliases for an entire snap
    prefer           Enable aliases from a snap, disabling any conflicting aliases

  Account (authentication to snapd and the snap store):
    login            Authenticate to snapd and the store
    logout           Log out of snapd and the store
    whoami           Show the email the user is logged in with

  Snapshots (archives of snap data):
    saved            List currently stored snapshots
    save             Save a snapshot of the current data
    check-snapshot   Check a snapshot
    restore          Restore a snapshot
    forget           Delete a snapshot
    export-snapshot  Export a snapshot
    import-snapshot  Import a snapshot

  Device (manage device):
    model            Get the active model for this device
    remodel          Remodel this device
    reboot           Reboot into selected system and mode
    recovery         List available recovery systems

  Warnings (manage warnings):
    warnings         List warnings
    okay             Acknowledge warnings

  Assertions (manage assertions):
    known            Show known assertions of the provided type
    ack              Add an assertion to the system

  Introspection (introspection and debugging of snapd):
    version          Show version details
    debug            Run debug commands

  Development (developer-oriented features):
    download         Download the given snap
    pack             Pack the given directory as a snap
    run              Run the given snap command
    try              Test an unpacked snap in the system
    prepare-image    Prepare a device image

  Quota Groups (Manage quota groups for snaps):
    set-quota        Create or update a quota group.
    remove-quota     Remove quota group
    quotas           Show quota groups
    quota            Show quota group for a set of snaps

  Validation Sets (Manage validation sets):
    validate         List or apply validation sets

For more information about a command, run 'snap help <command>'.


```


# rpm

```
[al@macone-redhat9 ~]$ rpm --help
Usage: rpm [OPTION...]

Query/Verify package selection options:
  -a, --all                          query/verify all packages
  -f, --file                         query/verify package(s) owning installed
                                     file
      --path                         query/verify package(s) owning path,
                                     installed or not
  -g, --group                        query/verify package(s) in group
  -p, --package                      query/verify a package file
      --pkgid                        query/verify package(s) with package
                                     identifier
      --hdrid                        query/verify package(s) with header
                                     identifier
      --triggeredby                  query the package(s) triggered by the
                                     package
      --whatconflicts                query/verify the package(s) which require
                                     a dependency
      --whatrequires                 query/verify the package(s) which require
                                     a dependency
      --whatobsoletes                query/verify the package(s) which
                                     obsolete a dependency
      --whatprovides                 query/verify the package(s) which provide
                                     a dependency
      --whatrecommends               query/verify the package(s) which
                                     recommends a dependency
      --whatsuggests                 query/verify the package(s) which
                                     suggests a dependency
      --whatsupplements              query/verify the package(s) which
                                     supplements a dependency
      --whatenhances                 query/verify the package(s) which
                                     enhances a dependency
      --nomanifest                   do not process non-package files as
                                     manifests

Query/Verify file selection options:
  -c, --configfiles                  only include configuration files
  -d, --docfiles                     only include documentation files
  -L, --licensefiles                 only include license files
  -A, --artifactfiles                only include artifact files
      --noghost                      exclude %%ghost files
      --noconfig                     exclude %%config files
      --noartifact                   exclude %%artifact files

Query options (with -q or --query):
      --dump                         dump basic file information
  -l, --list                         list files in package
      --queryformat=QUERYFORMAT      use the following query format
  -s, --state                        display the states of the listed files

Verify options (with -V or --verify):
      --nofiledigest                 don't verify digest of files
      --nofiles                      don't verify files in package
      --nodeps                       don't verify package dependencies
      --noscript                     don't execute verify script(s)

Install/Upgrade/Erase options:
      --allfiles                     install all files, even configurations
                                     which might otherwise be skipped
      --allmatches                   remove all packages which match <package>
                                     (normally an error is generated if
                                     <package> specified multiple packages)
      --badreloc                     relocate files in non-relocatable package
  -e, --erase=<package>+             erase (uninstall) package
      --excludedocs                  do not install documentation
      --excludepath=<path>           skip files with leading component <path> 
      --force                        short hand for --replacepkgs
                                     --replacefiles
  -F, --freshen=<packagefile>+       upgrade package(s) if already installed
  -h, --hash                         print hash marks as package installs
                                     (good with -v)
      --ignorearch                   don't verify package architecture
      --ignoreos                     don't verify package operating system
      --ignoresize                   don't check disk space before installing
      --noverify                     short hand for --ignorepayload
                                     --ignoresignature
  -i, --install                      install package(s)
      --justdb                       update the database, but do not modify
                                     the filesystem
      --nodeps                       do not verify package dependencies
      --nofiledigest                 don't verify digest of files
      --nocontexts                   don't install file security contexts
      --nocaps                       don't install file capabilities
      --noorder                      do not reorder package installation to
                                     satisfy dependencies
      --noscripts                    do not execute package scriptlet(s)
      --notriggers                   do not execute any scriptlet(s) triggered
                                     by this package
      --oldpackage                   upgrade to an old version of the package
                                     (--force on upgrades does this
                                     automatically)
      --percent                      print percentages as package installs
      --prefix=<dir>                 relocate the package to <dir>, if
                                     relocatable
      --relocate=<old>=<new>         relocate files from path <old> to <new>
      --replacefiles                 ignore file conflicts between packages
      --replacepkgs                  reinstall if the package is already
                                     present
      --test                         don't install, but tell if it would work
                                     or not
  -U, --upgrade=<packagefile>+       upgrade package(s)
      --reinstall=<packagefile>+     reinstall package(s)

Common options for all rpm modes and executables:
  -D, --define='MACRO EXPR'          define MACRO with value EXPR
      --undefine=MACRO               undefine MACRO
  -E, --eval='EXPR'                  print macro expansion of EXPR
      --target=CPU-VENDOR-OS         Specify target platform
      --macros=<FILE:...>            read <FILE:...> instead of default file(s)
      --load=<FILE>                  load a single macro file
      --noplugins                    don't enable any plugins
      --nodigest                     don't verify package digest(s)
      --nosignature                  don't verify package signature(s)
      --rcfile=<FILE:...>            read <FILE:...> instead of default file(s)
  -r, --root=ROOT                    use ROOT as top level directory (default:
                                     "/")
      --dbpath=DIRECTORY             use database in DIRECTORY
      --querytags                    display known query tags
      --showrc                       display final rpmrc and macro
                                     configuration
      --quiet                        provide less detailed output
  -v, --verbose                      provide more detailed output
      --version                      print the version of rpm being used

Options implemented via popt alias/exec:
      --scripts                      list install/erase scriptlets from
                                     package(s)
      --setperms                     set permissions of files in a package
      --setugids                     set user/group ownership of files in a
                                     package
      --setcaps                      set capabilities of files in a package
      --restore                      restore file/directory permissions
      --conflicts                    list capabilities this package conflicts
                                     with
      --obsoletes                    list other packages removed by installing
                                     this package
      --provides                     list capabilities that this package
                                     provides
      --requires                     list capabilities required by package(s)
      --recommends                   list capabilities recommended by
                                     package(s)
      --suggests                     list capabilities suggested by package(s)
      --supplements                  list capabilities supplemented by
                                     package(s)
      --enhances                     list capabilities enhanced by package(s)
      --info                         list descriptive information from
                                     package(s)
      --changelog                    list change logs for this package
      --changes                      list changes for this package with full
                                     time stamps
      --xml                          list metadata in xml
      --triggers                     list trigger scriptlets from package(s)
      --filetriggers                 list filetrigger scriptlets from
                                     package(s)
      --last                         list package(s) by install time, most
                                     recent first
      --dupes                        list duplicated packages
      --filesbypkg                   list all files from each package
      --fileclass                    list file names with their classes
      --filecolor                    list file names with their colors
      --fileprovide                  list file names with their provides
      --filerequire                  list file names with requires
      --filecaps                     list file names with their POSIX1.e
                                     capabilities

Help options:
  -?, --help                         Show this help message
      --usage                        Display brief usage message
```

# dpkg

```
lab@lab:~$ dpkg --help
Usage: dpkg [<option>...] <command>

Commands:
  -i|--install       <.deb file name>... | -R|--recursive <directory>...
  --unpack           <.deb file name>... | -R|--recursive <directory>...
  -A|--record-avail  <.deb file name>... | -R|--recursive <directory>...
  --configure        <package>... | -a|--pending
  --triggers-only    <package>... | -a|--pending
  -r|--remove        <package>... | -a|--pending
  -P|--purge         <package>... | -a|--pending
  -V|--verify [<package>...]       Verify the integrity of package(s).
  --get-selections [<pattern>...]  Get list of selections to stdout.
  --set-selections                 Set package selections from stdin.
  --clear-selections               Deselect every non-essential package.
  --update-avail [<Packages-file>] Replace available packages info.
  --merge-avail [<Packages-file>]  Merge with info from file.
  --clear-avail                    Erase existing available info.
  --forget-old-unavail             Forget uninstalled unavailable pkgs.
  -s|--status [<package>...]       Display package status details.
  -p|--print-avail [<package>...]  Display available version details.
  -L|--listfiles <package>...      List files 'owned' by package(s).
  -l|--list [<pattern>...]         List packages concisely.
  -S|--search <pattern>...         Find package(s) owning file(s).
  -C|--audit [<package>...]        Check for broken package(s).
  --yet-to-unpack                  Print packages selected for installation.
  --predep-package                 Print pre-dependencies to unpack.
  --add-architecture <arch>        Add <arch> to the list of architectures.
  --remove-architecture <arch>     Remove <arch> from the list of architectures.
  --print-architecture             Print dpkg architecture.
  --print-foreign-architectures    Print allowed foreign architectures.
  --assert-help                    Show help on assertions.
  --assert-<feature>               Assert support for the specified feature.
  --validate-<thing> <string>      Validate a <thing>'s <string>.
  --compare-versions <a> <op> <b>  Compare version numbers - see below.
  --force-help                     Show help on forcing.
  -Dh|--debug=help                 Show help on debugging.

  -?, --help                       Show this help message.
      --version                    Show the version.

Validatable things: pkgname, archname, trigname, version.

Use dpkg with -b, --build, -c, --contents, -e, --control, -I, --info,
  -f, --field, -x, --extract, -X, --vextract, --ctrl-tarfile, --fsys-tarfile
on archives (type dpkg-deb --help).

Options:
  --admindir=<directory>     Use <directory> instead of /var/lib/dpkg.
  --root=<directory>         Install on a different root directory.
  --instdir=<directory>      Change installation dir without changing admin dir.
  --pre-invoke=<command>     Set a pre-invoke hook.
  --post-invoke=<command>    Set a post-invoke hook.
  --path-exclude=<pattern>   Do not install paths which match a shell pattern.
  --path-include=<pattern>   Re-include a pattern after a previous exclusion.
  -O|--selected-only         Skip packages not selected for install/upgrade.
  -E|--skip-same-version     Skip packages whose same version is installed.
  -G|--refuse-downgrade      Skip packages with earlier version than installed.
  -B|--auto-deconfigure      Install even if it would break some other package.
  --[no-]triggers            Skip or force consequential trigger processing.
  --verify-format=<format>   Verify output format (supported: 'rpm').
  --no-pager                 Disables the use of any pager.
  --no-debsig                Do not try to verify package signatures.
  --no-act|--dry-run|--simulate
                             Just say what we would do - don't do it.
  -D|--debug=<octal>         Enable debugging (see -Dhelp or --debug=help).
  --status-fd <n>            Send status change updates to file descriptor <n>.
  --status-logger=<command>  Send status change updates to <command>'s stdin.
  --log=<filename>           Log status changes and actions to <filename>.
  --ignore-depends=<package>[,...]
                             Ignore dependencies involving <package>.
  --force-<thing>[,...]      Override problems (see --force-help).
  --no-force-<thing>[,...]   Stop when problems encountered.
  --refuse-<thing>[,...]     Ditto.
  --abort-after <n>          Abort after encountering <n> errors.
  --robot                    Use machine-readable output on some commands.

Comparison operators for --compare-versions are:
  lt le eq ne ge gt       (treat empty version as earlier than any version);
  lt-nl le-nl ge-nl gt-nl (treat empty version as later than any version);
  < << <= = >= >> >       (only for compatibility with control file syntax).

Use 'apt' or 'aptitude' for user-friendly package management.
```

# zypper


# pacman

```

```

# rug

```

```
