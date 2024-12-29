# Order Management API

## Project Description
This project provides an API for managing orders in a system where users can be either admins or customers. Admins have access to all orders, while customers can only manage their own orders. The API includes endpoints for creating, retrieving, updating, and deleting orders by the product name.

## Features
- **User Authentication:** Token-based authentication for secure access.
- **Role-based Access Control:**
  - Admins can access all orders.
  - Customers can only access their own orders.
- **Order Management:**
  - Create orders.
  - Retrieve orders.
  - Update orders by product name.
  - Delete orders by product name.
- **Filtering:** Supports filtering orders using Django Filter Backend.

## Endpoints
### Authentication
Authentication is handled using Django's token-based system. Each request must include the user's token in the `Authorization` header:
```
Authorization: Token <your_token>
```

### Order Endpoints
1. **List All Orders**
   - **URL:** `GET /orders/`
   - **Access:**
     - Admin: All orders.
     - Customer: Only their own orders.

2. **Create an Order**
   - **URL:** `POST /orders/create/`
   - **Access:** Admin and Customer.
   - **Request Body:**
     ```json
     {
       "product_name": "<product_name>",
       "quantity": <quantity>,
       "total_price": <total_price>
     }
     ```

3. **Retrieve an Order by Product Name**
   - **URL:** `GET /orders/<product_name>/`
   - **Access:** Customer (only their orders).

4. **Update an Order by Product Name**
   - **URL:** `PUT /orders/<product_name>/update/`
   - **Access:** Customer (only their orders).
   - **Request Body:**
     ```json
     {
       "quantity": <quantity>,
       "total_price": <total_price>
     }
     ```

5. **Delete an Order by Product Name**
   - **URL:** `DELETE /orders/<product_name>/delete/`
   - **Access:** Customer (only their orders).

## Models
### CustomUser Model
- Extends Django's `AbstractUser`.
- Includes a `role` field to define the user role (admin or customer).

### Order Model
- Fields:
  - `product_name`: Unique identifier for the product.
  - `quantity`: Number of items in the order.
  - `total_price`: Total price of the order.
  - `created_at`: Timestamp of when the order was created.
  - `updated_at`: Timestamp of the last update.
  - `customer`: Foreign key to the `CustomUser` model.

## Permissions
### IsAdminOrCustomer
Custom permission class to allow access only to admins and customers.

### Authentication Classes
Token-based authentication using `TokenAuthentication`.

## Filters
### OrderFilter
Supports filtering orders based on customizable fields. Add filter fields in the `OrderFilter` class as needed.

## Testing
### Overview
The project includes a comprehensive test suite for both models and API endpoints. Tests ensure that all features work as expected under various conditions.

### Model Tests
#### `OrderModelTest`
- Verifies the `Order` model's creation and string representation.
- Example:
  - `test_order_creation`: Checks that the `Order` fields are correctly saved.
  - `test_order_string_representation`: Ensures the string representation follows the format `product_name - customer_username`.

### API Tests
#### `OrderListViewTest`
- Tests for listing and accessing orders.
- Examples:
  - `test_admin_can_view_all_orders`: Confirms that admins can view all orders in the database.
  - `test_customer_can_view_own_orders`: Ensures customers can only see their orders.
  - `test_unauthenticated_user_cannot_access_orders`: Validates that unauthenticated users receive a 401 Unauthorized response.

### Running Tests
1. Ensure the development environment is set up.
2. Run the test suite with:
   ```sh
   python manage.py test
   ```

## Docker Setup
### Dockerfile
The project includes a `Dockerfile` for containerized deployment.
```Dockerfile
FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
```

### Docker Compose
`docker-compose.yml` is provided for multi-service orchestration, including a PostgreSQL database.
```yaml
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: ./Dockerfile
    container_name: app-test
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app
    depends_on:
      - db
    networks:
      - test_network

  db:
    image: postgres:latest
    container_name: db-test
    environment:
      POSTGRES_USER: ${DEFAULT_USER}
      POSTGRES_PASSWORD: ${DEFAULT_PASSWORD}
      POSTGRES_DB: ${DEFAULT_NAME}
      POSTGRES_HOST_AUTH_METHOD: trust
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - test_network

volumes:
  postgres_data:

networks:
  test_network:
    driver: bridge
```

### Running with Docker
1. Build and start the services:
   ```sh
   docker-compose up --build
   ```
2. Access the application at `http://localhost:8000`.
3. Use the API endpoints to interact with the application.

## How to Run
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```sh
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Use tools like Postman or Curl to interact with the API.

## Notes
- Ensure to generate tokens for users using Django's built-in token authentication system.
- For production, configure environment-specific settings (e.g., database, secret keys).

