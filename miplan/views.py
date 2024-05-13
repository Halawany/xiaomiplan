from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import psycopg2

from .forms import InsertForm

def plan_home_view(request):
    try:
        conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            data = cur.fetchall()
            context = {'all_data': data}
            return render(request, 'miplan/home.html', context)
    except psycopg2.Error as e:
        print("Error occurred while fetching data:", e)
        context = {'error_message': "Error occurred while fetching data"}
        return render(request, 'miplan/home.html', context)
            
    return render(request, 'miplan/home.html')


def insert_plan_view(request):
    form = InsertForm()
    return render(request, 'miplan/insert.html', {"form": form})
        