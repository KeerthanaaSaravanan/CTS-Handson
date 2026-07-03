from django.http import HttpResponse

def hello_view(request):
    """
    A simple view that returns a greeting message.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: A response with the message "Course Management API is running"
    """
    return HttpResponse("Course Management API is running")
