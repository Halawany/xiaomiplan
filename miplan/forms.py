from django import forms
import psycopg2

class InsertForm(forms.Form):
    
    # id = forms.IntegerField(help_text="Enter Row ID number", required=True)
    first_name = forms.CharField(max_length=50, required=True, help_text="Enter First Name")
    last_name = forms.CharField(max_length=50, required=True, help_text="Enter Last Name")
    
    def clean(self):
        super(InsertForm, self).clean()
        
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        
        if len(first_name) < 5:
            self._errors = self.error_class([
                'First name must be > 5 letters'
            ])

        if len(last_name) < 5:
            self._errors = self.error_class([
                'Last name minimum letters must be 5'
            ])

        return self.cleaned_data
class UpdateForm(forms.Form):
    
    id = forms.IntegerField(help_text="Enter Row ID number", required=True)
    first_name = forms.CharField(max_length=50, required=True, help_text="Enter First Name")
    last_name = forms.CharField(max_length=50, required=True, help_text="Enter Last Name")
    
    def clean(self):
        super(UpdateForm, self).clean()
        id = self.cleaned_data.get("id")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        
        try:
            conn = psycopg2.connect("dbname=plan_test_db user=postgres password=eslam010")
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE id = %s", (id, ))
                result = cur.fetchone()
                if not result:
                    self._errors = self.error_class([
                        "ID Doesn't exist."
                    ])
                conn.commit()
                conn.close()
        except psycopg2.Error as e:
            print("Error occured while inserting data:", e)
            
        if len(first_name) < 5:
            self._errors = self.error_class([
                'First name must be > 5 letters'
            ])

        if len(last_name) < 5:
            self._errors = self.error_class([
                'Last name minimum letters must be 5'
            ])