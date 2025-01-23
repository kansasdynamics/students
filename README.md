# Students Spreadsheet Update
Take an Excel Spreadsheet input and output a new version with student information in easier to use formats.


# Instructions for Running the Python Script

This guide provides step-by-step instructions on how to set up Python, install required modules, and execute the provided script to process the student data.

---

## 1. Install Python

### Step 1: Download Python
- Go to the [official Python website](https://www.python.org/downloads/).
- Download the latest stable version of Python for your operating system (Windows, macOS, or Linux).

### Step 2: Install Python
1. Run the installer.
2. On the setup screen, check the box **"Add Python to PATH"** (this is important).
3. Click **Install Now** and follow the on-screen instructions.
4. Once installed, verify Python is working:
   - Open a terminal or command prompt.
   - Run: `python --version` (or `python3 --version` on some systems).
   - You should see the installed version of Python.

---

## 2. Install Required Python Modules

The script requires the following modules:
- `pandas`
- `openpyxl`

### Step 1: Open a Terminal or Command Prompt

### Step 2: Install Modules
Run the following commands:
```bash
pip install pandas openpyxl
```

To verify the modules are installed, run:
```bash
pip show pandas openpyxl
```
This will display information about the installed modules.

---

## 3. Save the Python Script

### Step 1: Copy the Script
Save the Python script provided above to a `.py` file. For example, you can save it as `process_students.py`.

### Step 2: Verify Input and Output File Paths
1. Ensure the input file (`input.xlsx`) is in the correct location.
2. Update the `input_file` and `output_file` paths in the script if needed:
   ```python
   input_file = r"C:\path\to\input.xlsx"
   output_file = r"C:\path\to\output.xlsx"
   ```

---

## 4. Run the Script

### Step 1: Open a Terminal or Command Prompt
Navigate to the directory containing the script using:
```bash
cd C:\path\to\script
```

### Step 2: Run the Script
Execute the script using:
```bash
python process_students.py
```

### Step 3: Check the Output
The script will generate an output file (`output.xlsx`) in the specified path. Open this file to verify the results.

---

## 5. Troubleshooting

### Issue: "pip is not recognized"
- Ensure Python was added to PATH during installation.
- If not, reinstall Python and check the box **"Add Python to PATH"**.

### Issue: Module Not Found
- Ensure the modules are installed by running:
  ```bash
  pip install pandas openpyxl
  ```

### Issue: Script Fails with Errors
- Double-check the input file (`input.xlsx`) structure.
- Ensure it matches the format described in the script.
- Verify that the rows and columns are aligned as expected.

---

## 6. Additional Notes
- Always make sure the input file has the correct format before running the script.
- You can modify the output file name and path as needed.
- For further assistance, refer to the [Python documentation](https://docs.python.org/3/).

