# Advanced API Project

## Endpoints

### Book Endpoints

- `GET /books/` - List all books (public).
- `GET /books/<int:pk>/` - Retrieve a single book by ID (public).
- `POST /books/create/` - Create a new book (authenticated).
- `PUT /books/<int:pk>/update/` - Update an existing book (authenticated).
- `DELETE /books/<int:pk>/delete/` - Delete a book (authenticated).

## Permissions

- Public endpoints: `ListView`, `DetailView`.
- Restricted endpoints: `CreateView`, `UpdateView`, `DeleteView` (requires authentication).

## API Query Features

### Filtering

You can filter books by:

- `title`: Filter by book title.
- `author__name`: Filter by the author's name.
- `publication_year`: Filter by the year of publication.

**Example:**

```bash
GET /books/?author__name=George%20Orwell
```

## API Testing

### Purpose

The unit tests ensure:

- CRUD operations function as expected.
- Filtering, searching, and ordering features behave correctly.
- Authentication and permissions are enforced properly.

### How to Run Tests

1. Navigate to the project directory.
2. Run the following command:
   ```bash
   python manage.py test api
   ```
