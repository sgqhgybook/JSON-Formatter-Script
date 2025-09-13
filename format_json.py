import json

def format_json(json_string, indent=4):
    """
    Formats a given JSON string with proper indentation for readability.

    Args:
        json_string (str): The input JSON string.
        indent (int, optional): Number of spaces for indentation. Defaults to 4.

    Returns:
        str: The formatted JSON string, or an error message if invalid JSON.
    """
    try:
        parsed = json.loads(json_string)
        return json.dumps(parsed, indent=indent)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

if __name__ == "__main__":
    # Example usage:
    input_json = input("Enter a JSON string: ")
    print(format_json(input_json))
