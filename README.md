# Customer Management Service

An application for managing purchases made by customers.

## Getting Started

This module depends on an available PostgreSQL Server and Kafka Broker.
To deploy them locally, reffer to https://github.com/Tavh/customer-platform

Once these conditions are met, follow these steps to run this application:


## Configuration

The Purchase Management Service uses a configuration file to specify the connection details for the PostgreSQL database and
the kafka bootstrap servers. The configuration file should be named `config.ini` and located in the root directory of the app. Here's an example configuration file:

```ini
[database]
url = postgresql://username:password@localhost:5432/customers

[kafka]
bootstrap_servers = localhost:9092
```

## API Endpoints

The following API endpoints are available:

- `GET /customers/{customer_id}/purchases`: Returns a list of purchases made by the customer.
