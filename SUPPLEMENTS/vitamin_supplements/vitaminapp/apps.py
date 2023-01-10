from django.apps import AppConfig


class VitaminappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vitaminapp'

    def ready(self):
        import pandas as pd
        from django.conf import settings
        from sqlalchemy import create_engine
        from .models import SunshineAvailability, Zones

        xls = pd.ExcelFile('vitaminapp/resources/Vitamin D (1).xlsx')
        df1 = pd.read_excel(xls, 'Vitamin D Strength')
        df2 = pd.read_excel(xls, 'Zones')
        df1.columns = ["ZoneID", "Month", "Strength"]
        df2.columns = ["ZoneID", "LatitudeMin", "LatitudeMax", "NorthSouth"]
        df2.set_index("ZoneID", inplace=True)
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        database_url = 'postgresql://root:root@localhost:5432/postgres'.format(
            user=user,
            password=password,
            database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)

        df1.to_sql('Sunshine_Availability', con=engine, if_exists='append')
        df2.to_sql('Zones', con=engine, if_exists='append')
