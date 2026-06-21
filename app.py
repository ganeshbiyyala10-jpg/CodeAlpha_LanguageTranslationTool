from googletrans import Translator

translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr"
}

text = input("Enter text: ")

print("Available Languages:")
for lang in languages:
    print(lang)

source = input("Source Language: ")
target = input("Target Language: ")

result = translator.translate(
    text,
    src=languages[source],
    dest=languages[target]
)

print("\nTranslated Text:")
print(result.text)