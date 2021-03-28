# InstagramPost 📷

<p align="center">
    <img src="img/photo.jpeg" width="550" title="Instagram Post Image">
</p>
<p>This bot allows you to post photos to your Instagram account through your browser, just by editing 5 lines of code.</p>

## Installation
<ol>
    <li><a href="https://github.com/leandrobove/instagram-post/archive/refs/heads/main.zip" target="_blank">Click here</a> and download files or clone this repository.</li>
    <li>Install all requirements running</li>
</ol>

```cmd
python -m pip install -r requirements.txt
```

## Usage

### 1 - Download chromedriver.exe
<p>Download the version of chromedriver compatible with your browser and operating system <a href="https://chromedriver.chromium.org/downloads" target="_blank">click here</a> and then paste on <b>/chromedriver</b> folder.</p>

### 2 - Open <b>config.py</b> file and change with your Instagram account credentials.


```python
username = "YOUR_INSTAGRAM_USERNAME"
password = "YOUR_INSTAGRAM_PASSWORD"

photo_full_path = "Your photo full path file here." # Example: C:\\User\\Images\\photo.jpg
post_description = "Your post description here." # Example: I can post on Instagram without a cell phone ;)

user_chrome_data_path = "This is the path where Chrome data will be stored" # Example: C:\\my_main_project_folder\\user_data_chrome
headless = False # Define if Chrome window will apear or no. Set value True or False
```

### 3 - Open cmd.exe and run the code below.

```cmd
python InstagramPost.py
```

## Contributing
<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

## License
[MIT](https://choosealicense.com/licenses/mit/)

<p>Copyright (c) [year] [fullname]</p>

<p>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:</p>

<p>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.</p>