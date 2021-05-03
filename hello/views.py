from django.http import HttpResponse ## HttpResponse uses HTML syntax.
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World!<br><br>This is a little attempt at preparing a home for my RymBot App service hosted on Azure.  <br><br> See it as a sandbox where i am going to explore ways of satisfying my development ambitions:<br> 1. To learn coding.<br> 2. WatRymMet website.<br> 3. Apex Legends data analytics.<br> 4. Anything else I want to use Python for (Monitoring ETL pipelines, general blog of my journey (I would like to share my experiences with the world). <br><br>Check back soon for more! <br><br> ~ Wiaan, 2021/05/03")
