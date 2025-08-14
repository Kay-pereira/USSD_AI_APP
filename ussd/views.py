from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decouple import config
import africastalking
import requests

# Initialize Africa's Talking
africastalking.initialize(
    username=config("AFRIKAS_TALKING_USERNAME"),
    api_key=config("AFRIKAS_TALKING_API_KEY")
)
sms = africastalking.SMS


#  USSD FLOW
@csrf_exempt
def ussd_callback(request):
    """Handle USSD menu navigation"""
    if request.method == "POST":
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST.get("text", "")

        if text == "":
            response = "CON Welcome to Kwesi's AI USSD\n"
            response += "1. Ask a question\n"
            response += "2. Exit\n"

        elif text == "1":
            response = "CON Enter your question:"

        elif text.startswith("1*"):
            question = text.split("*", 1)[1]

            headers = {
                "Authorization": f"Bearer {settings.OPEN_AI_API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": question}],
                "max_tokens": 100
            }
            try:
                ai_res = requests.post(settings.OPEN_AI_URL, headers=headers, json=payload)
                ai_text = ai_res.json()["choices"][0]["message"]["content"]

                 # Send AI answer via SMS
                sms.send(f"AI Reply: {ai_text}", [phone_number])
                
                response = "END Your answer has been sent via SMS"

            except Exception as e:
             print("AI request failed", e)
             response = "Sorry there was a problem fetching you answer"

            # Save question and trigger SMS reply later
             send_ai_response(phone_number, question)
            response = "END Thanks! We'll send your answer via SMS."

        elif text == "2":
            response = "END Goodbye!"

        else:
            response = "END Invalid choice"

        return HttpResponse(response, content_type="text/plain")

    return HttpResponse("Invalid request", status=400)


# SMS FLOW
@csrf_exempt
def sms_callback(request):
    """Handle incoming SMS"""
    if request.method == "POST":
        phone_number = request.POST.get("from")
        text = request.POST.get("text")

        print(f"Incoming SMS from {phone_number}: {text}")
        send_sms(phone_number, "Thanks for your message!")
        return HttpResponse("ok")
    return HttpResponse("Invalid request", status=400)


# Helper to send SMS
def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        print("SMS Response:", response)
        return response
    except Exception as e:
        print("Error sending SMS:", e)
        return None


# Helper to call OpenAI and send response via SMS
def send_ai_response(phone_number, question):
    try:
        headers = {
            "Authorization": f"Bearer {settings.OPEN_AI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 100
        }
        ai_res = requests.post(settings.OPEN_AI_URL, headers=headers, json=payload)
        ai_text = ai_res.json()["choices"][0]["message"]["content"]

        send_sms(phone_number, f"AI Reply: {ai_text}")

    except Exception as e:
        print("Error getting AI response:", e)
