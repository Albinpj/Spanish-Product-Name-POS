odoo.define('spanish_product.spanish_receipt_temp', function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_fields('product.product', 'spanish_name');

var _super_orderline = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    export_for_printing: function() {
        var line = _super_orderline.export_for_printing.apply(this,arguments);
        line.spanish_name = this.get_product().spanish_name;
        return line;

    },
});

});
