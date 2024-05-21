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
    upload_midate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Upload Midate (YYYY-MM-DD)")
    cdate = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Creation Date (YYYY-MM-DD)")
    mdate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Modification Date (YYYY-MM-DD)")
    sscode = forms.CharField(max_length=100, required=True, help_text="Enter SS Code")
    d_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter D Plan Time")
    n_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter N Plan Time")

    def clean(self):
        super(InsertForm, self).clean() 
        d_plan_qty = self.cleaned_data.get("d_plan_qty")
        n_plan_qty = self.cleaned_data.get("n_plan_qty")
        sum_in_qty = self.cleaned_data.get("sum_in_qty")
        plan_qty = self.cleaned_data.get("plan_qty")
        actual_qty = self.cleaned_data.get("actual_qty")
        
        day_plan = d_plan_qty + n_plan_qty
        if day_plan != sum_in_qty:
             self._errors = self.error_class([
                'The whole day target must be equal to day plan + night plan'
            ])
        
        if day_plan != plan_qty:
             self._errors = self.error_class([
                'Day and night plan must be equal to Plan Quantity'
            ])

        if day_plan != actual_qty:
            self._errors = self.error_class([
                'Day and night plan must be equal to Actual Quantity'
            ])

        return self.cleaned_data
class UpdateForm(forms.Form):
    
    id = forms.IntegerField(help_text="Enter Row ID number", required=True,)
    plan_date = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Plan Date (YYYY-MM-DD)")
    project = forms.CharField(max_length=100, required=True, help_text="Enter Project")
    group_level = forms.CharField(max_length=100, required=True, help_text="Enter Group Level")
    pn = forms.CharField(max_length=100, required=True, help_text="Enter PN")
    sum_in_qty = forms.IntegerField(required=False, help_text="Enter Sum In Quantity")
    d_plan_qty = forms.IntegerField(required=True, help_text="Enter D Plan Quantity")
    n_plan_qty = forms.IntegerField(required=True, help_text="Enter N Plan Quantity")
    plan_qty = forms.IntegerField(required=True, help_text="Enter Plan Quantity")
    actual_qty = forms.IntegerField(required=True, help_text="Enter Actual Quantity")
    upload_midate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Upload Midate (YYYY-MM-DD)")
    cdate = forms.DateField(input_formats=['%Y-%m-%d'], required=True, help_text="Enter Creation Date (YYYY-MM-DD)")
    mdate = forms.DateField(input_formats=['%Y-%m-%d'], required=False, help_text="Enter Modification Date (YYYY-MM-DD)")
    sscode = forms.CharField(max_length=100, required=False, help_text="Enter SS Code")
    d_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter D Plan Time")
    n_plan_time = forms.CharField(max_length=100, required=False, help_text="Enter N Plan Time")

    def clean(self):
        super(UpdateForm, self).clean() 
        id = self.cleaned_data.get("id")
        d_plan_qty = self.cleaned_data.get("d_plan_qty")
        n_plan_qty = self.cleaned_data.get("n_plan_qty")
        sum_in_qty = self.cleaned_data.get("sum_in_qty")
        plan_qty = self.cleaned_data.get("plan_qty")
        actual_qty = self.cleaned_data.get("actual_qty")
        
        try:
            conn = psycopg2.connect("dbname=miplaninfodata user=postgres password=eslam010")
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM plan WHERE id = %s", (id, ))
                result = cur.fetchone()
                if not result:
                    self._errors = self.error_class([
                         "ID Doesn't exist."
                    ])
                conn.commit()
                conn.close()
        except psycopg2.Error as e:
             print("Error occured while inserting data:", e)
        
        day_plan = d_plan_qty + n_plan_qty
        if day_plan < sum_in_qty:
             self._errors = self.error_class([
                'The whole day target must be equal to day plan + night plan'
            ])
        
        if day_plan < plan_qty:
             self._errors = self.error_class([
                'Day and night plan must be equal to Plan Quantity'
            ])

        if day_plan < actual_qty:
            self._errors = self.error_class([
                'Day and night plan must be equal to Actual Quantity'
            ])

        return self.cleaned_data