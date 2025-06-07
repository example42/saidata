# systemd

```
parallels@ubuntu-linux-2404:~$ systemctl -h
systemctl [OPTIONS...] COMMAND ...

Query or send control commands to the system manager.

Unit Commands:
  list-units [PATTERN...]             List units currently in memory
  list-automounts [PATTERN...]        List automount units currently in memory,
                                      ordered by path
  list-paths [PATTERN...]             List path units currently in memory,
                                      ordered by path
  list-sockets [PATTERN...]           List socket units currently in memory,
                                      ordered by address
  list-timers [PATTERN...]            List timer units currently in memory,
                                      ordered by next elapse
  is-active PATTERN...                Check whether units are active
  is-failed [PATTERN...]              Check whether units are failed or
                                      system is in degraded state
  status [PATTERN...|PID...]          Show runtime status of one or more units
  show [PATTERN...|JOB...]            Show properties of one or more
                                      units/jobs or the manager
  cat PATTERN...                      Show files and drop-ins of specified units
  help PATTERN...|PID...              Show manual for one or more units
  list-dependencies [UNIT...]         Recursively show units which are required
                                      or wanted by the units or by which those
                                      units are required or wanted
  start UNIT...                       Start (activate) one or more units
  stop UNIT...                        Stop (deactivate) one or more units
  reload UNIT...                      Reload one or more units
  restart UNIT...                     Start or restart one or more units
  try-restart UNIT...                 Restart one or more units if active
  reload-or-restart UNIT...           Reload one or more units if possible,
                                      otherwise start or restart
  try-reload-or-restart UNIT...       If active, reload one or more units,
                                      if supported, otherwise restart
  isolate UNIT                        Start one unit and stop all others
  kill UNIT...                        Send signal to processes of a unit
  clean UNIT...                       Clean runtime, cache, state, logs or
                                      configuration of unit
  freeze PATTERN...                   Freeze execution of unit processes
  thaw PATTERN...                     Resume execution of a frozen unit
  set-property UNIT PROPERTY=VALUE... Sets one or more properties of a unit
  bind UNIT PATH [PATH]               Bind-mount a path from the host into a
                                      unit's namespace
  mount-image UNIT PATH [PATH [OPTS]] Mount an image from the host into a
                                      unit's namespace
  service-log-level SERVICE [LEVEL]   Get/set logging threshold for service
  service-log-target SERVICE [TARGET] Get/set logging target for service
  reset-failed [PATTERN...]           Reset failed state for all, one, or more
                                      units
  whoami [PID...]                     Return unit caller or specified PIDs are
                                      part of

Unit File Commands:
  list-unit-files [PATTERN...]        List installed unit files
  enable [UNIT...|PATH...]            Enable one or more unit files
  disable UNIT...                     Disable one or more unit files
  reenable UNIT...                    Reenable one or more unit files
  preset UNIT...                      Enable/disable one or more unit files
                                      based on preset configuration
  preset-all                          Enable/disable all unit files based on
                                      preset configuration
  is-enabled UNIT...                  Check whether unit files are enabled
  mask UNIT...                        Mask one or more units
  unmask UNIT...                      Unmask one or more units
  link PATH...                        Link one or more units files into
                                      the search path
  revert UNIT...                      Revert one or more unit files to vendor
                                      version
  add-wants TARGET UNIT...            Add 'Wants' dependency for the target
                                      on specified one or more units
  add-requires TARGET UNIT...         Add 'Requires' dependency for the target
                                      on specified one or more units
  edit UNIT...                        Edit one or more unit files
  get-default                         Get the name of the default target
  set-default TARGET                  Set the default target

Machine Commands:
  list-machines [PATTERN...]          List local containers and host

Job Commands:
  list-jobs [PATTERN...]              List jobs
  cancel [JOB...]                     Cancel all, one, or more jobs

Environment Commands:
  show-environment                    Dump environment
  set-environment VARIABLE=VALUE...   Set one or more environment variables
  unset-environment VARIABLE...       Unset one or more environment variables
  import-environment VARIABLE...      Import all or some environment variables

Manager State Commands:
  daemon-reload                       Reload systemd manager configuration
  daemon-reexec                       Reexecute systemd manager
  log-level [LEVEL]                   Get/set logging threshold for manager
  log-target [TARGET]                 Get/set logging target for manager
  service-watchdogs [BOOL]            Get/set service watchdog state

System Commands:
  is-system-running                   Check whether system is fully running
  default                             Enter system default mode
  rescue                              Enter system rescue mode
  emergency                           Enter system emergency mode
  halt                                Shut down and halt the system
  poweroff                            Shut down and power-off the system
  reboot                              Shut down and reboot the system
  kexec                               Shut down and reboot the system with kexec
  soft-reboot                         Shut down and reboot userspace
  exit [EXIT_CODE]                    Request user instance or container exit
  switch-root [ROOT [INIT]]           Change to a different root file system
  suspend                             Suspend the system
  hibernate                           Hibernate the system
  hybrid-sleep                        Hibernate and suspend the system
  suspend-then-hibernate              Suspend the system, wake after a period of
                                      time, and hibernate
Options:
  -h --help              Show this help
     --version           Show package version
     --system            Connect to system manager
     --user              Connect to user service manager
  -H --host=[USER@]HOST  Operate on remote host
  -M --machine=CONTAINER Operate on a local container
  -t --type=TYPE         List units of a particular type
     --state=STATE       List units with particular LOAD or SUB or ACTIVE state
     --failed            Shortcut for --state=failed
  -p --property=NAME     Show only properties by this name
  -P NAME                Equivalent to --value --property=NAME
  -a --all               Show all properties/all units currently in memory,
                         including dead/empty ones. To list all units installed
                         on the system, use 'list-unit-files' instead.
  -l --full              Don't ellipsize unit names on output
  -r --recursive         Show unit list of host and local containers
     --reverse           Show reverse dependencies with 'list-dependencies'
     --with-dependencies Show unit dependencies with 'status', 'cat',
                         'list-units', and 'list-unit-files'.
     --job-mode=MODE     Specify how to deal with already queued jobs, when
                         queueing a new job
  -T --show-transaction  When enqueuing a unit job, show full transaction
     --show-types        When showing sockets, explicitly show their type
     --value             When showing properties, only print the value
     --check-inhibitors=MODE
                         Whether to check inhibitors before shutting down,
                         sleeping, or hibernating
  -i                     Shortcut for --check-inhibitors=no
     --kill-whom=WHOM    Whom to send signal to
     --kill-value=INT    Signal value to enqueue
  -s --signal=SIGNAL     Which signal to send
     --what=RESOURCES    Which types of resources to remove
     --now               Start or stop unit after enabling or disabling it
     --dry-run           Only print what would be done
                         Currently supported by verbs: halt, poweroff, reboot,
                             kexec, soft-reboot, suspend, hibernate, 
                             suspend-then-hibernate, hybrid-sleep, default,
                             rescue, emergency, and exit.
  -q --quiet             Suppress output
     --no-warn           Suppress several warnings shown by default
     --wait              For (re)start, wait until service stopped again
                         For is-system-running, wait until startup is completed
     --no-block          Do not wait until operation finished
     --no-wall           Don't send wall message before halt/power-off/reboot
     --no-reload         Don't reload daemon after en-/dis-abling unit files
     --legend=BOOL       Enable/disable the legend (column headers and hints)
     --no-pager          Do not pipe output into a pager
     --no-ask-password   Do not ask for system passwords
     --global            Edit/enable/disable/mask default user unit files
                         globally
     --runtime           Edit/enable/disable/mask unit files temporarily until
                         next reboot
  -f --force             When enabling unit files, override existing symlinks
                         When shutting down, execute action immediately
     --preset-mode=      Apply only enable, only disable, or all presets
     --root=PATH         Edit/enable/disable/mask unit files in the specified
                         root directory
     --image=PATH        Edit/enable/disable/mask unit files in the specified
                         disk image
     --image-policy=POLICY
                         Specify disk image dissection policy
  -n --lines=INTEGER     Number of journal entries to show
  -o --output=STRING     Change journal output mode (short, short-precise,
                             short-iso, short-iso-precise, short-full,
                             short-monotonic, short-unix, short-delta,
                             verbose, export, json, json-pretty, json-sse, cat)
     --firmware-setup    Tell the firmware to show the setup menu on next boot
     --boot-loader-menu=TIME
                         Boot into boot loader menu on next boot
     --boot-loader-entry=NAME
                         Boot into a specific boot loader entry on next boot
     --plain             Print unit dependencies as a list instead of a tree
     --timestamp=FORMAT  Change format of printed timestamps (pretty, unix,
                             us, utc, us+utc)
     --read-only         Create read-only bind mount
     --mkdir             Create directory before mounting, if missing
     --marked            Restart/reload previously marked units
     --drop-in=NAME      Edit unit files using the specified drop-in file name
     --when=TIME         Schedule halt/power-off/reboot/kexec action after
                         a certain timestamp

See the systemctl(1) man page for details.

```

# launchd

```
MacBookPro:~ al$ launchctl 
Usage: launchctl <subcommand> ... | help [subcommand]
Many subcommands take a target specifier that refers to a domain or service
within that domain. The available specifier forms are:

system/[service-name]
Targets the system-wide domain or service within. Root privileges are required
to make modifications.

user/<uid>/[service-name]
Targets the user domain or service within. A process running as the target user
may make modifications. Root may modify any user's domain. User domains do not
exist on iOS.

gui/<uid>/[service-name]
Targets the GUI domain or service within. Each GUI domain is associated with a
user domain, and a process running as the owner of that user domain may make
modifications. Root may modify any GUI domain. GUI domains do not exist on iOS.

session/<asid>/[service-name]
Targets a session domain or service within. A process running within the target
security audit session may make modifications. Root may modify any session
domain.

pid/<pid>/[service-name]
Targets a process domain or service within. Only the process which owns the
domain may modify it. Even root may not do so.

When using a legacy subcommand which manipulates a domain, the target domain is
inferred from the current execution context. When run as root (whether it is
via a root shell or sudo(1)), the target domain is assumed to be the
system-wide domain. When run from a normal user's shell, the target is assumed
to be the per-user domain for that current user.

Subcommands:
	bootstrap       Bootstraps a domain or a service into a domain.
	bootout         Tears down a domain or removes a service from a domain.
	enable          Enables an existing service.
	disable         Disables an existing service.
	kickstart       Forces an existing service to start.
	attach          Attach the system's debugger to a service.
	debug           Configures the next invocation of a service for debugging.
	kill            Sends a signal to the service instance.
	blame           Prints the reason a service is running.
	print           Prints a description of a domain or service.
	print-cache     Prints information about the service cache.
	print-disabled  Prints which services are disabled.
	print-token     Prints service identifier given an xpc event token.
	plist           Prints a property list embedded in a binary (targets the Info.plist by default).
	procinfo        Prints port information about a process.
	hostinfo        Prints port information about the host.
	resolveport     Resolves a port name from a process to an endpoint in launchd.
	limit           Reads or modifies launchd's resource limits.
	examine         Runs the specified analysis tool against launchd in a non-reentrant manner.
	config          Modifies persistent configuration parameters for launchd domains.
	dumpstate       Dumps launchd state to stdout.
	dumpjpcategory  Dumps the jetsam properties category for all services.
	reboot          Initiates a system reboot of the specified type.
	bootshell       Brings the system up from single-user mode with a console shell.
	load            Recommended alternatives: bootstrap | enable. Bootstraps a service or directory of services.
	unload          Recommended alternatives: bootout | disable. Unloads a service or directory of services.
	remove          Unloads the specified service name.
	list            Lists information about services.
	start           Starts the specified service.
	stop            Stops the specified service if it is running.
	setenv          Sets the specified environment variables for all services within the domain.
	unsetenv        Unsets the specified environment variables for all services within the domain.
	getenv          Gets the value of an environment variable from within launchd.
	bsexec          Execute a program in another process' bootstrap context.
	asuser          Execute a program in the bootstrap context of a given user.
	submit          Submit a basic job from the command line.
	managerpid      Prints the PID of the launchd controlling the session.
	manageruid      Prints the UID of the current launchd session.
	managername     Prints the name of the current launchd session.
	error           Prints a description of an error.
	variant         Prints the launchd variant.
	version         Prints the launchd version.
	help            Prints the usage for a given subcommand.
```

# windows SCm Service Control Manager

```
PS C:\Users\al> sc.exe
DESCRIPTION:
        SC is a command line program used for communicating with the
        Service Control Manager and services.
USAGE:
        sc <server> [command] [service name] <option1> <option2>...


        The option <server> has the form "\\ServerName"
        Further help on commands can be obtained by typing: "sc [command]"
        Commands:
          query-----------Queries the status for a service, or
                          enumerates the status for types of services.
          queryex---------Queries the extended status for a service, or
                          enumerates the status for types of services.
          start-----------Starts a service.
          pause-----------Sends a PAUSE control request to a service.
          interrogate-----Sends an INTERROGATE control request to a service.
          continue--------Sends a CONTINUE control request to a service.
          stop------------Sends a STOP request to a service.
          config----------Changes the configuration of a service (persistent).
          description-----Changes the description of a service.
          failure---------Changes the actions taken by a service upon failure.
          failureflag-----Changes the failure actions flag of a service.
          sidtype---------Changes the service SID type of a service.
          privs-----------Changes the required privileges of a service.
          managedaccount--Changes the service to mark the service account
                          password as managed by LSA.
          qc--------------Queries the configuration information for a service.
          qdescription----Queries the description for a service.
          qfailure--------Queries the actions taken by a service upon failure.
          qfailureflag----Queries the failure actions flag of a service.
          qsidtype--------Queries the service SID type of a service.
          qprivs----------Queries the required privileges of a service.
          qtriggerinfo----Queries the trigger parameters of a service.
          qpreferrednode--Queries the preferred NUMA node of a service.
          qmanagedaccount-Queries whether a services uses an account with a
                          password managed by LSA.
          qprotection-----Queries the process protection level of a service.
          quserservice----Queries for a local instance of a user service template.
          delete----------Deletes a service (from the registry).
          create----------Creates a service. (adds it to the registry).
          control---------Sends a control to a service.
          sdshow----------Displays a service's security descriptor.
          sdset-----------Sets a service's security descriptor.
          showsid---------Displays the service SID string corresponding to an arbitrary name.
          triggerinfo-----Configures the trigger parameters of a service.
          preferrednode---Sets the preferred NUMA node of a service.
          GetDisplayName--Gets the DisplayName for a service.
          GetKeyName------Gets the ServiceKeyName for a service.
          EnumDepend------Enumerates Service Dependencies.

        The following commands don't require a service name:
        sc <server> <command> <option>
          boot------------(ok | bad) Indicates whether the last boot should
                          be saved as the last-known-good boot configuration
          Lock------------Locks the Service Database
          QueryLock-------Queries the LockStatus for the SCManager Database
EXAMPLE:
        sc start MyService


QUERY and QUERYEX OPTIONS:
        If the query command is followed by a service name, the status
        for that service is returned.  Further options do not apply in
        this case.  If the query command is followed by nothing or one of
        the options listed below, the services are enumerated.
    type=    Type of services to enumerate (driver, service, userservice, all)
             (default = service)
    state=   State of services to enumerate (inactive, all)
             (default = active)
    bufsize= The size (in bytes) of the enumeration buffer
             (default = 4096)
    ri=      The resume index number at which to begin the enumeration
             (default = 0)
    group=   Service group to enumerate
             (default = all groups)

SYNTAX EXAMPLES
sc query                - Enumerates status for active services & drivers
sc query eventlog       - Displays status for the eventlog service
sc queryex eventlog     - Displays extended status for the eventlog service
sc query type= driver   - Enumerates only active drivers
sc query type= service  - Enumerates only Win32 services
sc query state= all     - Enumerates all services & drivers
sc query bufsize= 50    - Enumerates with a 50 byte buffer
sc query ri= 14         - Enumerates with resume index = 14
sc queryex group= ""    - Enumerates active services not in a group
sc query type= interact - Enumerates all interactive services
sc query type= driver group= NDIS     - Enumerates all NDIS drivers
```