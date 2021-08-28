# payroll-system
# NEW: Setting up your development environment using Docker (Windows 10 / Ubuntu 20 WLS2 ) !

This assumes you have your Windows 10 Professional, Ubuntu 20 WLS2 properly setup and
that docker is running in Ubuntu.

## To build your docker development environment:

Start your Ubuntu App as an Administrator
 
 
### You may now clone the project into your applications folder:

```
appplications$ git clone https://github.com/ploidddddd/payroll_system.git
```

### Build the docker using docker-compose, go to your project folder and execute

```
applications$ cd payroll_system
applications/payroll_system$ docker-compose up

```

### You can now open in your browser:

- the Web2py Admin

```
http://localhost:8380/
```

### In your project folder set your database connection parameters

- Create the required application config (appconfig.ini) from the template:

```
atwin# cp private/appconfig.ini.template appconfig.ini
atwin# sudo vim appconfig.ini
```

- Edit appconfig.ini file and set your database connection string (db_uri)

```
[db] 
; uri       = sqlite://storage.sqlite 
uri       = mysql://<username_here>:<password_here>@db1/openatdb 
migrate   = true 
fake_migrate = false
pool_size = 10  
```

### You may want to utilize an existing MySQL database (this is optional):

- Export your existing MySQL database (in Windows):

```
C:\Users\redenfloyd> mysqldump -uroot -p payrollsystemdb > payrollsystemdb_001.sql
```

This will create the file in current directory.

- Import the database to your MySQL docker (in Ubuntu):

```
$ docker exec -i open_at_db_1 sh -c 'exec mysql -uroot -p<root_password> payrollsystemdb' < /path/to/payrollsystemdb_001.sql
```

- NOTE: Inside Ubuntu, you can reference the Windows file system as:

* Drive C and D 
```
/mnt/c
/mnt/d
```

* Example C:\Users\redenfloyd>payrollsystemdb_001.sql maps to

```
/mnt/c/Users/nredenfloyd/atwindb_full.sql
```


### Start the applicattion
  
```
http://localhost:8380/payroll_system
```  

### Basic docker commands 

- To list your docker images

```
$ docker images
redenfloyd@darkmatter:~/ws/web2py/applications/ems$ docker images
REPOSITORY                        TAG                 IMAGE ID            CREATED             SIZE
python                            3.7.8-slim          378b5f00e004        6 days ago          156MB
mariadb                           latest              8075b7694a2d        12 days ago         407MB
nginx                             latest              0901fa9da894        3 weeks ago         132MB
ubuntu                            latest              adafef2e596e        4 weeks ago         73.9MB
node                              latest              37ad18cd8bd1        5 weeks ago         943MB
alpine                            latest              a24bb4013296        2 months ago        5.57MB
hello-world                       latest              bf756fb1ae65        7 months ago        13.3kB
jenkins                           latest              cd14cecfdb3a        2 years ago         696MB

```

- To list the running docker containers:

```
$ docker ps

CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                                            NAMES
278099612bef        rok/web2py:python3.7   "entrypoint.sh http"     4 hours ago         Up 4 hours          0.0.0.0:8380->8080/tcp, :::8380->8080/tcp        payroll_system_web_1
1360c7fb0702        mariadb                "docker-entrypoint.s…"   4 hours ago         Up 4 hours          3306/tcp                                         payroll_system_db_1
```

* atwin_web1_1 is the name for the Web2py container
* atwin_db1_1 is the name for the MySQL container

- Login to containers using the container names:

* For MySQL 

  ```
    $ docker exec -it payroll_system_db_1 /bin/bash
    root@bf8745a04eae:/# 
    root@bf8745a04eae:/# mysql -uroot -p
    Enter password: <root password>

    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 6
    Server version: 10.5.4-MariaDB-1:10.5.4+maria~focal mariadb.org binary distribution

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | payrollsystemdb    |
    | information_schema |
    | mysql              |
    | performance_schema |
    +--------------------+
    4 rows in set (0.007 sec)

    MariaDB [(none)]>  
    
  ```

* Type exit from your container to go back to Docker host (Ubuntu)

```
root@bf8745a04eae:/# exit  
payrollsystem$
```


- To stop all the containers started by `docker-compose up`:

* from shell

```
payrollsystem$ docker-compose down
```

* in running session, just press Ctrl-C twice
  
```
web1_1  | spawned uWSGI master process (pid: 1)
web1_1  | spawned uWSGI worker 1 (pid: 21, cores: 1)
web1_1  | spawned uWSGI http 1 (pid: 22)i
db1_1      | 2020-08-06  5:10:16 3 [Warning] Access denied for user 'root'@'localhost' (using password: YES)
db1_1      | 2020-08-06  6:10:16 5 [Warning] Access denied for user 'root'@'localhost' (using password: YES)
^CGracefully stopping... (press Ctrl+C again to force)
Stopping atwim_web1_1 ... done
Stopping atwin_db1_1     ... done
neiloswald@darkmatter:~/ws/web2py/applications/atwin$
```

- to stop a specific container:

```
$ docker stop payroll_system_web_1
```

- to view docker logs:

```
$ docker logs -f payroll_system_web_1
```

### Running VS Code from Ubuntu project

- Go to the project folder and enter command
  
  ```
  $ cd payroll_system_web_1
  $ payroll_system_web_1/code .
  ```
  

