from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from models_handler import get_available_models
from file_handler import open_file, save_file
from oop_explanation import get_oop_info


# Create main window
root = Tk()
root.title("GUI")
root.resizable(False, False)

menubar = Menu(root)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Models menu
models_menu = Menu(menubar, tearoff=0)
models_menu.add_command(label="Load Model")
models_menu.add_command(label="Manage Models")
menubar.add_cascade(label="Models", menu=models_menu)

# Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About")
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)


# Top frame: Model selection
top_frame = Frame(root)
top_frame.pack(pady=5)

Label(top_frame, text="Model Selection:", width=20).pack(side=LEFT, fill=BOTH, padx=10)

available_models = get_available_models()
model_names = list(available_models.keys())
current_model = None  # Will store the loaded model

model_combo = ttk.Combobox(top_frame, values=model_names, width=20)
model_combo.pack(side=LEFT, fill=BOTH, padx=10)
model_combo.current(0)

def load_model():
    global current_model
    selected = model_combo.get()
    if selected in available_models:
        current_model = available_models[selected]
        messagebox.showinfo("Model Loaded", f"{selected} loaded successfully!")

        # Update model info
        model_name_label.config(text=f"• Model Name: {current_model.name}")
        model_category_label.config(text=f"• Category: {'Text' if 'Text' in current_model.name else 'Image'}")
        model_description_label.config(text=f"• Description: {current_model.description}")

        # Auto switch input type
        if "Text" in current_model.name:
            input_option.set("Text")
        else:
            input_option.set("Image")

Button(top_frame, text="Load Model", width=20, command=load_model).pack(side=LEFT, fill=BOTH, padx=10)


# Middle frame: User input and output
middle_frame = Frame(root)
middle_frame.pack()

# Input frame
input_frame = LabelFrame(middle_frame, text="User Input Selection", width=30, padx=10)
input_frame.grid(row=0, column=0, padx=10, pady=5)

input_option = StringVar(value="Text")
Radiobutton(input_frame, text="Text", variable=input_option, value="Text").grid(row=0, column=0, sticky="w")
Radiobutton(input_frame, text="Image", variable=input_option, value="Image").grid(row=0, column=1, sticky="w")
Button(input_frame, text="Browse", command=open_file).grid(row=0, column=2, padx=5)

# Assign Text widget to variable
input_text = Text(input_frame, height=6, width=30)
input_text.grid(row=1, column=0, columnspan=3, pady=10)

# Output frame
output_frame = LabelFrame(middle_frame, text="Output Display", width=30, padx=10)
output_frame.grid(row=0, column=1, padx=10, pady=5)

Label(output_frame, text="Output Display").grid(row=0)
output_text = Text(output_frame, height=10, width=30)
output_text.grid(row=1, column=0, columnspan=3, pady=10)


# Functions for Run and Clear
def run_model():
    selected_model_name = model_combo.get()
    models = get_available_models()
    model = models[selected_model_name]

    if input_option.get() == "Text":
        # For text models or Text-to-Speech
        user_input = input_text.get("1.0", END).strip()
        if "Text-to-Speech" in selected_model_name:
            # run TTS
            result = model.run(user_input, output_path="output.wav")
            messagebox.showinfo("Info", "Audio saved as output.wav")
        else:
            # run regular text model
            result = model.run(user_input)

        output_text.delete("1.0", END)
        output_text.insert(END, str(result))

    elif input_option.get() == "Image":
        # Use the Browse dialog to get image path
        image_file_path = open_file()  # <-- put it here
        if image_file_path:
            result = model.run(image_file_path)
            output_text.delete("1.0", END)
            output_text.insert(END, str(result))
        else:
            messagebox.showwarning("Warning", "No image selected!")

def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

Button(input_frame, text="Run Model", command=run_model).grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="w")
Button(input_frame, text="Clear", command=clear_text).grid(row=2, column=2, padx=5, pady=10)

# Info frame
info_frame = Frame(root, pady=5, padx=5)
info_frame.pack(fill=BOTH, expand=True)

# Model info
model_info = LabelFrame(info_frame, text="Model Information & Explanation", padx=10, pady=10)
model_info.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

model_name_label = Label(model_info, text="• Model Name:")
model_name_label.pack(anchor="w")
model_category_label = Label(model_info, text="• Category:")
model_category_label.pack(anchor="w")
model_description_label = Label(model_info, text="• Description:")
model_description_label.pack(anchor="w")

# OOP explanation
oop_info = LabelFrame(info_frame, text="OOP Concepts Explanation:", padx=10, pady=10)
oop_info.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

for line in get_oop_info():
    Label(oop_info, text=f"• {line}").pack(anchor="w")

Label(root, text="Notes: you have to load Model before use").pack(side=LEFT, fill=BOTH, padx=10, pady=5)

# Run GUI loop
root.mainloop()
