# Projet_07_OC

## Introduction

In this project, I will be developing an algorithm aimed at enhancing our short-term investment programs. 
My main goal is to create a solution that identifies the most profitable stocks for our clients, 
ensuring maximum profit after two years of investment while adhering to specific constraints:

    Each stock can only be purchased once.
    Fractional shares cannot be bought.
    I can spend a maximum of €500 per client.

The algorithm will read a file containing stock information, including stock names, costs, and projected profits 
after two years. It will explore all possible combinations of stocks to determine the best investment strategy.

## Requirements

- Python 3.10: https://www.python.org/downloads/release/python-31014/
- Clone the repository: https://github.com/Razvan-drb/Projet_07_OC

## Installation

Before proceeding, ensure that you have Python 3.10 installed on your computer. 
Follow the [Python Installation Guide](https://www.python.org/downloads/) if needed.

1. Clone the repository:

    ```bash
    git clone https://github.com/Razvan-drb/Projet_07_OC
    ```

2. Install the virtual environment:

    ```bash
    sudo apt install python3.10-venv
    python3 -m venv .venv
    ```

3. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

4. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

After completing the installation, you can run the scripts, right click on the file you want to execute and click on run 
Make sure the virtual environment is activated.

```bash
python3 bruteforce/bruteforce.py
```

```bash
python3 optimized/optimized.py
```

```bash
python3 optimized/dataset1.py
```

```bash
python3 optimized/dataset2.py
```

## Author

- Razvan DARABAN


## Contact

For any questions or concerns, you can contact the author:

- Email: [razvan_drb@yahoo.com](mailto:razvan-drb@yahoo.com)
- GitHub: [Razvan-drb](https://github.com/Razvan-drb)
