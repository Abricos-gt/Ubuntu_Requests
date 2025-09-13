import requests
import os
import hashlib
from urllib.parse import urlparse

def sanitize_filename(filename):
    """
    Ensure filename is safe and usable.
    If the URL has no filename, provide a default one.
    """
    if not filename:
        filename = "downloaded_image.jpg"
    return filename.replace("/", "_").replace("\\", "_")

def get_file_hash(content):
    """
    Generate a unique hash of the image content
    to prevent duplicate downloads.
    """
    return hashlib.sha256(content).hexdigest()

def fetch_image(url, saved_hashes):
    try:
        # Add headers to respect the server
        headers = {"User-Agent": "Ubuntu-Image-Fetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for HTTP issues

        # Precaution: Ensure it's really an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Prevent duplicates by checking file hash
        file_hash = get_file_hash(response.content)
        if file_hash in saved_hashes:
            print(f"✗ Skipped duplicate: {url}")
            return
        saved_hashes.add(file_hash)

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = sanitize_filename(os.path.basename(parsed_url.path))
        filepath = os.path.join("Fetched_Images", filename)

        # If filename already exists, create a new one
        counter = 1
        while os.path.exists(filepath):
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join("Fetched_Images", filename)
            counter += 1

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory for saving images
    os.makedirs("Fetched_Images", exist_ok=True)

    # Accept multiple URLs at once
    urls = input("Please enter image URLs (separated by spaces): ").split()

    # Keep track of already downloaded images
    saved_hashes = set()

    # Process each URL
    for url in urls:
        fetch_image(url.strip(), saved_hashes)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
