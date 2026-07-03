# Migration Guide

This guide explains how to manage database migrations for the Flask Course Manager application using Flask-Migrate.

## Initializing the Migration Repository

To set up Flask-Migrate for the first time, run:

```bash
flask db init
```

This command creates a `migrations` directory in your project. The `migrations` folder will store all your migration scripts.

## Creating a Migration

Whenever you make changes to your SQLAlchemy models (like adding a new table or modifying a column), you need to create a new migration script that captures these changes.

To generate a migration script, run:

```bash
flask db migrate -m "initial schema"
```

The `-m` flag allows you to provide a descriptive message for the migration. This command compares your current models to the previous migration (or the current database state if no migrations exist) and generates a new migration script in the `migrations/versions` folder.

## Applying Migrations to the Database

After generating a migration script, you apply it to the database using:

```bash
flask db upgrade
```

This command executes all pending migrations in order, updating your database schema to match your current models.

## Migration Workflow Summary

1. **Modify your models** in `flask_coursemanager/courses/models.py`.
2. **Generate a migration** with `flask db migrate -m "description of changes"`.
3. **Apply the migration** with `flask db upgrade`.

## Common Migration Issues

### 1. Forgetting to Generate a Migration
If you modify your models but forget to run `flask db migrate`, the changes won't be applied to the database, and you may encounter errors when the application tries to access columns or tables that don't exist.

**Solution:** Always run `flask db migrate` after changing your models.

### 2. Migration Script Conflicts
If two developers create migration scripts at the same time, you might end up with conflicting migration versions.

**Solution:** Communicate with your team and try to merge changes frequently. If conflicts occur, you may need to manually merge the migration scripts.

### 3. Database Already Has Tables
If you initialize Flask-Migrate on an existing database that already has tables, the first `flask db migrate` might try to create tables that already exist.

**Solution:** You can stamp the current database state as the initial migration:
```bash
flask db stamp head
```
This tells Flask-Migrate to consider the current database state as up-to-date with the latest migration.

### 4. Forgetting to Apply the Migration
Running `flask db migrate` only generates the script; it doesn't change the database. You must run `flask db upgrade` to apply the changes.

**Solution:** Always follow `flask db migrate` with `flask db upgrade`.

## Tips

- Always test migrations on a development or staging database before applying them to production.
- Keep your migration messages descriptive so you can understand what each migration does by reading the message.
- If you make a mistake in a migration, you can revert it by rolling back to the previous version:
  ```bash
  flask db downgrade
  ```
  Then fix the migration script and regenerate/reapply.