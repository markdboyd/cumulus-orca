# Table of Contents

* [shared\_db](#shared_db)
  * [get\_configuration](#shared_db.get_configuration)
  * [get\_admin\_connection](#shared_db.get_admin_connection)
  * [get\_user\_connection](#shared_db.get_user_connection)

<a name="shared_db"></a>
# shared\_db

Name: shared_db.py

Description: Shared library for database objects needed by the various libraries.

<a name="shared_db.get_configuration"></a>
#### get\_configuration

```python
get_configuration() -> Dict[str, str]
```

Create a dictionary of configuration values based on environment variables
parameter store information and other items needed to create the database.


```
Environment Variables:
    PREFIX (str): Deployment prefix used to pull the proper AWS secret.
    AWS_REGION (str): AWS reserved runtime variable used to set boto3 client region.
    DATABASE_PORT (str): The database port. The standard is 5432
    DATABASE_NAME (str): The name of the application database.
    APPLICATION_USER (str): The name of the database application user.
    ADMIN_USER (str): *OPTIONAL* The name of the database super user (postgres).
    ADMIN_DATABASE (str): *OPTIONAL* The name of the admin database for the instance (postgres).

Parameter Store:
    <prefix>-drdb-user-pass (string): The password for the application user (APPLICATION_USER).
    <prefix>-drdb-host (string): The database host.
    <prefix>-drdb-admin-pass: The password for the admin user
```

**Arguments**:

  None
  

**Returns**:

- `Configuration` _Dict_ - Dictionary with all of the configuration information.
  The schema for the output is available [here](schemas/output.json).
  

**Raises**:

- `Exception` _Exception_ - When variables or secrets are not available.

<a name="shared_db.get_admin_connection"></a>
#### get\_admin\_connection

```python
get_admin_connection(config: Dict[str, str], database: str = None) -> Engine
```

Creates a connection engine to a database as a superuser.

**Arguments**:

- `config` _Dict_ - Configuration containing connection information.
- `database` _str_ - Database for the admin user to connect to. Defaults to admin_database.
  
  Returns
- `Engine` _sqlalchemy.future.Engine_ - engine object for creating database connections.

<a name="shared_db.get_user_connection"></a>
#### get\_user\_connection

```python
get_user_connection(config: Dict[str, str]) -> Engine
```

Creates a connection engine to the application database as the application
database user.

**Arguments**:

- `config` _Dict_ - Configuration containing connection information.
  
  Returns
- `Engine` _sqlalchemy.future.Engine_ - engine object for creating database connections.

