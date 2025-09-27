# in chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
import json
from .gst_engine.pipeline import answer_query

def chat_view(request):
    """Renders the main chat page."""
    return render(request, 'chat.html')

def ask_bot(request):
    """API endpoint to get an answer from the chatbot."""
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')

        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)

        # Get the answer from your pipeline
        answer = answer_query(query)
        
        return JsonResponse({'answer': answer})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

        
            


    