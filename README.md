# JSON Formatter Script

This repository contains a simple Python script for formatting a given JSON string with proper indentation for improved readability.

## Features

- Accepts a raw JSON string as input
- Outputs the formatted (pretty-printed) JSON with customizable indentation
- Handles invalid JSON gracefully by displaying an error message

## Usage

1. **Run the script:**
    ```bash
    python format_json.py
    ```

2. **Enter your JSON string** when prompted.

3. **View the formatted output** printed to the console.

## Example

**Input:**
```
{"name":"John","age":30,"city":"New York"}
```

**Output:**
```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

## Requirements

- Python 3.x

## License

This project is open source and available under the [MIT License](LICENSE).
