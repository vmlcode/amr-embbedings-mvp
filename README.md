# Embeddings MVP

## Overview
This project is a Minimum Viable Product (MVP) for generating and utilizing embeddings in various machine learning tasks. Embeddings are dense vector representations of data that can capture semantic relationships and are widely used in natural language processing, recommendation systems, and other AI applications.

## Features
- Generate embeddings from text data
- Utilize embeddings for similarity search
- Integration with machine learning models

## Setup
To set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/embeddings-mvp.git
    cd embeddings-mvp
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To generate embeddings and perform similarity search, follow these steps:

1. Prepare your fasta files in the DB folder

2. Run the db generation script:
    ```bash
    python preprocessing.py --input data.txt --output embeddings.npy
    ```


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
