from flask import Flask, render_template
import json
import requests
import sqlite3
import unittest

app = Flask(__name__)


@app.route('/api1/purchaseReport')
def getPurchaseReport():
    purchases = purchaseService.getPurchases()
    csvPurchases = convertJsonArrayToCsv(purchases)
    return csvPurchases


def convertJsonArrayToCsv(jsonArray):
    csv = ""
    for item in jsonArray:
        for val in item.values():
            csv = csv + val + ','
        csv = csv[:-1] + '\n'
    return csv


class PurchaseService():
    def getPurchases(self):
        resp = requests.get('http://127.0.0.1:5002/api2/purchases')
        if resp.status_code != 200:
            raise Exception("Failed to get purchases.")
        return json.loads(resp.content)


class UnitTests(unittest.TestCase):

    def test_convertJsonArrayToCsv(self):
        jsonArray = json.loads('[{"foo":"bar"},{"zoo":"foobar"}]')
        expectedCsv = 'bar\nfoobar\n'
        self.assertEqual(convertJsonArrayToCsv(jsonArray), expectedCsv)


if __name__ == "__main__":
    # Unit test.
    # unittest.main(exit=False)

    global purchaseService
    purchaseService = PurchaseService()

    app.run(host="0.0.0.0", port=5001)
