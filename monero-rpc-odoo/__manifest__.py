# -*- coding: utf-8 -*-
{
    "name": "moneroodoo",
    "summary": "Allows you to accept Monero Payments",
    "author": "Monero Integrations",
    "website": "https://monerointegrations.com/",
    # Categories can be used to filter modules in modules listing
    # for the full list
    "category": "Accounting",
    "version": "0.2",
    # any module necessary for this one to work correctly
    "depends": [
        "website_sale",
        "website_payment",
        "website",
        "payment_transfer",
        "payment",
        "base_setup",
        "web",
    ],
    # always loaded
    "data": [
        "views/scheduler.xml",
        "views/monero_acquirer_form.xml",
        "views/monero_payment_confirmation.xml",
        "data/currency.xml",
        "data/monero_xmr_payment_acquirer.xml",
    ],
    # only loaded in demonstration mode
    # TODO add demo data
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
    "classifiers": ["License :: OSI Approved :: MIT License"],
}