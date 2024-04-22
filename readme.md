# Budget Tracker WebApp

This is a simple web application built with Flask that allows users to add expense entries.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/at-sso/Budget-Tracker-WebApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Budget-Tracker-WebApp
   ```

3. Install the required dependencies:

   ```bash
   pip install -r ./env/requirements.txt
   ```

## Usage

To run the application, execute the following command:

```bash
python main.py
```

The application will be accessible at `http://localhost:5000` in your web browser.

## Features

- **Expense Form**: Users can add new expense entries through a web form.
- **Validation**: The form validates that both the name and amount fields are filled out before submission.
- **Simple Interface**: The interface is designed to be user-friendly and intuitive.

## Dependencies

- Flask
- Flask-WTF
- WTForms

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](license).
