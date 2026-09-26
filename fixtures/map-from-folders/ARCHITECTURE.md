# Pantry architecture

## Entry points

- `pantry.api.app:create_app`, the web API.
- `pantry.cli:main`, the admin command line.

## Layers

Three clean layers: `api` calls `services`, `services` calls `db`. Nothing in `services`
imports from `api`, so the services can be reused by the command line unchanged.

## Components

- **API** (`src/api/`): HTTP routes.
- **Services** (`src/services/`): pricing and checkout.
- **Notifications** (`src/notifications/`): a separate service that sends order emails. It can
  be scaled and deployed on its own.
- **Payments** (`src/payments/`): legacy code from the old Stripe integration. Nothing uses it;
  it can be deleted in the rewrite.
- **DB** (`src/db/`): the data access layer. Each table has one owner.
