# Product Registration Automation

Portuguese version: [README.md](README.md)

This project automates product registration in a web system using Python and the `pyautogui` library.

## Overview

The main goal is to open the browser, go to a login page, authenticate, and automatically register products based on the data in the `produtos.csv` file.

## Project Files

- `codigo.py`: main automation script that logs in and registers each product from `produtos.csv`.
- `auxiliar.py`: utility to capture the mouse position on the screen. Very useful to adjust click coordinates.
- `pegar_posicao.py`: simple script that prints the current mouse position after 5 seconds.
- `gabarito.py`: reference version of the automation with the main steps detailed.
- `produtos.csv`: example dataset with the products to register.

## Dependencies

Install the required libraries before running the project:

```bash
pip install pyautogui pyperclip pandas
```

> Note: in some cases, `pyautogui` requires additional packages such as `pillow`.

## How It Works

1. The script opens the Google Chrome browser.
2. It navigates to the login link:
   `https://dlp.hashtagtreinamentos.com/python/intensivao/login`
3. Logs in with the email `pythonimpressionador@gmail.com` and the password specified in the code.
4. Loads the `produtos.csv` spreadsheet using `pandas`.
5. Iterates over each row in the file, filling form fields and submitting the registration.
6. After each registration, the script scrolls to return to the top of the page.

## `produtos.csv` File Structure

The CSV must contain the following columns:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

## How to Run

1. Adjust your execution environment and activate your virtualenv if desired.
2. Verify your monitor resolution.
3. If necessary, use `auxiliar.py` or `pegar_posicao.py` to capture correct click coordinates.
4. Run:

```bash
python codigo.py
```

## Warnings / Recommendations

- The automation depends on fixed click positions on the screen. If the layout or resolution changes, you will need to adjust the `x` and `y` values in the code.
- To stop `pyautogui`, move the cursor to the top-left corner of the screen (0,0).
- Do not run the script while using the computer for other tasks, as it controls the mouse and keyboard.

## Possible Improvements

- Replace fixed coordinates with image or visual element detection.
- Use exception handling to detect when the site does not load correctly.
- Make the username and password configurable parameters.
- Read other data formats, such as Excel (`.xlsx`).

## References

- `pyautogui` documentation: https://pyautogui.readthedocs.io
- `pandas` documentation: https://pandas.pydata.org
