from django.shortcuts import render
from django.http import HttpResponse
from children.models import children

# Create your views here.

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

def view_one(request):
    # if GET request
    # display file input form
    # render_template(csv_import.html)

    # GET return HTML to load the page
    if request.method == "GET":
        child = children.objects.get(pk=1)
        return HttpResponse(f"{child.name} - {child.sex} - {child.age}")

    # POST take data from the user
    # and take necessary actions
    if request.method == "POST":
        form = request.form
        csv_file = form.file

        for row in DictReader(open('./children.csv')):
            child=children(name=row['Name'], sex=row['Sex'], age=row['Age'])
            child.save()

        # take data from form
        # child = children(name="aoeu")
        # child.save()
