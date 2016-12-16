from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('jquery_loadmask_spin', 'resources')

spin = Resource(library, 'js/spin.js', minified='js/spin.min.js')

jquery_loadmask_js = Resource(
    library, 'js/jquery.loadmask.spin.js',
    minified='js/jquery.loadmask.spin.min.js',
    minifier='jsmin',
    depends=[spin, jquery,])
jquery_loadmask_css = Resource(
    library, 'css/jquery.loadmask.spin.css',
    minified='css/jquery.loadmask.spin.min.css',
    minifier='cssmin')
jquery_loadmask = Group([jquery_loadmask_css, jquery_loadmask_js])
