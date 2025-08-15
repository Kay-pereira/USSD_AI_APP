# USSD_AI_APP



A Django-based USSD application that integrates **Africa's Talking** and **OpenAI API** to allow users to ask questions via USSD and receive AI-generated answers via SMS.

## 📌 Features
- USSD menu navigation
- AI-powered responses using OpenAI's API
- Automatic SMS replies via Africa's Talking
- Handles incoming SMS and delivery reports
- Secure API key management via `.env` and `python-decouple`

---

## 🛠 Tech Stack
- **Backend**: Django [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white)](https://github.com/YourUsername/YourRepo)
- **USSD & SMS Gateway**: Africa's Talking [![Africa’s Talking](https://img.shields.io/badge/Africa's_Talking-FFA500?logo=africas-talking&logoColor=white)](https://github.com/AfricasTalkingLtd)
- **AI**: OpenAI GPT models (GPT-3o Turbo) [![ChatGPT](https://img.shields.io/badge/ChatGPT-412991?logo=openai&logoColor=white)](https://openai.com/chatgpt)
- **Environment Management**: python-decouple [![Python Decouple](https://img.shields.io/badge/Python_Decouple-3776AB?logo=python&logoColor=white)](https://pypi.org/project/python-decouple/)

---

## 📂 Project Structure

.
├── ussd_ai_sms/ # Django project folder
├── manage.py
├── requirements.txt
└── .env # Environment variables (not committed)


---

## ⚙️ Installation

### 1 Clone the repository
```bash
git clone https://github.com/Kay-pereira/USSD_AI_APP.git
cd USSD_AI_APP
```

 2  python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3 pip install -r requirements.txt

🔑 **Environment Variables**
Create a .env file in the project root:

AFRIKAS_TALKING_USERNAME=your_africas_talking_username
AFRIKAS_TALKING_API_KEY=your_africas_talking_api_key
OPEN_AI_API_KEY=your_openai_api_key
OPEN_AI_URL=https://api.openai.com/v1/chat/completions

⚠️ Never commit .env to GitHub. Add it to .gitignore.

python manage.py runserver

 **Africa's Talking Setup**
Go to Africa's Talking Sandbox.

Create a USSD channel and set the callback URL:

http://<your-domain>/ussd/
Create an SMS channel and set the callback URL:


http://<your-domain>/sms/

USSD Flow
Dial your sandbox code.

Menu options:

1: Ask a question (response sent via SMS).

2: Exit.

📩 SMS Flow
Receives incoming SMS messages.

Sends acknowledgment replies.

Logs delivery reports for sent messages.

📜 License
This project is licensed under the MIT License.

👤 Author
Edmund Kwesi Pereira
GitHub Profile: https://github.org/Kay-pereira 

# USSD AI App ![GitHub Repo](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white) 
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)

A Django-based USSD application that integrates **Africa's Talking** and **OpenAI API** to allow users to ask questions via USSD and receive AI-generated answers via SMS even when offline. 🤯**AMAZING**





