# Address Verification App

## Project Overview

The **Address Verification App** is a desktop application that validates identity cards (CIN) and compares addresses between two images (CIN and facture) using advanced techniques like machine learning, image processing, and OpenAI's GPT API. The app features a graphical interface built with PySide6, image preprocessing via OpenCV, and powerful text extraction through APIs.

---

## Features
- **CIN Validation**: Verifies if an uploaded CIN image matches a predefined template.
- **Address Extraction**: Extracts address information from CIN and facture images using OpenAI's GPT API.
- **Address Comparison**: Compares extracted addresses to determine similarity.
- **User-Friendly Interface**: Offers an intuitive GUI for uploading images, tracking progress, and viewing results.

---

## Requirements

### Prerequisites
- **Python**: Version 3.8 or higher
- **OpenAI API Key**: Required for address extraction

### Libraries
The following libraries are required:
- `opencv-python` (Image processing)
- `numpy` (Array operations)
- `PySide6` (GUI development)
- `openai` (API interaction)
- `difflib` (String comparison for address similarity)

Install dependencies using:
```bash
pip install opencv-python numpy PySide6 openai
