from django.shortcuts import render
from .gst_engine.pipeline import gst_chatbot_response

def chat_view(request):
    response = ""
    if request.method == "POST":
        user_query = request.POST.get("query", "")
        response = gst_chatbot_response(user_query)
    return render(request, "index.html", {"response": response})