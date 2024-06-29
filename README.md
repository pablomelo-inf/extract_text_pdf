
# PDF Exam Question Extractor

This project implements a feature to extract text questions from the PDF of the ENEM 2015 exam.

## Description

The goal of this repository is to provide a Python-based solution for extracting text questions from the ENEM 2015 exam PDF. The project utilizes `pdfplumber` for handling PDF parsing and extraction, and the extracted data can be saved in JSON format.

## Features

- Extracts text questions from the ENEM 2015 exam PDF.
- Parses the PDF and processes text to identify and separate questions.
- Saves extracted questions to a JSON file for easy access and manipulation.

## Installation

1. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project requires the following Python libraries:

- `pdfplumber`
- `json` (part of Python's standard library)

You can find the dependencies listed in the `requirements.txt` file.

## Usage

1. **Place the ENEM 2015 PDF in the project directory.**

2. **Run the extraction script:**

   ```bash
   python extract_questions.py
   ```

3. **Output:**

   The script will generate a `questions.json` file containing the extracted questions.

## Project Structure

- `extract_questions.py`: The main script to extract questions from the PDF.
- `requirements.txt`: A file listing the dependencies required for the project.
- `questions.json`: The output file containing the extracted questions (generated after running the script).



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
