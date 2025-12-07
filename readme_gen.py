from pathlib import Path


def ask(prompt, default=""):
    value = input(f"{prompt}: ").strip()
    return value or default


def build_readme(data, template_name):
    template_path = Path("templates") / f"{template_name}.md"

    if not template_path.exists():
        raise FileNotFoundError(f"Template '{template_name}' not found.")

    content = template_path.read_text(encoding="utf-8")

    for key, value in data.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    return content.strip() + "\n"


def main():
    print("\nreadme-gen-lite — quick README generator\n")

    print("Choose a template:")
    print("1. minimal")
    print("2. basic")
    print("3. detailed")
    print("4. aesthetic")
    print("5. engineering-girl")

    choice = ask("Template (1–5)", "2")

    template_map = {
        "1": "minimal",
        "2": "basic",
        "3": "detailed",
        "4": "aesthetic",
        "5": "engineering-girl",
    }

    template_name = template_map.get(choice, "basic")

    data = {
        "project_name": ask("Project name", "my-project"),
        "description": ask("Short description", "A small project that does something useful."),
        "f1": ask("Feature 1", "Simple"),
        "f2": ask("Feature 2", "Lightweight"),
        "f3": ask("Feature 3", "Easy to use"),
        "language": ask("Main language", "Python"),
        "dependencies": ask("Dependencies", "None"),
        "install": ask("Install command", "pip install -r requirements.txt"),
        "run": ask("Run command", "python main.py"),
        "contribute": ask("Contributing notes", "Pull requests are welcome."),
        "license": ask("License", "MIT"),
    }

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(build_readme(data, template_name))

    print(f"\n✅ README.md created using '{template_name}' template\n")


if __name__ == "__main__":
    main()
