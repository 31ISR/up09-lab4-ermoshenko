from django.shortcuts import render
def about(req):
    return render(req, "about.html")
def main(req):
    return render(req, "main.html")
def layout(req):
    return render(req, "layout.html")