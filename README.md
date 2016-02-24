### Install Pyramid + Deps
- When using virtual environments, install appropriately
- Install (Ubuntu 12.04.3) Pyramid for Python 2.7 http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter

```shell
apt-get install python-setuptools build-essential
$EASY_INSTALL=$(which easy_install)
$PSERVE=$(which pserve)
$EASY_INSTALL "pyramid==1.5.2"
$EASY_INSTALL "deform==2.0a2"
$EASY_INSTALL "beautifulsoup==3.2.1"
$EASY_INSTALL "WebTest"
$EASY_INSTALL "pyramid-debugtoolbar"
$EASY_INSTALL "pyramid-chameleon"
$EASY_INSTALL "BeautifulSoup"
export PYTHONPATH=$(pwd)/pyramid-starter-kit
$PSERVE pyramid-starter-kit/development.ini --reload
```

- Visit [http://localhost:6543/](http://localhost:6543/) in your browser, preferably google chrome.

### Test URL's

To demonstrate the major features test with the following urls

- http://en.wikipedia.org/wiki/Wikipedia (Valid URL + Table Of Contents Displayed)
- http://www.google.com (Invalid URL)
- http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost (No Table Of Contents)

These url's are used in the functional tests as well.

### Unit Testing

Requires [WebTest](http://webtest.pythonpaste.org/en/latest/) which should have been installed @ step 1, Install Pyramid

```shell
/path/to/env/python pyramid-starter-kit/setup.py test -q
```
