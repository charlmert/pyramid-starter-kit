### Install Pyramid + Deps
- When using virtual environments, install appropriately
- Install Pyramid for Python 2.7 http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter
'''bash
easy_install "pyramid==1.5.2"
easy_install "deform==2.0a2"
easy_install "beautifulsoup==3.2.1"
cd pyramid-starter-kit
/path/to/env/pserve pyramid-starter-kit/development.ini --reload
- Visit http://localhost:6543/ in your browser, preferably google chrome.

### To demonstrate the major features test with the following urls
- http://en.wikipedia.org/wiki/Wikipedia (Valid URL + Table Of Contents Displayed)
- http://www.google.com (Invalid URL)
- http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost (No Table Of Contents)

### Unit Testing
- Unit Tests ... still to come ... in the not sooo distant future.
- python.exe setup.py test -q