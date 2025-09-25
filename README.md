 # 🌍 Ubuntu-Inspired Image Fetcher
*Created by **Abrha Gebrehiwet***  

> *"I am because we are"*  

The **Ubuntu Image Fetcher** is a mindful Python script that connects to the global community of the internet, **respectfully fetches shared images**, and organizes them for future appreciation.

This project is inspired by the **Ubuntu philosophy**:
- 🤝 **Community**: Connects with the wider web  
- 🙏 **Respect**: Handles errors gracefully  
- 📤 **Sharing**: Organizes downloaded images for future use  
- ⚡ **Practicality**: Provides a simple, useful tool  

---

## ✨ Features
✅ **Fetch single or multiple images** from URLs  
📂 **Automatic directory creation** → Saves images in a `Fetched_Images/` folder  
🖼️ **Smart file naming** → Extracts filenames from URLs or generates defaults  
🔐 **Image validation** → Checks headers to confirm files are actual images  
⚡ **Duplicate prevention** → Skips files already downloaded using file hashes  
🛡️ **Error handling** → Gracefully manages network issues without crashing  
🤗 **Server respect** → Uses polite `User-Agent` headers  

---

## 📦 Requirements
- 🐍 **Python 3.7+**
- Required Python Library:
  - `requests` (for downloading images)

Install dependencies with:
```bash
pip install requests

---

▶️ Usage

1️⃣ Clone or Download this repository:
git clone https://github.com/Abricos-gt/ubuntu-image-fetcher.git
cd ubuntu-image-fetcher


---

2️⃣ Run the script:
python ubuntu_image_fetcher.py

---

3️⃣ Enter one or more image URLs (separated by spaces) when prompted.

🖥️ Example Run
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (separated by spaces): 
https://upload.wikimedia.org/wikipedia/commons/8/87/Ubuntu_Wallpaper.png https://placekitten.com/300/300

✓ Successfully fetched: Ubuntu_Wallpaper.png
✓ Image saved to Fetched_Images/Ubuntu_Wallpaper.png
✓ Successfully fetched: 300
✓ Image saved to Fetched_Images/300

Connection strengthened. Community enriched.


---

📂 Project Structure

ubuntu-image-fetcher/
│
├─ ubuntu_image_fetcher.py   # Main script
├─ Fetched_Images/           # Downloaded images saved here
└─ README.md                 # Documentation (this file)


---

🌟 Ubuntu Spirit

This project embodies the Ubuntu philosophy:

🤝 Community → Sharing knowledge and resources responsibly

🙏 Respect → Handling errors and servers with care

📤 Sharing → Organizing files for easy reuse

⚡ Practicality → A tool built to serve real needs

"Connection strengthened. Community enriched."

---

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request with improvements or new features.

📜 License

This project is licensed under the MIT License

