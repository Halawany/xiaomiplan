from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import psycopg2

from .forms import InsertForm, UpdateForm

@login_required
def plan_home_view(request):
    try:
        conn = psycopg2.connect("dbname=miplaninfodata user=postgres password=eslam010")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM plan ORDER BY id;")
            data = cur.fetchall()
            context = {'all_data': data}
            return render(request, 'miplan/home.html', context)
    except psycopg2.Error as e:
        print("Error occurred while fetching data:", e)
        context = {'error_message': "Error occurred while fetching data"}
        return render(request, 'miplan/home.html', context)
            
    return render(request, 'miplan/home.html')

@login_required
def insert_plan_view(request):
    if request.method == "POST":
        form = InsertForm(request.POST)
        if form.is_valid():
            plan_date = form.cleaned_data["plan_date"]
            project = form.cleaned_data["project"]
            group_level = form.cleaned_data["group_level"]
            pn = form.cleaned_data["pn"]
            sum_in_qty = form.cleaned_data["sum_in_qty"]
            d_plan_qty = form.cleaned_data["d_plan_qty"]
            n_plan_qty = form.cleaned_data["n_plan_qty"]
            plan_qty = form.cleaned_data["plan_qty"]
            actual_qty = form.cleaned_data["actual_qty"]
            upload_midate = form.cleaned_data["upload_midate"]
            cdate = form.cleaned_data["cdate"]
            mdate = form.cleaned_data["mdate"]
            sscode = form.cleaned_data["sscode"]
            d_plan_time = form.cleaned_data["d_plan_time"]
            n_plan_time = form.cleaned_data["n_plan_time"]
            try:
                conn = psycopg2.connect("dbname=miplaninfodata user=postgres password=eslam010")
                with conn.cursor() as cur:
                    finish_rate = 100
                    plan_stock_qty = 0
                    factory = 'EAI'
                    _status = 0
                    remark1 = ' '
                    remark2 = ' '
                    remark3 = ' '
                    cuser = 'Eslam'
                    muser = 'Eslam'
                    toplace = ' '
                    project_item = ' '
                    d_hour_plan_qty =' '
                    n_hour_plan_qty = ' '
                    cur.execute("SELECT id FROM plan ORDER BY id DESC;")
                    last_id = cur.fetchone()[0] + 1
                    cur.execute("INSERT INTO plan(id, plandate, project, group_level, pn, suminqty, dplanqty, nplanqty, planqty, actualqty, finishrate, planstockqty, factory, _status, uploadmidate, remark1, remark2, remark3, cdate, cuser, mdate, muser, toplace, projectitem, sscode, dplantime, nplantime, dhourplanqty, nhourplanqty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                                (last_id, plan_date, project, group_level, pn, 
                                 sum_in_qty, d_plan_qty, n_plan_qty, plan_qty, actual_qty, finish_rate, plan_stock_qty, 
                                 factory, _status, upload_midate, remark1, remark2, remark3, cdate, cuser, 
                                 mdate, muser, toplace, project_item, sscode, d_plan_time, n_plan_time, 
                                 d_hour_plan_qty, n_hour_plan_qty))
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

@login_required
def update_plan_view(request):
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            plan_date = form.cleaned_data["plan_date"]
            project = form.cleaned_data["project"]
            group_level = form.cleaned_data["group_level"]
            pn = form.cleaned_data["pn"]
            sum_in_qty = form.cleaned_data["sum_in_qty"]
            d_plan_qty = form.cleaned_data["d_plan_qty"]
            n_plan_qty = form.cleaned_data["n_plan_qty"]
            plan_qty = form.cleaned_data["plan_qty"]
            actual_qty = form.cleaned_data["actual_qty"]
            upload_midate = form.cleaned_data["upload_midate"]
            cdate = form.cleaned_data["cdate"]
            mdate = form.cleaned_data["mdate"]
            sscode = form.cleaned_data["sscode"]
            d_plan_time = form.cleaned_data["d_plan_time"]
            n_plan_time = form.cleaned_data["n_plan_time"]
            
            try:
                conn = psycopg2.connect("dbname=miplaninfodata user=postgres password=eslam010")
                with conn.cursor() as cur:
                    finish_rate = 100
                    plan_stock_qty = 0
                    factory = 'EAI'
                    _status = 0
                    remark1 = ' '
                    remark2 = ' '
                    remark3 = ' '
                    cuser = 'Eslam'
                    muser = 'Eslam'
                    toplace = ' '
                    project_item = ' '
                    d_hour_plan_qty =' '
                    n_hour_plan_qty = ' '
                    cur.execute("UPDATE plan SET plandate = %s, project = %s, group_level = %s, pn = %s, suminqty = %s, dplanqty = %s, nplanqty = %s, planqty = %s, actualqty = %s, finishrate = %s, planstockqty = %s, factory = %s, _status = %s, uploadmidate = %s, remark1 = %s, remark2 = %s, remark3 = %s, cdate = %s, cuser = %s, mdate = %s, muser = %s, toplace = %s, projectitem = %s, sscode = %s, dplantime = %s, nplantime = %s, dhourplanqty = %s, nhourplanqty = %s WHERE id = %s", 
            (plan_date, project, group_level, pn, sum_in_qty, d_plan_qty, 
             n_plan_qty, plan_qty, actual_qty, finish_rate, plan_stock_qty, factory, _status, 
             upload_midate, remark1, remark2, remark3, cdate, cuser, mdate, muser, toplace, project_item, 
             sscode, d_plan_time, n_plan_time, d_hour_plan_qty, n_hour_plan_qty, id))
                    conn.commit()
                    conn.close()
                    return redirect('home')
            except psycopg2.Error as e:
                print("Error occured while inserting data:", e)
                context = {"error_message": e}
                return render(request, 'miplan/update.html', context)
    else:
        
        form = UpdateForm()
    return render(request, "miplan/update.html", {"form": form})