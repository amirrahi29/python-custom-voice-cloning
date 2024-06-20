from elevenlabs.client import ElevenLabs
from elevenlabs import play, save

# Replace 'YOUR_API_KEY' with your actual ElevenLabs API key
API_KEY = "sk_873722231fd4ee93bc25dd2dc3744ea318db8c3874bafac0"

# Instantiate the client with your API key
client = ElevenLabs(api_key=API_KEY)

# Choose the model
model = "eleven_monolingual_v1"  # Change to "eleven_multilingual_v2" if needed

# Generate audio
audio = client.generate(
    text="Hey, how are you ?",
    voice="AmirRahiUniqueVoice",
    model=model
)

# Save the generated audio to a file
output_file = "output_audio.mp3"
save(audio, output_file)

# Play the generated audio file
play(audio)
