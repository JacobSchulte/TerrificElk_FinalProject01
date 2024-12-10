#JSONreader.py
import json

class JSONReader:
  """
  Reads and parses JSON data from files.
  """
  def __init__(self, file_path):
    """
    Initializes the JSON reader with the path to the JSON file.

    Args:
      file_path (str): The path to the JSON file.
    """
    self.file_path = file_path

  def load_data(self):
    """
    Loads and parses the JSON data from the file.

    Returns:
      dict: The parsed JSON data as a dictionary.

    Raises:
      OSError: If the file cannot be opened.
      json.JSONDecodeError: If the file content is not valid JSON.
    """

  def load_json_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
  def get_data_for_name(data, name):
    if name in data:
        return data[name]
    else:
        print(f"Name '{name}' not found in the JSON data.")
        return None
    try:
      with open(self.file_path, 'r') as file:
        data = json.load(file)
      return data
    except OSError as e:
      raise OSError(f"Error opening file: {self.file_path}. {str(e)}")
    except json.JSONDecodeError as e:
      raise ValueError(f"Invalid JSON data in file: {self.file_path}. {str(e)}")



