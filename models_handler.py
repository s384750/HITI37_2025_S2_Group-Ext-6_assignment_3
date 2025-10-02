
from transformers import pipeline
from PIL import Image
import numpy as np
from scipy.io.wavfile import write
import soundfile as sf  

class BaseModel:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def run(self, input_data):
        raise NotImplementedError

# Text-to-Speech Model
class TextToSpeechModel(BaseModel):
    def __init__(self):
        super().__init__("Text-to-Speech", "Converts text into speech audio and create an output.wav file in thie folder directory")
        from transformers import pipeline
        self.model = pipeline(
            "text-to-speech",
            model="facebook/mms-tts-mfe" 
        )

    def run(self, input_text, output_path="output.wav"):
        audio = self.model(input_text)
        audio_array = audio["audio"]

        import numpy as np
        if len(audio_array.shape) == 2:
            audio_array = audio_array.flatten()

        sampling_rate = audio["sampling_rate"]

        # Save audio to WAV
        from scipy.io.wavfile import write
        write(output_path, sampling_rate, audio_array)

        return f"Audio saved to {output_path}"




# Image Model
class ImageClassificationModel(BaseModel):
    def __init__(self):
        super().__init__("Image Classification", "Classifies images into categories (tiny ViT model).")
        self.model = pipeline("image-classification", model="WinKawaks/vit-tiny-patch16-224")

    def run(self, image_path):
        image = Image.open(image_path)
        return self.model(image)

# Factory
def get_available_models():
    return {
        "Text-to-Speech": TextToSpeechModel(),
        "Image Classification": ImageClassificationModel()
    }
