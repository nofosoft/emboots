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

AI_TOKEN = os.getenv("AI_TOKEN")
AI_TEMA = os.getenv("AI_TEMA")

POST_DIR = "ui/public/posts"
os.makedirs(POST_DIR, exist_ok=True)


API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {AI_TOKEN}"}


def get_ai_response(payload):
    try:
        response = requests.post(API_URL, headers=HEADERS,
                                 json=payload, timeout=30)

        data = response.json()

        if "choices" not in data:
            print("API ERROR:", data)
            return None

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("PARSE ERROR:", e)
        return None


def generate_ai_topic(related_topic):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": f"Berikan saya topik artikel yang unik berupa kalimat tentang {related_topic} yang relevan untuk tren teknologi hari ini. Topik harus berbeda dari topik sebelumnya minimal 6 kata. Respon dengan hanya satu kalimat."
            }
        ]
    }

    topic = get_ai_response(payload)
    print(topic)

    return topic


def generate_ai_topic_description(topic):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": f"Buatkan deskripsi tentang {topic} dengan panjang 50 kata"
            }
        ]
    }

    description = get_ai_response(payload)
    print(description)

    return description


def generate_ai_article(topic):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": f"Tulislah 500 kata artikel blog dengan topik {topic} dengan format markdown. \
                    fokus pada konten saja dan jangan tambahkan markdown yang tidak perlu. \
                        Gunakan bahasa teknis yang mudah. Hilangkan sub judul pendahuluan, pengantar atau sejenisnya akan tetapi langsung ke deskripsinya. \
                            Gunakan penomoran ## untuk sub judul dan # untuk judul utama.\
                                Sub judul terakhir adalah kesimpulan."
            }
        ]
    }

    msg = get_ai_response(payload)

    return msg


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

    ai_get_topic = generate_ai_topic(reletated_topic)
    ai_get_description = generate_ai_topic_description(ai_get_topic)
    ai_content = generate_ai_article(ai_get_topic)
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
