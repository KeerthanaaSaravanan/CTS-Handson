# Background Tasks in FastAPI

## Introduction

FastAPI provides a `BackgroundTasks` class to run tasks in the background after returning a response. This is useful for operations that don't need to be completed before sending the response to the client, such as sending emails, processing files, or making external API calls.

## How It Works

1. Import `BackgroundTasks` from `fastapi`.
2. Add a parameter of type `BackgroundTasks` to your path operation function.
3. Use the `add_task` method to schedule a function to be run in the background.

## Example

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # Simulate sending an email
    print(f"Sending email to {email}: {message}")

@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Hello!")
    return {"message": "Notification will be sent in the background"}
```

## Key Points

- Background tasks are executed after the response has been sent.
- They run in the same process as the application.
- For long-running or CPU-intensive tasks, consider using a task queue like Celery.
- Background tasks are not suitable for tasks that require guaranteed execution (use a task queue for that).
- Each background task runs in a separate thread, but they are still limited by the GIL for CPU-bound tasks.

## In This Project

In the enrollment endpoint (`POST /api/enrollments/`), we use a background task to send a confirmation email to the student after creating the enrollment. This allows the API to return a response immediately without waiting for the email to be sent.

The background task function `send_confirmation_email` is defined in `main.py` and simply prints a message to the console. In a real application, this would be replaced with actual email sending logic using a library like `smtplib` or a service like SendGrid.