import requests
from difflib import get_close_matches

from .tools import load_json, get_openrouter_key
from .prompt_templates import build_prompt

def find_best_course(course_list, question):
    titles = [course["title"] for course in course_list]
    match = get_close_matches(question, titles, n=1, cutoff=0.3)
    if match:
        for course in course_list:
            if course["title"] == match[0]:
                return course
    return course_list[0]  # fallback to first course if no match

def query_agent(question, course_info):
    selected_course = find_best_course(course_info, question)
    prompt = build_prompt(selected_course, question)

    api_key = get_openrouter_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful academic assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
