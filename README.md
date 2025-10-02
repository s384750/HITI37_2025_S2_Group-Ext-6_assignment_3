Overview

This project is a Tkinter-based GUI application that allows users to interact with multiple machine learning models. The GUI supports text-to-speech and image classification, and can be extended to other models. It demonstrates OOP principles like inheritance, encapsulation, polymorphism, and method overriding in Python.

Files & Descriptions

1. GUI.py
Purpose: Main entry point of the project. Launches the GUI for model interaction.
Key Features:
Main window with menu bar (File, Models, Help).
Model selection dropdown and Load Model button.
Input section with Text/Image selection, Browse, Run Model, and Clear buttons.
Output section to display model results.
Model information panel showing name, category, and description.
OOP concepts explanation panel demonstrating assignment design choices.

Behavior:
Select a model → click Load Model → updates model info and input type.
Enter input → click Run Model → output appears in the output panel.
Click Clear → input and output are reset.

2. models_handler.py
Purpose: Contains all the machine learning models used by the application.

Included Models:
text to speech: (ightweight TTS model: facebook/mms-tts-mfe)
Image Classification Model (WinKawaks/vit-tiny-patch16-224)

Usage Notes:
Update or replace models by editing the BaseModel subclasses.
Each model has a run() method that takes the input and returns results.
For image models, you need to provide the full image file path.

3. file_handler.py
Purpose: Handles file selection dialogs for opening and saving files.

Functions:
open_file(): Opens a file selection dialog and returns the full path.
save_file(): Opens a save file dialog and returns the desired path.
Integration: Used in the GUI Browse, Open, and Save buttons.

4. oop_explanation.py
Purpose: Provides explanations of the OOP concepts applied in the project.

Function:
get_oop_info(): Returns a list of explanations covering:
Multiple Inheritance
Encapsulation
Polymorphism
Method Overriding
Decorators usage
Integration: Populates the OOP concepts panel in the GUI.

Installation
Clone the repository

git clone <your-repo-url>
cd <repository-folder>


Set up a Python virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Required libraries include:
transformers
torch
Pillow
tkinter (usually included with Python)
scipy (only if using TTS)

Running the Application
python GUI.py

Steps:
Select a model from the dropdown.
Click Load Model.
Enter text or browse for an image depending on the model.
Click Run Model to get results.
Optionally, click Clear to reset input and output fields.

Usage Notes
Text-to-Speech: Converts typed text into audio saved as output.wav. Playback requires an audio player.
Image Classification: Provide image file path, output shows top predicted classes.

Changing Models:
Edit models_handler.py and modify or add new subclasses of BaseModel.
Update the get_available_models() dictionary to include new models.

OOP Concepts Applied
Multiple Inheritance: GUI integrates with Model Handler functionality.
Encapsulation: Models stored as attributes in classes.
Polymorphism: All models inherit from BaseModel and override run().
Method Overriding: run() implementation differs per model type.
Decorators (Optional): Can be applied for logging or validation.

Notes
Image models require full file paths; GUI Browse button helps select files.
Text-to-Speech models may produce large audio files depending on the model size.
For large models, GPU is recommended for faster inference.
