# COUNTER1-SMS

#### Authors: [Ariso Okanga](https://github.com/Arisodee), [Carol Wambui](https://github.com/carol-wambui), [Peter Kungu](https://github.com/peterkush), [Kennedy Karuri](https://github.com/Kennedy-karuri), [Barnabas Kamau](https://github.com/Barnabas27), [Farzana Isack](https://github.com/farzana583), [Emmanuel Otieno](https://github.com/Emmanuel-otieno), [Ketsia Iragena](https://github.com/Ketsia-a)

## Description
COUNTER1-SMS offers simple SMS solutions by providing users with the ability to send messages to their contacts.

## Development set up
-   Check that python 3.x.x is installed:
    ```
    python --version
    >> Python 3.x.x
    ```
-   Install pipenv:
    ```
    pip3 install pipenv
    ```
-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2020.11.15
    ```
-   Check that postgres is installed:
    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```
-  Database
    * Swith to postgres account (in terminal)
        ```
        sudo su - postgres
        ```
    * Run PostgreSQL command line client.
        ```
        psql
        ```
    * Create a database user with a password.
        ```
        CREATE USER counter1_owner with password 'password1234';
        ```
    * Create a database instance.
        ```
        CREATE DATABASE counter1;
        ```  
    ```
- clone the repository and cd into it
    ```
    git clone https://github.com/Arisodee/COUNTER1-SMS.git
    ```

- Create  virtual environment
    ```
    pipenv --python 3.x
    ```
- Turn off a virtual environment  
    ```
    exit
    ```
- Spawn a shell in a virtual environment
    ```
    pipenv shell
    ```
- Install dependencies
    ```
   pipenv sync 
    ```
- Create Application environment variables and save them in .env file 
    ```
    DJANGO_READ_DOT_ENV_FILE=True
    DJANGO_DEBUG=True
    DB_NAME='counter1'
    DB_USER='<your database username>'
    DB_PASSWORD='<password to your database>'
    DB_HOST='127.0.0.1'
    SECRET_KEY='super_secret'
    ```
- Add the variables in the .env file to path
    ```
    source .env
    ```
- Running migrations
    - Initial migration commands
        ```
        python3 manage.py make migrations 
        python3 manage.py migrate
        ```
- Run application.
    ```
    python3.x manage.py runserver
    ```


### Merge Request Process
-   A contributor shall identify a task to be done
-   If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
-   The Contributor shall then create a branch off the `development` branch where they are expected to undertake their tasks
-   After undertaking the task, a fully detailed pull request shall be submitted to the owner of this repository for review.
-   If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `development` by the owner of this repository.
-   There should be only one commit per Merge Request, to achieve this use `git commit --amend`  

## Built with
- Python version  3
- Django 
- Postgres
- HTML, CSS and Bootstrap
- JavaScript