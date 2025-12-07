# readme-gen-lite ✨

A lightweight Python CLI tool that generates clean and stylish `README.md` files
using multiple templates — from minimal and professional to aesthetic and
engineering-girl core (kaomojis included).

---

## ✨ Why readme-gen-lite?

Writing a README often takes more effort than writing the actual code.
**readme-gen-lite** removes that friction by letting you:

- Answer a few simple prompts
- Choose a template that matches your vibe
- Instantly generate a well-formatted `README.md`

No frameworks. No dependencies. Just Python and good taste.

---

## 🚀 Features

- Interactive command-line interface  
- Multiple built-in README templates  
- Clean Markdown output  
- No external libraries required  
- Beginner-friendly and easily extensible  

---

## 🗂 Available Templates

| Template | Style |
|--------|-------|
| `minimal` | Very clean and short |
| `basic` | Standard GitHub README |
| `detailed` | Full project documentation |
| `aesthetic` | Soft emojis & minimal vibes |
| `engineering-girl` | Kaomojis, emojis & logic ✨ |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/nazeyanehal/readme-gen-lite.git
cd readme-gen-lite
```

# ▶️ Usage

Run the generator:

python readme_gen.py

You will be prompted to:

Choose a template

Enter project details (name, features, tech stack, etc.)

The generated README will be saved as:

README.md

in the same folder.

# 🧠 How It Works

Templates are stored as Markdown files inside the templates/ directory

Placeholders like {{project_name}} are replaced using simple string substitution

The script dynamically loads and fills the selected template

This keeps the code minimal, readable, and easy to modify.

# 🛠 Tech Stack

Python

Markdown

# 🌱 Future Enhancements (Optional)

Custom output file name

Template preview mode

User-defined templates

CLI flags instead of interactive prompts

# 🤝 Contributing

Contributions are welcome.
Feel free to open an issue or submit a pull request with improvements or new templates.

# 📄 License

MIT License
