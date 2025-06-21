# handwriting-plotter
Generates randomized G-code handwriting for pen plotters

📦 1. Clone the Repository
If you haven't already:

**bash
git clone https://github.com/YOUR_USERNAME/handwriting-plotter.git
cd handwriting-plotter

🐍 2. Set Up the Python Environment
Create and activate a virtual environment:

**bash**
python3 -m venv venv
source venv/bin/activate

🐍 2.1 Install required Python packages:

**bash**
pip install -r requirements.txt

🗂️ 3. Prepare Your Input Files (I ALREADY DID THIS FOR YOU RACHEL)
You’ll need two files in the input/ folder:

📝 notecard_template.txt
A text file that includes placeholders like {FULL_NAME}, {USERNAME}, {ADDRESS}, {EMAIL}, {CODE}. Example:

css

Copy
Edit
{FULL_NAME}
{USERNAME}
{ADDRESS}
{EMAIL}
CODE: {CODE}

I wish to receive Stake cash...

✏️ 4. Generate Handwriting G-code Files
Run the script:

**bash**
python app/write_letter.py



