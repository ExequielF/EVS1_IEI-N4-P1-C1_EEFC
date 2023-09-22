from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1(request):
    html="""
    <h1>Aplicación N°1</h1>
    <p>Esto es un párrafo</p>
    <b>Esto está en negritas</b>
    <br>
    <ol>
        <li>Esto</li>
        <li>Es</li>
        <li>Una</li>
        <li>Lista</li>
    </ol>
    """
    return HttpResponse(html)