from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2(request):
    html="""
    <h1>Aplicación N°2</h1>
    <p>Esto es otro párrafo</p>
    <b>Esto también está en negritas</b>
    <br>
    <ol>
        <li>Esto</li>
        <li>Es</li>
        <li>otra</li>
        <li>Lista</li>
        <li>más</li>
    </ol>
    """
    return HttpResponse(html)