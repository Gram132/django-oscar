import datetime

from django.test import TestCase
from django.utils.timezone import now

from oscar.apps.order import reports


class TestOrderReportGenerator(TestCase):
    def test_generate_csv_no_filter(self):
        generator = reports.OrderReportGenerator(formatter="CSV")
        generator.generate()

    def test_generate_csv_start_and_end_date(self):
        start_date = now() - datetime.timedelta(days=28)
        end_date = now() + datetime.timedelta(days=28)

        generator = reports.OrderReportGenerator(
            start_date=start_date, end_date=end_date, formatter="CSV"
        )
        generator.generate()
