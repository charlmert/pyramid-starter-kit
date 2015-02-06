import unittest

from pyramid import testing
from collections import OrderedDict

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        
        self.assertEqual(info['error_message'], None)
        self.assertEqual(info['content'], None)
        self.assertEqual(info['url'], None)
        self.assertTrue('id="deform"' in info['form'])

    def test_form_view(self):
        from .views import form_view
        request = testing.DummyRequest()
        info = form_view(request)
        
        self.assertTrue('id="deform"' in info['form'])
        
# Functional Tests, (Requires WebTest http://webtest.pythonpaste.org/en/latest/)
class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from scaffolds import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_expected_responses(self):
        # Testing with google.com
        res = self.testapp.post(
            '/view', 
            OrderedDict([
                ('url', 'www.google.com'),
                ('submit', 'doPost')
            ]),
            status=200)
        
        self.assertTrue('www.google.com is not a valid wikipedia url' in res.body)

        # Testing with http://en.wikipedia.org/wiki/Wikipedia
        res = self.testapp.post(
            '/view', 
            OrderedDict([
                ('url', 'http://en.wikipedia.org/wiki/Wikipedia'),
                ('submit', 'doPost')
            ]),
            status=200)

        self.assertTrue('<p class="lead"><br/>The table of contents for <span class="font-normal"><a href="http://en.wikipedia.org/wiki/Wikipedia">http://en.wikipedia.org/wiki/Wikipedia</a></span></p>' in res.body)
        
        # Testing with http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost
        res = self.testapp.post(
            '/view', 
            OrderedDict([
                ('url', 'http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost'),
                ('submit', 'doPost')
            ]),
            status=200)

        self.assertTrue('<p class="lead">The wikipedia page @ <a href="http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost">http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost</a> didn\'t contain any identifiable table of contents. Try another URL</p>' in res.body)