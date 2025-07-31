# Get filename input and normalize it (lowercase + strip whitespace)
folder_name = input("File name: ").lower().strip()

# Check file extension and output corresponding MIME type
if folder_name.endswith(".gif"):
    print("image/gif")  # GIF image format
elif folder_name.endswith((".jpg", ".jpeg")):  # Tuple of possible JPEG extensions
    print("image/jpeg")  # JPEG image format
elif folder_name.endswith(".png"):
    print("image/png")   # PNG image format
elif folder_name.endswith(".pdf"):
    print("application/pdf")  # PDF document format
elif folder_name.endswith(".txt"):
    print("text/plain")  # Plain text format
elif folder_name.endswith(".zip"):
    print("application/zip")  # ZIP archive format
else:
    print("application/octet-stream")  # Default for unknown file types