from CheckId import is_valid_id_card
from utils import extract_address, compare_addresses

# Define image paths
input_image_1 = "bz1.jpg"
input_image_2 = "facture.jpg"
template_image_path = "cin1.jpg"

if __name__ == "__main__":
    # Step 1: Validate the ID card
    if is_valid_id_card(input_image_1, template_image_path, threshold=0.7):  # Adjust threshold as needed
        print("The input image is a valid ID card.")
        
        # Step 2: Extract the address
        try:
            address_cin = extract_address(input_image_1)
            print("Extracted Address from CIN:", address_cin)

            address_facture = extract_address(input_image_2)
            print("Extracted Address from facture:", address_facture)

            if compare_addresses(address_cin, address_facture):
                print("The addresses are identical or sufficiently similar.")
            else:
                print("The addresses are not identical.")

        except Exception as e:
            print("An error occurred while extracting the address:", e)
    else:
        print("The input image is NOT a valid ID card. Please provide a real card.")
