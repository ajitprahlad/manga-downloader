# 📚 Manga Downloader

This Python script allows you to easily download manga chapters from the website `manhwatoon.com`. It fetches the images from each chapter and saves them directly to your desktop, organizing them by manga title and chapter number. 🎉

![image](https://github.com/user-attachments/assets/850fbc32-9434-4b1a-8696-b0f656f44a19)


## ✨ Features

- **🚀 Concurrent Downloads:** The script uses multithreading to download multiple images at once, speeding up the process.
- **📁 Automatic Folder Creation:** Automatically creates folders on your desktop based on the manga title and chapter number, ensuring your downloads are neatly organized.
- **⚠️ Error Handling:** Checks the status of each image download and logs any failures to ensure you don't miss a page.

## 🛠️ Prerequisites

Make sure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`

Install these libraries using pip:

```bash
pip install requests beautifulsoup4
```

## 📝 Usage

1. Run the Script: Execute the script in your Python environment.

```bash
python manga_downloader.py
```

2. Input the Manga URL: When prompted, enter the URL of the manga you want to download. The script will handle the rest. 🌐

3. Wait for Downloads: The script will start downloading all chapters of the manga, saving the images in the appropriate folders on your desktop. ⏳

## 🛡️ How It Works
- ***🍪 Cookies and Headers***: The script includes necessary cookies and headers to mimic a legitimate browser request.
- ***📜 Chapter Processing:*** For each chapter, the script fetches the HTML, parses it with BeautifulSoup, and extracts image URLs.
- ***🖼️ Image Downloading***: Images are downloaded concurrently, with a limit of five simultaneous downloads to prevent overloading the server.

## 🔍 Example
- If you input the URL https://www.manhwatoon.com/manga/re-monarch/, the script will download all available chapters of "Re: Monarch" and save the images in folders like Desktop/Re Monarch/Chapter 1/.

## ⚠️ Note
- **Website Changes:** The script relies on the current structure of manhwatoon.com. If the website changes its layout or structure, the script may need adjustments.
- **🔒 Legal Disclaimer:** Ensure that you have the right to download the manga from the website and respect copyright laws. This script is intended for educational purposes only.

## 📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.
