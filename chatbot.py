#%%
import google.generativeai as genai
import os
from scrap import load_or_scrape_site


# Config API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-1.5-flash')

site_content = load_or_scrape_site()

def get_bot_response(user_input):
    try:
        prompt = f"""
Tu es un assistant web pour une entreprise dont voici les informations extraites de leur site web : {site_content}
Réponds de manière claire, professionnelle et concise à la question suivante :

Question : {user_input}
"""
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        print("Erreur Gemini :", e)  # ← ceci va afficher le vrai problème dans le terminal
        return "Je suis désolé, une erreur est survenue avec l'IA."

# %%
