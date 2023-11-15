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

The script performs a GET request to the specified API endpoint and checks for the existence of certain parameter types in the response. The results are displayed in a table with colors indicating whether each parameter type was found.

## Dependencies

- [requests](https://docs.python-requests.org/en/latest/)
- [tabulate](https://pypi.org/project/tabulate/)
- [termcolor](https://pypi.org/project/termcolor/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.