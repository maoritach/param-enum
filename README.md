# param-enum
## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/maoritach/param-enum.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the script:

    ```
    python main.py [options]
    ```

## Requirements

- Python 3.x
- `requests` library
- `json` library
- `argparse` library
- `tabulate` library
- `termcolor` library

## Interactive Mode

If the script is run without any command line arguments, it enters interactive mode, prompting the user to enter the required information such as Project ID, Discovery ID, API Key, and Cluster.

## Command Line Arguments

- `-p`, `--project`: Project ID
- `-d`, `--discovery`: Discovery ID
- `-t`, `--api-key`: API Key
- `-c`, `--cluster`: Cluster (choices: 'eu' or 'app')

## Result Display

![Screenshot 2023-11-16 014703](https://github.com/maoritach/param-enum/assets/99506255/b05e0ed8-b007-4a35-9333-3e3e13b6c7fb)

## Dependencies

- [requests](https://docs.python-requests.org/en/latest/)
- [tabulate](https://pypi.org/project/tabulate/)
- [termcolor](https://pypi.org/project/termcolor/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
