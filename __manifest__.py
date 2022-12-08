{
    'name': 'Spanish Product',
    'version': '15.0.1.0',
    'category': 'Spanish Product Name',
    'sequence': -1500,
    'summary': 'Spanish Product Name',
    'application': True,
    'depends': [
        'base',
        'product','point_of_sale'

    ],
    'data': [
       'views/product_template.xml',

    ],
    'assets': {
        'web.assets_qweb': [
            'spanish_product/static/src/xml/spanish_product_name.xml',
            'spanish_product/static/src/xml/spanish_product_reciept.xml',
        ],
        'web.assets_backend': [
            'spanish_product/static/src/js/spanish_product_name.js',
            'spanish_product/static/src/js/spanish_product_reciept.js',
        ],
    },
}
