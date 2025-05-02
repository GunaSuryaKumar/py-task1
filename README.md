
# AI Personal Assistant in Python

This Python script creates a basic AI personal assistant that can perform several tasks, including:

* **Text-to-Speech:** Speaks responses and information to the user.
* **Speech Recognition:** Listens to user commands via the microphone.
* **Date and Time:** Tells the current date and time.
* **Screenshot:** Takes a screenshot of the current screen.
* **AI Chatbot Interaction:** Sends user queries to the Eden AI API and speaks the chatbot's response.

## Prerequisites

Before running this script, ensure you have Python installed on your system. You will also need to install the following Python libraries. You can install them using pip:


pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio  # Required for microphone input with SpeechRecognition
pip install setuptools # May be required for pyaudio
pip install pyscreeze
pip install Pillow     # Required by pyscreeze for image manipulation
pip install requests
pip install openai     # Although currently not directly used, it's imported

Note on pyaudio: Installing pyaudio can sometimes be tricky. You might need to install system-level dependencies depending on your operating system. Refer to the pyaudio documentation for specific instructions for your OS.
Setup
 * Clone the Repository (if applicable):
   If this code is hosted in a repository (e.g., on GitHub), you'll first need to clone it to your local machine. Open your terminal or command prompt and navigate to the directory where you want to store the project, then run:
   git clone <repository_url>

   Replace <repository_url> with the actual URL of the repository.
 * Navigate to the Project Directory:
   Once cloned (or if you have the main.py file directly), navigate into the project directory in your terminal:
   cd <project_directory>

   Replace <project_directory> with the name of the directory containing the main.py file.
 * Install Dependencies:
   If you haven't already, install all the required Python libraries using pip:
   pip install -r requirements.txt

   (Optional: Create a requirements.txt file in the project directory with the list of dependencies if you plan to share or manage the project more formally. The content of requirements.txt would be:
   pyttsx3
SpeechRecognition
pyaudio
setuptools
pyscreeze
Pillow
requests
openai

   Then run the pip install -r requirements.txt command.)
 * Obtain an Eden AI API Key:
   This script uses the Eden AI API for chatbot functionality. You need to sign up for an account on the Eden AI website and obtain your API key.
 * Update the API Key in the Script:
   Open the main.py file in a text editor and replace the placeholder API key with your actual Eden AI API key in the headers dictionary:
   headers = {"Authorization": "Bearer YOUR_EDEN_AI_API_KEY"}

Running the Script
Once you have installed the prerequisites and updated the API key, you can run the script from your terminal using the Python interpreter:
python main.py

The script will first greet you, and then it will start listening for your commands. Speak clearly into your microphone.
Using the Assistant
Here are some commands you can try:
 * "time": To hear the current time.
 * "date": To hear the current date.
 * "screenshot": To take a screenshot of your screen. The script indicates that the screenshot is saved as screenshot.png in the same directory as the script.
 * "exit": To terminate the assistant.
 * Any other query: The script will send your query to the Eden AI chatbot and speak its response. For example, you can ask:
   * "Hello, how are you?"
   * "What is the weather like today?"
   * "Tell me a joke."
Contributing and Working on the Project
If you want to contribute to this project or work on it yourself, here's a typical workflow:
 * Fork the Repository (if you don't have direct write access):
   * Go to the project's repository page (e.g., on GitHub).
   * Click the "Fork" button in the top right corner. This will create a copy of the repository under your own GitHub account.
 * Clone the Forked Repository to Your Local Machine:
   * Open your terminal or command prompt.
   * Navigate to the directory where you want to store the project.
   * Use the git clone command with the URL of your forked repository:
     git clone https://github.com/GunaSuryaKumar/py-task1.git

     Replace YOUR_USERNAME with your GitHub username and REPOSITORY_NAME with the name of the repository.
 * Navigate to the Project Directory:
   cd REPOSITORY_NAME

 * Set Up a Virtual Environment (Recommended):
   It's good practice to create a virtual environment to isolate the project's dependencies.
   python -m venv venv  # Create a virtual environment named 'venv'
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate  # On Windows

 * Install Dependencies in the Virtual Environment:
   pip install -r requirements.txt

   (If you created the requirements.txt file) or install them individually as listed in the Prerequisites section.
 * Create a New Branch for Your Changes:
   Before making any modifications, create a new branch to keep your work separate from the main codebase:
   git checkout -b feature/your-new-feature  # Replace 'feature/your-new-feature' with a descriptive name for your branch

 * Make Your Changes and Commit Them:
   * Edit the Python files (e.g., main.py) to add new features, fix bugs, or make improvements.
   * Stage your changes:
     git add .  # Add all modified files

   * Commit your changes with a clear and concise message:
     git commit -m "Add new feature: ..."

 * Push Your Changes to Your Forked Repository:
   git push origin feature/your-new-feature

 * Create a Pull Request (if you want to contribute to the original repository):
   * Go to the original project's repository on GitHub.
   * You should see a notification asking if you want to create a pull request for the branch you just pushed.
   * Click "Compare & pull request".
   * Provide a clear title and description for your pull request, explaining the changes you've made.
   * Click "Create pull request".
 * Stay Updated:
   To keep your local repository in sync with the original repository, you can add the original repository as a remote and fetch/merge changes:
   git remote add upstream https://github.com/GunaSuryaKumar/py-task1.git
git fetch upstream
git merge upstream/main  # Or upstream/develop, depending on the main branch name

Further Development Ideas
Here are some ideas for expanding this personal assistant:
 * Web Searching: Integrate the ability to search the web for information.
 * Playing Music: Add functionality to play music.
 * Opening Applications: Allow the user to open specific applications using voice commands.
 * Reminders and Alarms: Implement a system for setting reminders and alarms.
 * More Sophisticated Chatbot Interaction: Explore other AI models or fine-tune the interaction with the current one.
 * GUI: Create a graphical user interface for easier interaction.
 * Task Automation: Add the ability to automate simple tasks.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

MIT License

Copyright (c) [2025] Guna Surya Kumar Katakam.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


