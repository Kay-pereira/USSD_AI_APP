from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question
import os
import requests
import threading
from django.conf import settings

AFRIKAS_TALKING_API_KEY = os.getenv("{settings.AFRIKAS_TALKING_API_KEY}")
AFRIKAS_TALKING_USERNAME = os.getenv("{settings.AFRIKAS_TALKING_USERNAME}")


OPEN_AI_API_KEY = os.getenv("{settings.OPEN_AI_API_KEY}")
OPEN_AI_URL = "{settings.OPEN_AI_URL}"

@csrf_exempt
def sms_callback(request):

    # Default response if nothing matches
    default_response = HttpResponse("END An error occurred", content_type="text/plain")

    try:
        if request.method == "POST":
            text = request.POST.get("text", "")
            phone_number = request.POST.get("phoneNumber", "")
            session_id = request.POST.get("sessionId", "")

            # Main USSD flow
            if text == "":
                response = "CON Welcome to Kwesi's AI USSD\n"
                response += "1. Please Ask a question\n"
                response += "2. Exit\n"
                "Please keep your question as short as possible, Thank you"
                return HttpResponse(response, content_type="text/plain")

            elif text == "1":
                response = "CON Enter your question:"
                return HttpResponse(response, content_type="text/plain")

            elif text.startswith("1*"):
                question = text.split("*", 1)[1]
                response = f"END Thanks, Your question was: {question}"
                return HttpResponse(response, content_type="text/plain")

            elif text == "2":
                return HttpResponse("END Goodbye!", content_type="text/plain")

            else:
                return HttpResponse("END Invalid choice", content_type="text/plain")

        else:
            return HttpResponse("END Invalid request method", content_type="text/plain")
    except Exception as e:
        print("Error in sms_callback:", e)
        return default_response
        
        # handle request.POST data from Africa's Talking here
    print(request.POST)  
    return HttpResponse("OK")
        
def send_ai_response(phone_number, question, question_id):

    #Fetch AI response and send it as SMS.
    
    try:
        # Calling open ai  API
        headers = {
            "Authorization": f"Bearer {settings.OPEN_AI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-",
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 100
        }
        ai_res = requests.post({settings.OPEN_AI_URL}, headers=headers, json=payload)
        ai_text = ai_res.json()["choices"][0]["message"]["content"]

        # Saving AI response in DB
        Question.objects.filter(id=question_id).update(ai_response=ai_text)

        # Send SMS via Africa's Talking
        sms_url = "https://api.africastalking.com/version1/messaging"
        sms_headers = {
            "apiKey": {settings.AFRIKAS_TALKING_API_KEY},
            "Content-Type": "application/x-www-form-urlencoded"
        }
        sms_payload = {
            "username": {settings.AFRIKAS_TALKING_USERNAME},
            "to": phone_number,
            "message": f"AI Reply: {ai_text}"
        }
        requests.post(sms_url, headers=sms_headers, data=sms_payload)
    except Exception as e:
        print("Error sending AI response:", e)

        
    

