from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('form_view', '/')

    config.add_route('view', '/view')
    config.add_static_view('deform_static', 'deform:static/')
    #config.scan('.views')
	
    config.scan()
    return config.make_wsgi_app()
