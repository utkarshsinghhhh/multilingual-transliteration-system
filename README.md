#  Multilingual Transliteration System

A powerful and accurate transliteration tool that converts **Roman (English) text** into native scripts including **Hindi, Bengali, and Tamil**. It uses a hybrid approach combining neural transformation (mT5) with precise rule-based engines.

## Features
- **Hybrid Engine:** Uses `google/mt5-small` for neural demonstration and `indic-transliteration` for production-grade accuracy.
- **Support for 3 Languages:** Hindi (Devanagari), Bengali, and Tamil.
- **Dual Interfaces:** Use the Command Line Interface (CLI) or a modern Web UI.
- **Batch Processing:** Built-in support for processing datasets from AI4Bharat's Aksharantar.

---

## Setup Instructions

### 1. Prerequisite
Ensure you have **Python 3.8+** installed.

### 2. Installation
Clone this repository and install the dependencies:

```bash
# Install core dependencies
pip install torch transformers==4.39.3 tokenizers==0.15.2
pip install indic-transliteration sentencepiece protobuf gradio
```

---

## Usage

### Option 1: Web Interface (Recommended)
Run the Gradio app for a beautiful, interactive UI:
```bash
python app.py
```
*Locally visit: `http://127.0.0.1:7860`*

### Option 2: Command Line Interface
Run the script to transliterate directly in your terminal:
```bash
python main.py
```

### Option 3: Dataset Loading
To download and preview samples from the AI4Bharat Aksharantar dataset:
```bash
python dataset.py
```

---

## Sample Outputs

The system correctly maps phonetic Roman text to the target script:

| Input (Roman) | Hindi (हिंदी) | Bengali (বাংলা) | Tamil (தமிழ்) |
| :--- | :--- | :--- | :--- |
| `mera naam utkarsh hai` | मेरा नाम उत्कर्ष है | মেরা নাম উৎকর্ষ হৈ | மேரா நாம் உத்கர்ஷ ஹை |
| `bharat ek mahan desh hai` | भारत एक महान देश है | ভারত এক মহান দেশ হৈ | பாரத ஏக மஹான தேஷ ஹை |
| `ami tomake bhalobashi` | अमि तोमाके भालोबाशि | আমি তোমকে ভালোবাশি | அமி தோமாகே பாலோபாஷி |
| `vanakkam eppadi irukeenga` | वणक्कम एप्पडि इरुकींगा | বণক্কম এপ্কডি ইরুকীঙ্গা | வணக்கம் எப்படி இருக்கீங்க |

---

## Project Structure
- `app.py`: Full-featured Gradio Web Application.
- `main.py`: Hybrid transliteration logic (CLI).
- `dataset.py`: AI4Bharat dataset handling and downloading.
- `requirements.txt`: List of required libraries.

---

## About the Project
This project was developed to show the capability of combining **Deep Learning (mT5)** with **Deterministic Rules** to solve the complex problem of Indian language transliteration where phonetic mapping is key.
