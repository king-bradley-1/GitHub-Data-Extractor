# API Data Extractor

A Python script to extract repository details from the GitHub API and save them as a JSON file.

## Features

- Fetches repositories for a specified GitHub user.
- Stores repository details in a structured JSON file.
- Uses environment variables for authentication.

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [pandas](https://pypi.org/project/pandas/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the project root with the following content:
   - USER=your_github_username
   - PAT=Bearer your_github_pat

## Usage

Run the script: `main.py`

The repository details will be saved to `repo_details.json`.

## License

MIT License
