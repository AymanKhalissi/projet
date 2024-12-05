import base64
from openai import OpenAI
import difflib

# Initialize the OpenAI client
client = OpenAI(api_key="provide your api key")

def encode_image(image_path):
    """
    Encodes an image into base64 format.

    Args:
        image_path (str): The file path to the image.

    Returns:
        str: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def extract_address(image_path):
    """
    Extracts the address from an image using the OpenAI API.

    Args:
        image_path (str): The file path to the image.

    Returns:
        str: The extracted address from the image.
    """
    # Get the base64 string of the image
    base64_image = encode_image(image_path)

    # Make the API request to extract the address
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract the address from this image.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
    )

    # Extract the address content
    address = response.choices[0].message.content
    return address



def compare_addresses(address1, address2):
    """
    Compares two addresses to determine if they are identical or similar.

    Args:
        address1 (str): The first address.
        address2 (str): The second address.

    Returns:
        bool: True if the addresses are identical or sufficiently similar, False otherwise.
    """
    # Strip and normalize whitespace
    address1 = address1.strip().lower()
    address2 = address2.strip().lower()

    # Use difflib to compute similarity ratio
    similarity = difflib.SequenceMatcher(None, address1, address2).ratio()

    print(f"Similarity Ratio: {similarity:.2f}")

    # Consider addresses identical if similarity is above a threshold (e.g., 90%)
    return similarity >= 0.65

