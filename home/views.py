from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>My First Django Website</title>
        </head>
        <body style="text-align:center; margin-top:100px;
                     font-family:Arial; background-color:lightblue;">

            <h1>Hello, World!</h1>
            <h2>Welcome to My First Django Website</h2>
            <p>This is a simple view created using Django.</p>

        </body>
        </html>
    """)