### Code Review Helper

Code Review Helper is a powerful tool designed to assist developers in reviewing their code. By leveraging FastAPI and Cohere's advanced language models, this tool analyzes code snippets to provide valuable suggestions for improvements, highlight potential bugs, and generate documentation comments. Whether you're working on a personal project or collaborating with a team, Code Review Helper enhances your code quality and boosts productivity.

#### Features
- **Automated Code Analysis:** Quickly analyze code snippets for improvements and potential issues.
- **Multi-Language Support:** Detects and reviews code in various programming languages.
- **Simple API Integration:** Easily integrate with your existing workflows using a RESTful API.
- **Real-Time Feedback:** Get instant feedback on your code to accelerate the development process.

#### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AlphaCodz/code-review-helper.git
    cd code-review-helper
    ```

2. Create and activate a virtual environment:
    ```sh
    poetry shell
    ```

3. Install the required dependencies:
    ```sh
    poetry install
    ```

4. Run the server:
    ```sh
    uvicorn main:app --reload
    ```

#### Usage

Send a POST request to the `/review_code/` endpoint with the code snippet you want to review. For example:

**Curl Command:**
```sh
curl -X POST "http://127.0.0.1:8000/review_code/" -H "Content-Type: application/json" -d '{"message": "def add(a, b):\n    return a + b"}'
```

**Example Response:**
```json
{
"1. The function `add` is simple and works as intended. However, consider adding type hints for better readability and error checking:\n\n```python\ndef add(a: int, b: int) -> int:\n    return a + b\n```\n\n2. Add a docstring to explain what the function does:\n\n```python\ndef add(a: int, b: int) -> int:\n    \"\"\"Returns the sum of a and b.\"\"\"\n    return a + b\n```"
}
```

#### Contributing

I welcome contributions from the community! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Contact

For questions or support, please contact [israelpy7@gmail.com](mailto:israelpy7@gmail.com).

---

Elevate your coding standards with Code Review Helper – your personal assistant for efficient and effective code reviews!
