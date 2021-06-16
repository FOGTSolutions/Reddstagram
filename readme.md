# Reddstagram

A python library for automated Reddit subforum scraping and uploading to Instagram.

Developed by FOGT Solutions (c) 2021

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Reddstagram.

```bash
pip install reddstagram
```

## Usage

```python
import reddstagram

#necessary arguments
reddstagram.auto(USER="", PASS="", SUBNAME="", ID="", SECRET="", AGENT="")

#optional arguments
reddstagram.auto(USER="", PASS="", SUBNAME="", ID="", SECRET="", AGENT="", LIMIT=0, DELAY=0, CAPTION="")
```

* USER - Your Instagram username.
* PASS - Your Instagram password.
* SUBNAME - Subreddit name to scrape from.
* ID - Your Reddit developer app id.
* SECRET - Your Reddit developer app secret.
* AGENT - Your Reddit developer app useragent.
* LIMIT - Maximum images to scrape.
* DELAY - Delay between uploads.
* CAPTION - Caption of the Instagram post.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
