from django.db import migrations


def gen_rules(apps, schema_editor):
    BBPSRepaymentSchedule = apps.get_model('payments', 'BBPSRepaymentSchedule')
    BBPSRepaymentSchedule.objects.bulk_create(
        [
            BBPSRepaymentSchedule(lender_id="123", account_id=1, year="2022", month="9",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6000, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=1, year="2022", month="10",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6000, outstanding_amount=60000),
            BBPSRepaymentSchedule(lender_id="123", account_id=1, year="2022", month="11",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=9000, outstanding_amount=120000),
            BBPSRepaymentSchedule(lender_id="123", account_id=1, year="2022", month="12",
                                  status="DUE", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6000, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=2, year="2022", month="9",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6000, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=2, year="2022", month="10",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=8500, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=2, year="2022", month="11",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6020, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=2, year="2022", month="12",
                                  status="DUE", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6300, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=3, year="2022", month="9",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6090, outstanding_amount=30000),
            BBPSRepaymentSchedule(lender_id="123", account_id=3, year="2022", month="10",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6000, outstanding_amount=30100),
            BBPSRepaymentSchedule(lender_id="123", account_id=3, year="2022", month="11",
                                  status="PAID", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6100, outstanding_amount=30700),
            BBPSRepaymentSchedule(lender_id="123", account_id=3, year="2022", month="12",
                                  status="DUE", due_date="2022-10-01", principal_outstanding_amount=1200,
                                  foreclosure_amount=6500, outstanding_amount=30100),
        ]
    )


class Migration(migrations.Migration):
    atomic = False

    operations = [
        migrations.RunPython(gen_rules),
    ]
    dependencies = [
        ("payments", "0002_remove_bbpsrepaymentschedule_loan_id_and_more"),
    ]
