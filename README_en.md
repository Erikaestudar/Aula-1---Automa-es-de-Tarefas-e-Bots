# Product Registration Automation

Portuguese version: [README.md](README.md)

This project automates product registration in a web system using Python and the `pyautogui` library.

## Overview

The main goal of this project is to open a browser, navigate to a login page, authenticate the user, and automatically register products based on the data stored in the `produtos.csv` file.

## Project Files

- `codigo.py`: Main automation script responsible for logging in and registering each product from `produtos.csv`.
- `auxiliar.py`: Utility script used to capture the mouse position on the screen. Useful for adjusting click coordinates.
- `pegar_posicao.py`: Simple script that prints the current mouse position after 5 seconds.
- `gabarito.py`: Reference version of the automation script with the main steps documented in detail.
- `produtos.csv`: Sample dataset containing the products to register.

## Dependencies

Install the required libraries before running the project:

```bash
pip install pyautogui pyperclip pandas
```

> Note: In some environments, `pyautogui` may require additional dependencies such as `pillow`.

## How It Works

1. Open the Google Chrome browser.
2. Navigate to the login page:
   `https://dlp.hashtagtreinamentos.com/python/intensivao/login`
3. Authenticate using the email `pythonimpressionador@gmail.com` and the password defined in the script.
4. Loads the `produtos.csv` file using `pandas`.
5. Iterate through each row in the dataset, populate the form fields, and submit the registration form.
6. Scroll back to the top of the page after each registration.

## `produtos.csv` File Structure

Ensure the CSV file contains the following columns:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

## How to Run

1. Configure your environment and activate the virtual environment if desired.
2. Verify your monitor resolution.
3. Use `auxiliar.py` or `pegar_posicao.py` to capture the correct click coordinates if necessary.
4. Run the script:

```bash
python codigo.py
```

## Warnings / Recommendations

- The automation relies on fixed screen coordinates. If the screen layout or resolution changes, update the `x` and `y` coordinate values in the script.
- Move the cursor to the top-left corner of the screen (0,0) to stop `pyautogui`.
- Avoid using the computer for other tasks while the script is running, since it controls the mouse and keyboard.

## Possible Improvements

- Replace fixed coordinates with image recognition or UI element detection.
- Implement exception handling to detect page loading failures.
- v
- Support additional data formats such as Excel (`.xlsx`).

## References

- `pyautogui` documentation: https://pyautogui.readthedocs.io
- `pandas` documentation: https://pandas.pydata.org
