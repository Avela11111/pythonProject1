import os

def test_path():
    # Use a raw string with double backslashes or forward slashes
    file_path = r"\pythonProject1\TestCases\conftest.py"

    # Get the absolute path by joining the current working directory and the file path
    full_path = os.path.join(os.getcwd(), file_path)

    if os.path.exists(full_path):
        print("File exists")
        # File exists, proceed with your code
    else:
        print(f"File not found: {full_path}")

def test_workingpath():
    current_path = os.getcwd()
    print(current_path)

if __name__ == "__main__":
    test_path()
    test_workingpath()
