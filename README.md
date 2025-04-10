# 🍽️ Restaurant Table Reservation System - FastAPI

This project is a backend implementation of a simple table reservation system using **FastAPI** and **MySQL**. It allows users to reserve tables in a restaurant and includes **role-based access control** for admins and users.

---

## 🚀 Project Overview

The core of the project is built using FastAPI, which provides a fast and easy way to build APIs. The database interaction is managed using **SQLAlchemy**, and data validation is handled by **Pydantic models**. The authentication is done using **JWT tokens**, ensuring that only authenticated users can access the reservation system.

---

## 🧩 Key Components

- **Database**: MySQL is used for persistent data storage. SQLAlchemy models define the structure of data, including tables for users, tables, and bookings.
- **Authentication**: JWT-based authentication system. Admins can manage tables, while users can only view and reserve available tables.
- **Models**:
  - `User`: Contains username, hashed password, and role (`admin` or `user`).
  - `Table`: Represents tables in the restaurant with availability.
  - `Booking`: Stores user reservation info.
- **Testing**: Built using `pytest` and FastAPI’s `TestClient`. An in-memory test database is used during testing to ensure clean runs.

---

## 📘 API Routes

### 🔐 Authentication Routes:
- `POST /auth/signup` — Register a new user (admin/user).
- `POST /auth/login` — Login and receive a JWT token.

---

### 👤 User Routes (`/tables` prefix):
- `GET /tables/` — View all **available tables**.
- `POST /tables/{id}/reserve` — Reserve a specific table by ID.
- `DELETE /tables/{id}/cancel` — Cancel an existing reservation.
- `GET /tables/history` — View your booking/reservation history.

---

### 🛠️ Admin Routes (`/admin` prefix):
- `GET /admin/tables` — View **all tables** (available or reserved).
- `POST /admin/tables` — **Add** a new table.
- `PUT /admin/tables/{id}` — **Update** table details (e.g., number of seats).
- `DELETE /admin/tables/{id}` — **Delete** a table.
- `GET /admin/bookings` — View **all bookings** made by users.

---

## 🧭 Project Flow

1. On app startup, DB tables are created using SQLAlchemy’s `Base.metadata.create_all`.
2. Users can **register**, **login**, and obtain **JWT tokens**.
3. Authenticated users (with "user" role) can:
   - **View available tables**
   - **Reserve** or **cancel** reservations
   - **View booking history**
4. Admins can:
   - **Add/update/delete tables**
   - **View all bookings**
5. Testing uses an **isolated in-memory DB** for clean test runs.
