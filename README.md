### Install Pyramid + Deps
- When using virtual environments, install appropriately
- Install (Ubuntu 12.04.3) Pyramid for Python 2.7 http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter

```shell
git clone git@github.com:charlmert/pyramid-starter-kit.git
cd pyramid-starter-kit
python setup.py develop
sudo apt-get install python-setuptools build-essential
sudo apt-get install python-iso8601 python-sqlalchemy 
pip install "pyramid==1.5.2"
pip install "deform==2.0a2"
pip install "beautifulsoup==3.2.1"
pip install "WebTest"
pip install "pyramid-debugtoolbar"
pip install "pyramid-chameleon"
pip install "BeautifulSoup"
pip install "Scaffold"
pserve development.ini --reload
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
