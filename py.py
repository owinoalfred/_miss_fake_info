import os

# Define the project structure
project_structure = [
    "app.py",
    "summarizer.py",
    "config.py",
    ".env",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "tests/test_summarizer.py"
]

# Create the project folder
project_root = "AI_Document_Summarizer"

# Loop through the project structure
for file_path in project_structure:
    full_path = os.path.join(project_root, file_path)
    
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Create the file
    with open(full_path, 'w') as f:
        pass  # Empty file creation

print("Files created successfully!")
