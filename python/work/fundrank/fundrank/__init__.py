from pyramid.config import Configurator

# 项目入口
# When you invoke the pserve development.ini command, the main function is executed.
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    #  include Jinja2 templating bindings so that we can use renderers with the .jinja2 extension within our project.
    config.include('pyramid_jinja2')

    # include the the package models using a dotted Python path. 
    config.include('.models')

    # include the routes module using a dotted Python path.
    config.include('.routes')

    # recursively scan our package, looking for @view_config and other special decorators. 
    # When it finds a @view_config decorator, a view configuration will be registered, allowing one of our application URLs to be mapped to some code.
    config.scan()

    return config.make_wsgi_app()
