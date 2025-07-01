#%%
import google.generativeai as genai
import os

# Config API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-1.5-flash')

def get_bot_response(user_input):
    try:
        prompt = f"""
Tu es un assistant intelligent pour SINGERS, une entreprise spécialisée dans l'événementiel.
Elle a été fondée en 2015 par A et B, et organise des événements comme des concerts, des mariages, et des soirées privées.
Réponds de manière claire, professionnelle et concise à la question suivante :

Question : {user_input}
"""
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        print("Erreur Gemini :", e)  # ← ceci va afficher le vrai problème dans le terminal
        return "Je suis désolé, une erreur est survenue avec l'IA."
