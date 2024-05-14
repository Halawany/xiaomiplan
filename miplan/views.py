from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import psycopg2

from .forms import InsertForm, UpdateForm

def plan_home_view(request):
    try:
        conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users ORDER BY id;")
            data = cur.fetchall()
            context = {'all_data': data}
            return render(request, 'miplan/home.html', context)
    except psycopg2.Error as e:
        print("Error occurred while fetching data:", e)
        context = {'error_message': "Error occurred while fetching data"}
        return render(request, 'miplan/home.html', context)
            
    return render(request, 'miplan/home.html')


def insert_plan_view(request):
    if request.method == "POST":
        form = InsertForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            try:
                conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
                with conn.cursor() as cur:
                    cur.execute("SELECT id FROM users ORDER BY id DESC;")
                    last_id = cur.fetchone()[0] + 1
                    cur.execute("INSERT INTO users (id, first_name, last_name) VALUES (%s, %s, %s);", (last_id, first_name, last_name))
                    conn.commit()
                    conn.close()
                    return redirect('home')
            except psycopg2.Error as e:
                print("Error occured while inserting data:", e)
                context = {"error_message": e}
                return render(request, 'miplan/insert.html', context)
            
    else:
        form = InsertForm()
    return render(request, 'miplan/insert.html', {"form": form})

def update_plan_view(request):
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            try:
                conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
                with conn.cursor() as cur:
                    cur.execute("UPDATE users SET first_name = %s, last_name = %s WHERE id = %s", (first_name, last_name, id))
                    conn.commit()
                    conn.close()
                    return redirect('home')
            except psycopg2.Error as e:
                print("Error occured while inserting data:", e)
                context = {"error_message": e}
                return render(request, 'miplan/update.html', context)
    else:
        form = InsertForm()
    return render(request, "miplan/update.html", {"form": form})