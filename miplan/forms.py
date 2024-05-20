from django import forms
import psycopg2

class InsertForm(forms.Form):
    plan_date = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Plan Date (YYYY-MM-DD)")
    project = forms.CharField(max_length=100, required=True, help_text="Enter Project")
    group_level = forms.CharField(max_length=100, required=True, help_text="Enter Group Level")
    pn = forms.CharField(max_length=100, required=True, help_text="Enter PN")
    sum_in_qty = forms.IntegerField(required=False, help_text="Enter Sum In Quantity")
    d_plan_qty = forms.IntegerField(required=True, help_text="Enter D Plan Quantity")
    n_plan_qty = forms.IntegerField(required=True, help_text="Enter N Plan Quantity")
    plan_qty = forms.IntegerField(required=True, help_text="Enter Plan Quantity")
    actual_qty = forms.IntegerField(required=True, help_text="Enter Actual Quantity")
    finish_rate = forms.CharField(max_length=10, required=True, help_text="Enter Finish Rate (0.00 - 100.00)")
    plan_stock_qty = forms.IntegerField(required=True, help_text="Enter Plan Stock Quantity")
    factory = forms.CharField(max_length=100, required=False, help_text="Enter Factory")
    _status = forms.IntegerField(required=True, help_text="Enter Status")
    upload_midate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Upload Midate (YYYY-MM-DD)")
    remark1 = forms.CharField(max_length=100, required=True, help_text="Enter Remark 1")
    remark2 = forms.CharField(max_length=100, required=True, help_text="Enter Remark 2")
    remark3 = forms.CharField(max_length=100, required=False, help_text="Enter Remark 3")
    cdate = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Creation Date (YYYY-MM-DD)")
    cuser = forms.CharField(max_length=100, required=True, help_text="Enter Creation User")
    mdate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Modification Date (YYYY-MM-DD)")
    muser = forms.CharField(max_length=100, required=False, help_text="Enter Modification User")
    toplace = forms.CharField(max_length=100, required=False, help_text="Enter To Place")
    project_item = forms.CharField(max_length=100, required=False, help_text="Enter Project Item")
    sscode = forms.CharField(max_length=100, required=False, help_text="Enter SS Code")
    d_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter D Plan Time")
    n_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter N Plan Time")
    d_hour_plan_qty = forms.CharField(max_length=100, required=False, help_text="Enter D Hour Plan Quantity")
    n_hour_plan_qty = forms.CharField(max_length=100, required=False, help_text="Enter N Hour Plan Quantity")

    def clean(self):
        cleaned_data = super().clean()
        d_plan_qty = cleaned_data.get('d_plan_qty')
        n_plan_qty = cleaned_data.get('n_plan_qty')
        sum_in_qty = cleaned_data.get('sum_in_qty')
        plan_qty = cleaned_data.get('plan_qty')
        actual_qty = cleaned_data.get('actual_qty')
        
        day_plan = d_plan_qty + n_plan_qty
        if day_plan < sum_in_qty:
            self.add_error("Sum", "Day and night plan must be equal to SUMINQTY")
        
        if day_plan < plan_qty:
            self.add_error("Plan Quantity", "Day and night plan must be equal to Plan Quantity")

        if day_plan < actual_qty:
            self.add_error("Actual Quantity", "Day and night plan must be equal to Actual Quantity")
        
        return cleaned_data
class UpdateForm(forms.Form):
    
    id = forms.IntegerField(help_text="Enter Row ID number", required=True)
    plan_date = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Plan Date (YYYY-MM-DD)")
    project = forms.CharField(max_length=100, required=True, help_text="Enter Project")
    group_level = forms.CharField(max_length=100, required=True, help_text="Enter Group Level")
    pn = forms.CharField(max_length=100, required=True, help_text="Enter PN")
    sum_in_qty = forms.IntegerField(required=False, help_text="Enter Sum In Quantity")
    d_plan_qty = forms.IntegerField(required=True, help_text="Enter D Plan Quantity")
    n_plan_qty = forms.IntegerField(required=True, help_text="Enter N Plan Quantity")
    plan_qty = forms.IntegerField(required=True, help_text="Enter Plan Quantity")
    actual_qty = forms.IntegerField(required=True, help_text="Enter Actual Quantity")
    finish_rate = forms.CharField(max_length=10, required=True, help_text="Enter Finish Rate (0.00 - 100.00)")
    plan_stock_qty = forms.IntegerField(required=True, help_text="Enter Plan Stock Quantity")
    factory = forms.CharField(max_length=100, required=False, help_text="Enter Factory")
    _status = forms.IntegerField(required=True, help_text="Enter Status")
    upload_midate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Upload Midate (YYYY-MM-DD)")
    remark1 = forms.CharField(max_length=100, required=True, help_text="Enter Remark 1")
    remark2 = forms.CharField(max_length=100, required=True, help_text="Enter Remark 2")
    remark3 = forms.CharField(max_length=100, required=False, help_text="Enter Remark 3")
    cdate = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Creation Date (YYYY-MM-DD)")
    cuser = forms.CharField(max_length=100, required=True, help_text="Enter Creation User")
    mdate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Modification Date (YYYY-MM-DD)")
    muser = forms.CharField(max_length=100, required=False, help_text="Enter Modification User")
    toplace = forms.CharField(max_length=100, required=False, help_text="Enter To Place")
    project_item = forms.CharField(max_length=100, required=False, help_text="Enter Project Item")
    sscode = forms.CharField(max_length=100, required=False, help_text="Enter SS Code")
    d_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter D Plan Time")
    n_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter N Plan Time")
    d_hour_plan_qty = forms.CharField(max_length=100, required=False, help_text="Enter D Hour Plan Quantity")
    n_hour_plan_qty = forms.CharField(max_length=100, required=False, help_text="Enter N Hour Plan Quantity")

    def check_id(self):
        try:
            conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE id = %s", (id, ))
                result = cur.fetchone()
                conn.commit()
                conn.close()
                return result
        except psycopg2.Error as e:
            print("Error occured while inserting data:", e)
            
    def clean(self):
        cleaned_data =  super().clean() 
        id = self.cleaned_data.get("id")
        d_plan_qty = self.cleaned_data.get("d_plan_qty")
        n_plan_qty = self.cleaned_data.get("n_plan_qty")
        sum_in_qty = self.cleaned_data.get("sum_in_qty")
        plan_qty = self.cleaned_data.get("plan_qty")
        actual_qty = self.cleaned_data.get("actual_qty")
        
        id_check = self.check_id()
        if not id_check:
            self.add_error("ID", "ID Doesn't exist.")
        
        day_plan = d_plan_qty + n_plan_qty
        if day_plan < sum_in_qty:
            self.add_error("Sum", "Day and night plan must be equal to SUMINQTY")
        
        if day_plan < plan_qty:
            self.add_error("Plan Quantity", "Day and night plan must be equal to Plan Quantity")

        if day_plan < actual_qty:
            self.add_error("Actual Quantity", "Day and night plan must be equal to Actual Quantity")

        return cleaned_data