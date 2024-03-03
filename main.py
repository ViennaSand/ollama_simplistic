from gtts import gTTS
import tempfile
from playsound import playsound
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'  # required, but unused
)


def speak_test(answer):
    to_tell = gTTS(answer, lang='en', tld='us')
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        temp_file_name = temp_file.name
        to_tell.save(temp_file_name)
        temp_file.close()
        playsound(temp_file_name)


response = client.chat.completions.create(
    model="mistral",
    messages=[
        {"role": "user", "content": "Could you please propose a text of 50 words that promote team work? ."
         },
    ]
)

if __name__ == '__main__':

    speak_test(response.choices[0].message.content)
    print(response.choices[0].message.content)
