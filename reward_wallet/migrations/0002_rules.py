from django.db import migrations


def gen_rules(apps, schema_editor):
    RewardRules = apps.get_model('reward_wallet', 'RewardRules')
    RewardRules.objects.bulk_create(
        [
            RewardRules(entity="hdfc", category="lending", sub_category="term_insurance", conversion_factor=0.2),
            RewardRules(entity="hdfc", category="lending", sub_category="health_insurance", conversion_factor=0.1),
            RewardRules(entity="hdfc", category="lending", sub_category="car_loan", conversion_factor=0.5),
            RewardRules(entity="hdfc", category="lending", sub_category="home_loan", conversion_factor=0.03),
            RewardRules(entity="hdfc", category="lending", sub_category="personal_loan", conversion_factor=0.8),
            RewardRules(entity="icici", category="lending", sub_category="term_insurance", conversion_factor=0.09),
            RewardRules(entity="icici", category="lending", sub_category="health_insurance", conversion_factor=0.07),
            RewardRules(entity="icici", category="lending", sub_category="car_loan", conversion_factor=0.02),
            RewardRules(entity="icici", category="lending", sub_category="home_loan", conversion_factor=0.01),
            RewardRules(entity="icici", category="lending", sub_category="personal_loan", conversion_factor=0.6),
        ]
    )


class Migration(migrations.Migration):
    atomic = False

    operations = [
        migrations.RunPython(gen_rules),
    ]
    dependencies = [
        ("reward_wallet", "0001_initial"),
    ]

