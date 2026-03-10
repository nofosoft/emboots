from datetime import datetime
import json
import math
import os
import re
from typing import Counter
from zoneinfo import ZoneInfo
import requests

from dotenv import load_dotenv

load_dotenv()   # membaca file .env

POST_DIR = "ui/public/posts"
os.makedirs(POST_DIR, exist_ok=True)

AI_TEMA = os.getenv("AI_TEMA")
AI_TOKEN_GEMINI = os.getenv("AI_TOKEN_GEMINI")
API_URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
HEADERS_GEMINI = {
    "Content-Type": f"application/json",
    "X-goog-api-key": f"{AI_TOKEN_GEMINI}"
}


def clean_ai_json(text):
    text = re.sub(r"```json|```", "", text)
    text = text.strip()
    return json.loads(text)


def get_ai_gemini_response(payload):
    try:
        response = requests.post(API_URL_GEMINI, headers=HEADERS_GEMINI,
                                 json=payload, timeout=30)

        data = response.json()

        if "candidates" not in data:
            print("API ERROR:", data)
            return None

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("PARSE ERROR:", e)
        return None


def ai_generate_article(related_topic):

    prompt = f"""
Anda adalah penulis artikel teknologi profesional.

Tugas Anda:
Tulis sebuah artikel blog berdasarkan topik {related_topic}.

Kriteria artikel:
- panjang maksimal 500 kata
- gunakan bahasa Indonesia
- gaya tulisan profesional dan informatif
- relevan dengan tren teknologi saat ini
- SEO friendly

Struktur artikel:
- gunakan heading markdown (#, ##, ###)
- gunakan paragraf yang jelas
- boleh menggunakan bullet list jika diperlukan

Output HARUS dalam format JSON valid dengan struktur berikut:
"title": "judul artikel","description": "ringkasan artikel 2-3 kalimat","content": "isi artikel dalam format markdown"

Aturan penting:
- Jangan menambahkan teks apa pun di luar JSON
- JSON harus valid
- content harus menggunakan format Markdown
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    res = get_ai_gemini_response(payload)

    print(res)

    data = clean_ai_json(res)

    file_path = "artikel.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("File berhasil disimpan:", file_path)


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)  # hapus karakter aneh
    text = re.sub(r'\s+', '-', text)      # ganti spasi dengan -
    return text


def estimate_reading_time(text, words_per_minute=200):
    words = len(text.split())
    minutes = math.ceil(words / words_per_minute)
    return minutes


def generate_keywords(text, top_n=10):

    # ubah ke lowercase
    text = text.lower()

    # ambil kata saja
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text)

    # stopwords sederhana
    stopwords = {
        "the", "and", "is", "in", "to", "of", "a", "for", "on", "with", "that",
        "ini", "dan", "yang", "di", "ke", "dari", "untuk", "dengan", "atau",
        "pada", "adalah", "sebagai", "oleh"
    }

    filtered = [w for w in words if w not in stopwords and len(w) > 3]

    counts = Counter(filtered)

    keywords = [word for word, _ in counts.most_common(top_n)]

    return keywords


def add_to_index(title, index_file="ui/public/posts/index.json"):

    # jika file belum ada
    if not os.path.exists(index_file):
        data = []
    else:
        with open(index_file, "r", encoding="utf-8") as f:
            data = json.load(f)

    # hindari duplikasi
    if title not in data:
        data.append(title)

    # simpan kembali
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Index diperbarui:", title)


def generate_article():

    reletated_topic = AI_TEMA

    # generate json file
    ai_generate_article(reletated_topic)

    # load json file
    with open("artikel.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # ambil data dari json
    ai_get_topic = data["title"]
    ai_get_description = data["description"]
    ai_content = data["content"]

    keywords = generate_keywords(ai_content)
    keywords_str = ", ".join(keywords)
    estimated_time_reading = estimate_reading_time(ai_content)

    add_to_index(slugify(ai_get_topic))

    date = datetime.now(ZoneInfo("Asia/Jakarta")).isoformat()
    filename = f"{POST_DIR}/{slugify(ai_get_topic)}.md"

    content = f"""---
title: "{ai_get_topic}"
category: "Artikel"
slug: "{slugify(ai_get_topic)}"
date: "{date}"
author: "Abdirrahman"
description: "{ai_get_description}"
readingTime: "{estimated_time_reading} min read"
keywords: "{keywords_str}"
---

{ai_content}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print("Artikel dibuat:", filename)
