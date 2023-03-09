# Customer Management Service

An application for managing customers and the items they purchase

## Getting Started

To get started with the Customer Management Service, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `make install`.
3. Create a PostgreSQL database and set the connection details in a configuration file (see below).
4. Run the app by running `python main.py`.

## Configuration

The Customer Management Service uses a configuration file to specify the connection details for the PostgreSQL database. The configuration file should be named `config.yml` and located in the root directory of the app. Here's an example configuration file:

## API Endpoints

The following API endpoints are available:

### Customers

- `GET /customers`: Returns a list of all customers.
- `GET /customers/{customer_id}`: Returns the details of a single customer.
- `POST /customers`: Creates a new customer.
- `PUT /customers/{customer_id}`: Updates the details of a customer.
- `DELETE /customers/{customer_id}`: Deletes a customer.

### Items

- `GET /items`: Returns a list of all items.
- `GET /items/{item_id}`: Returns the details of a single item.
- `POST /items`: Creates a new item.
- `PUT /items/{item_id}`: Updates the details of an item.
- `DELETE /items/{item_id}`: Deletes an item.

### Purchases

- `GET /purchases`: Returns a list of all purchases.
- `GET /purchases/{purchase_id}`: Returns the details of a single purchase.
- `POST /purchases`: Creates a new purchase.