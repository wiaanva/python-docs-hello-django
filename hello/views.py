from django.http import HttpResponse ## HttpResponse uses HTML syntax.
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World!<br><br>This is a little attempt at preparing a home for my RymBot App service hosted on Azure.  \r\n\r\n See it as a sandbox where i am going to explore ways of satisfying my development ambitions:\n 1. To learn coding.\n 2. WatRymMet website.\n 3. Apex Legends data analytics.\n 4. Anything else I want to use Python for (Monitoring ETL pipelines, general blog of my journey (I would like to share my experiences with the world). Check back soon for more! \n ~ Wiaan, 2021/05/03")
