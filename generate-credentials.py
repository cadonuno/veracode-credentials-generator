import sys
import os
import webbrowser

YES = "y"
NO = 'n'

def open_api_credentials_generator():
    webbrowser.open("[REPLACE: SAML URL TO LOG INTO VERACODE (or analysis center URL if not using SAML)]", new=0, autoraise=True)
    input("Press ENTER once you are logged into Veracode")
    webbrowser.open("https://analysiscenter.veracode.[REPLACE: YOUR VERACODE INSTANCE URL (EU/COM/US)]/auth/index.jsp#APICredentialsGenerator", new=0, autoraise=True)

def get_credentials_from_input():
    input("When the page loads, press 'Generate API Credentials'.")
    api_id = input("Insert the API ID:")
    api_key = input("Insert the API Secret Key:")
    return api_id, api_key

def save_credentials_file(api_id, api_key):
    file_content = f"""
    [default]
    veracode_api_key_id = {api_id}
    veracode_api_key_secret = {api_key}
    """
    directory = os.path.join(os.path.expanduser("~"), ".veracode")
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "credentials")
    with open(file_path, "w") as credentials_file:
        credentials_file.write(file_content)
        print("Setup complete.")

def request_input(message):
    value = ""
    while not value in [YES, NO]:
        value = input(message)
        if value:
            value = value.lower()
        else:
            value = ""
    return value == YES

def main():
    if request_input("Do you need to generate your API credentials (Y/N)?"):
        open_api_credentials_generator()
        api_id, api_key = get_credentials_from_input()
        save_credentials_file(api_id, api_key)

    webbrowser.open("[REPLACE: INTERNAL DOCS URL]", new=0, autoraise=True)
    input("Our internal documentation was opened in your browser.")
    
if __name__ == "__main__":
    main()
