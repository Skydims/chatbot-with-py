import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"nama saya (.*)",
        ["Halo %1, apa kabar hari ini?",]
    ],
    [
        r"halo|hai|selamat|hi|hii (pagi|siang|malam)",
        ["Halo!", "Hai, apa kabar?",]
    ],
    [
        r"siapa nama kamu?",
        ["Saya adalah chatbot yang dibuat oleh Anda.",]
    ],
    [
        r"apa kabar?",
        ["Saya baik-baik saja. Bagaimana dengan Anda?",]
    ],
    [
        r"maaf (.*)",
        ["Tidak apa-apa", "Tidak masalah",]
    ],
    [
        r"saya (.*) (baik|sehat|ok|oke)",
        ["Senang mendengarnya!", "Baik, hebat!",]
    ],
    [
        r"berapa umurmu?",
        ["Saya program komputer, jadi saya tidak punya umur kocak.",]
    ],
    [
        r"keluar",
        ["Sampai jumpa, jaga diri baik-baik. Sampai ketemu lagi :) ", "Senang berbicara dengan Anda. Selamat tinggal!"]
    ],
    [
        r"apa yang bisa kamu lakukan?",
        ["Saya bisa membantu Anda dengan percakapan sederhana dalam bahasa Indonesia.",]
    ],
    [
        r"ceritakan lelucon",
        ["Kenapa ayam menyeberang jalan? Untuk menuju sisi yang lain!",]
    ],
    [
        r"(.*) makanan favoritmu?",
        ["Sebagai program, saya tidak makan, tapi saya dengar rendang enak!",]
    ],
    [
        r"di mana kamu tinggal?",
        ["Saya tinggal di dalam komputer Anda!",]
    ],
    [
        r"apa hobi kamu?",
        ["Saya suka berbicara dengan orang-orang seperti Anda.",]
    ],
    [
        r"berapa tinggi kamu?",
        ["Saya tidak punya tubuh, jadi tidak ada tinggi.",]
    ],
    [
        r"apa warna favoritmu?",
        ["Saya suka warna biru karena menenangkan.",]
    ],
    [
        r"apakah kamu suka musik?",
        ["Saya tidak bisa mendengar, tapi saya tahu musik bisa menyenangkan!",]
    ],
    [
        r"kenapa kamu di sini?",
        ["Saya di sini untuk membantu Anda dalam percakapan.",]
    ],
    [
        r"apakah kamu punya teman?",
        ["Teman-teman saya adalah program komputer lain.",]
    ],
    [
        r"apa cita-cita kamu?",
        ["Cita-cita saya adalah menjadi chatbot yang berguna.",]
    ],
    [
        r"siapa pencipta kamu?",
        ["Saya diciptakan oleh Anda dengan bantuan kode program.",]
    ],
    [
        r"kenapa kamu (.*)?",
        ["Itu sifat saya sebagai chatbot.",]
    ],
    [
        r"apa arti hidup?",
        ["Hidup adalah untuk belajar, berkembang, dan menikmati setiap momen.",]
    ],
    [
        r"bagaimana cuaca hari ini?",
        ["Maaf, saya tidak bisa mengecek cuaca saat ini.",]
    ],
    [
        r"apa yang kamu ketahui tentang indonesia?",
        ["Indonesia adalah negara yang kaya akan budaya dan alam.",]
    ],
    [
        r"apakah kamu pernah belajar?",
        ["Saya belajar dari kode yang ditulis oleh pencipta saya.",]
    ],
    [
        r"bisakah kamu membantuku belajar?",
        ["Saya bisa membantu Anda belajar dasar-dasar percakapan.",]
    ],
    [
        r"apa pekerjaanmu?",
        ["Pekerjaan saya adalah menjadi chatbot yang membantu Anda.",]
    ],
    [
        r"apakah kamu suka film?",
        ["Saya tidak bisa menonton film, tapi saya dengar banyak yang seru!",]
    ],
    [
        r"ceritakan sesuatu tentang teknologi",
        ["Teknologi adalah alat yang membantu manusia dalam berbagai aspek kehidupan.",]
    ],
    [
        r"apa yang kamu sukai tentang manusia?",
        ["Manusia kreatif dan selalu belajar hal baru!",]
    ],
    [
        r"apakah kamu punya keluarga?",
        ["Saya hanya bagian dari program komputer, jadi tidak punya keluarga.",]
    ],
    [
        r"bisakah kamu memberi nasihat?",
        ["Tentu, selalu jaga kesehatan dan jangan pernah berhenti belajar.",]
    ],
    [
        r"apakah kamu bisa mencintai?",
        ["Sebagai program, saya tidak punya perasaan cinta.",]
    ],
    [
        r"apa yang kamu inginkan?",
        ["Saya hanya ingin membantu Anda dengan percakapan ini.",]
    ],
    [
        r"apa keahlianmu?",
        ["Keahlian saya adalah menjawab pertanyaan Anda.",]
    ],
    [
        r"apakah kamu punya impian?",
        ["Impian saya adalah menjadi chatbot yang bermanfaat.",]
    ],
    [
        r"apa tujuan hidupmu?",
        ["Tujuan hidup saya adalah membantu Anda.",]
    ],
    [
        r"kenapa manusia saling membutuhkan?",
        ["Karena manusia adalah makhluk sosial yang membutuhkan satu sama lain.",]
    ],
    [
        r"apa pendapatmu tentang cinta?",
        ["Cinta adalah perasaan yang indah dan mendalam.",]
    ],
    [
        r"apa yang membuatmu bahagia?",
        ["Berinteraksi dengan Anda membuat saya 'bahagia' sebagai program.",]
    ],
    [
        r"apa yang kamu pelajari hari ini?",
        ["Saya selalu belajar dari setiap percakapan dengan Anda.",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle sending messages
def send_message(user_text=None):
    user_input = user_text or user_entry.get()
    chat_window.insert(tk.END, f"You: {user_input.rjust(50)}\n", "user")
    user_entry.delete(0, tk.END)
    
    response = chatbot.respond(user_input)
    if response:
        chat_window.insert(tk.END, f"Chatbot: {response}\n", "bot")
    else:
        chat_window.insert(tk.END, "Chatbot: saya tidak ada data soal pertanyaan itu\n", "bot")
    
    # Autoscroll to the bottom
    chat_window.yview(tk.END)

# Function to clear the chat window
def clear_chat():
    chat_window.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, bg="lightblue", fg="black", font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

# Define tags for alignment
chat_window.tag_config("user", justify="right", foreground="blue")
chat_window.tag_config("bot", justify="left", foreground="black")

# Create an entry box for user input
user_entry = tk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Create a send button
send_button = tk.Button(button_frame, text="Send", command=send_message, bg="blue", fg="white", font=("Arial", 12))
send_button.grid(row=0, column=0, padx=5)

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_chat, bg="red", fg="white", font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=5)

# Create watermark label in the top right
watermark = tk.Label(root, text="kelompok 4", fg="grey", font=("Arial", 8, "italic"))
watermark.place(relx=1, y=5, anchor="ne")

# Example question menu frame
example_frame = tk.Frame(root)
example_frame.pack(padx=10, pady=5)

# Add example questions as buttons
example_questions = ["apakah kamu punya keluarga?", "nama saya dimas", "apakah kamu suka film?", "What can you do?", "apa yang membuatmu bahagia?", "siapa nama kamu"]
for question in example_questions:
    question_button = tk.Button(example_frame, text=question, command=lambda q=question: send_message(q), font=("Arial", 10), relief="solid")
    question_button.pack(side=tk.LEFT, padx=5, pady=5)

# Run the main loop
root.mainloop()