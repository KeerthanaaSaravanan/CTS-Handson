# DJANGO REQUEST–RESPONSE CYCLE
#
# Step-by-step explanation of a GET request to /api/courses/:
#
# 1. Browser sends GET request to the Django development server.
# 2. Django receives the request and passes it through the middleware stack.
# 3. Middleware processes the request (e.g., security, session handling).
# 4. URL Router (urls.py) matches the request path to a view function or class.
# 5. The view function/class receives the request object.
# 6. The view interacts with the Model to retrieve or manipulate data.
# 7. The Model performs an ORM/database query to fetch data from the database.
# 8. The database returns the requested data to the Model.
# 9. The Model returns the data to the View.
# 10. The View prepares an HTTP response (e.g., JSON, HTML) using the data.
# 11. Middleware processes the response (e.g., compression, security headers).
# 12. The response is returned to the browser.
#
# ASCII Flow Diagram:
#
# Browser
#     |
#     v
# Middleware (Request Processing)
#     |
#     v
# URL Router (urls.py)
#     |
#     v
# View (Function or Class)
#     |
#     v
# Model
#     |
#     v
# Database
#     |
#     v
# Model (Returns Data)
#     |
#     v
# View (Prepares Response)
#     |
#     v
# Middleware (Response Processing)
#     |
#     v
# Browser
#
#
# DJANGO MIDDLEWARE
#
# Middleware sits in the request-response cycle, acting as a layer between the
# web server and the view. It processes requests before they reach the view
# and processes responses after the view returns them.
#
# Middleware executes:
# - Before the request reaches the view (during request processing)
# - After the view returns a response (during response processing)
#
# Built-in Middleware Classes:
#
# a) django.middleware.security.SecurityMiddleware
#    - Adds security-related headers to HTTP responses (e.g., HSTS, XSS protection)
#    - Helps enforce HTTPS by redirecting HTTP requests to HTTPS
#    - Protects against common security issues like clickjacking and MIME sniffing
#
# b) django.contrib.sessions.middleware.SessionMiddleware
#    - Enables session management across requests
#    - Stores user session data in a server-side store (e.g., database, cache)
#    - Supports login persistence and user tracking by maintaining session state
#
#
# WSGI VS ASGI
#
# WSGI (Web Server Gateway Interface):
# - Traditional synchronous Python web standard
# - Suitable for standard web applications with request-response cycles
# - Processes requests synchronously (one request at a time per worker)
#
# ASGI (Asynchronous Server Gateway Interface):
# - Supports async/await for concurrent request handling
# - Supports WebSockets for real-time bidirectional communication
# - Supports long-lived connections (e.g., server-sent events)
# - Better for real-time applications and high-concurrency scenarios
#
# Comparison Table:
#
# Feature        | WSGI                    | ASGI
# ---------------|-------------------------|-------------------------
# Sync/Async     | Synchronous             | Asynchronous
# Concurrency    | Limited (per worker)    | High (async/await)
# WebSockets     | Not supported           | Supported
# Long-lived     | Not ideal               | Well-suited
# Use Case       | Traditional web apps    | Real-time apps, APIs
#
# Django uses WSGI by default for traditional deployments (via wsgi.py).
# Django also provides asgi.py for ASGI-compatible servers.
#
# Switch to ASGI when building:
#   * Chat systems
#   * WebSocket applications
#   * Live notifications
#   * Real-time dashboards
#   * High-concurrency async APIs
#
#
# MVC VS DJANGO MVT
#
# Traditional MVC Architecture:
# - Model = Data and database layer
# - View = User interface (what the user sees)
# - Controller = Request handling and business logic
#
# Django's MVT Architecture:
# - Model = Data layer (same as MVC)
# - View = Business logic and request handling (equivalent to Controller)
# - Template = Presentation layer (equivalent to View)
#
# Mapping Table:
#
# MVC                Django MVT
# --------------------------------
# Model       ->     Model
# View        ->     Template
# Controller  ->     View
#
# Clearly state:
#   "Django's View performs the role of the Controller in traditional MVC."
#

# DJANGO PROJECT VS DJANGO APP
# ----------------------------
# Django Project:
#   - A project is the entire application and its configuration
#   - Contains settings, URLs, WSGI/ASGI config, and other project-level configurations
#   - One project can contain multiple apps
#   - Example: 'coursemanager' is our Django project
#
# Django App:
#   - An app is a self-contained module designed to do one specific thing
#   - Contains models, views, templates, URLs, tests, etc. for a specific functionality
#   - Multiple apps can be combined to create a project
#   - Example: 'courses' is a Django app that handles course management functionality
#
# Key Difference:
#   A project is the entire website/application, while an app is a modular
#   component within that project that provides specific functionality.
