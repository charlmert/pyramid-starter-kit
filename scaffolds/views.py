from pyramid.view import view_config

# Imports required for deform types
from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf
from colander import Regex

# Imports for deform form/validation handling
from deform import ValidationFailure
from deform import Form

# HTML parsing library
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

# Fetching online documents
import urllib2

# Escaping Html Entities
import HTMLParser

# Deform schema class, contains the form elements
class MySchema(MappingSchema):
    url = SchemaNode(
			String(),
			title='',
			css_class='wiki-input', # Broken
			mask_placeholder='http://en.wikipedia.org/wiki/Wikipedia', # Broken
			validator = Regex('(https|http):\/\/.*.wikipedia.org\/', msg='Invalid wikipedia url was entered'),
			missing_msg = 'Invalid wikipedia url was entered'
	)

# Serving the response against a match for the form_view route configured to /. Renders the index.pt template
@view_config(route_name='form_view', renderer='templates/index.pt')
def form_view(request):
    schema = MySchema()
    myform = Form(schema, buttons=('submit',), action='/view')
	# Rendering with template variables
    return {'form':myform.render()}

# Matching the defined route against POST requests which will render the view.pt template
@view_config(route_name='view', renderer='templates/view.pt')
def my_view(request):
	schema = MySchema()
	myform = Form(schema, buttons=('submit',), action='/view')
	formHtml = myform.render()
	
	# If the submit button was pressed
	if 'submit' in request.POST:
		# Grabbing the form controls
		controls = request.POST.items()
		try:
			# Validating the form
			myform.validate(controls)
		except ValidationFailure, e:
			# Catch the validation exception and render the appropriate message
			return {
					'form':formHtml,
					# Validation seems to be working just the message isn't making it through: "There was a problem with your submission"
					'error_message':' '.join([request.POST['url'], "is not a valid wikipedia url"]),
					'content': None,
					'url': request.POST['url']
				}

		# Performing screen scrapping here
		response = urllib2.urlopen(request.POST['url'])
		html = response.read()
		
		# Converting HTML Entities
		soup = BeautifulSoup(html, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

		# Removing script tags after entities have been converted (XSS Protection)
		[x.extract() for x in soup.findAll('script')]
		
		# Locate the element containing the "table of contents" html
		content = soup.find("div", { "class" : "toc", "id" : "toc" })
		
		# If TOC found build up html string
		if content is not None:
			content = u''.join(unicode(item) for item in content)
			formHtml = None
		else:
			# Else null it
			content = None
		
		# Rendering with template variables
		return {
				'form':formHtml,
				'content':content,
				'url':request.POST['url'],
				'error_message': None,
			}

	# Rendering with template variables
	return {
			'form':formHtml,
			'content':None,
			'url':None,
			'error_message': None,
		}