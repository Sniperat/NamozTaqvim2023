from django.core.management.base import BaseCommand
from ._base import ParserBase
from bs4 import BeautifulSoup
from main.models import TimeModel, RegionModel
import requests
from datetime import datetime, timedelta
print(datetime.now())
class Command(ParserBase):

    def handle(self, *args, **kwargs):
        res = requests.get("https://islom.uz/", 'html.parser')
        soup = BeautifulSoup(res.text)
        soup.text
        times = soup.find_all("div", {"class": "p_clock"})
        for i in times:
            print(i.text)
        for region in RegionModel.objects.all():
            if region.solat_times != None:
                time_model = TimeModel.objects.get(id=region.solat_times.id)    
            else:
                time_model = TimeModel()
            print(region.name)
            bomdod = datetime(year=2023, month=1, day=1, hour=int(times[0].text.split(':')[0]), 
                              minute=int(times[0].text.split(':')[1]), second=00
                            )+ timedelta(minutes=region.time_on_minute-5)            
            print(bomdod)
            time_model.bomdod = bomdod
            quyosh = datetime(year=2023, month=1, day=1, hour=int(times[1].text.split(':')[0]), 
                              minute=int(times[1].text.split(':')[1]), second=00
                            ) + timedelta(minutes=region.time_on_minute)
            time_model.quyosh = quyosh
            peshin = datetime(year=2023, month=1, day=1, hour=int(times[2].text.split(':')[0]), 
                              minute=int(times[2].text.split(':')[1]), second=00
                            ) + timedelta(minutes=region.time_on_minute)
            time_model.peshin = peshin
            asr = datetime(year=2023, month=1, day=1, hour=int(times[3].text.split(':')[0]), 
                           minute=int(times[3].text.split(':')[1]), second=00
                            ) + timedelta(minutes=region.time_on_minute)
            time_model.asr = asr
            shom = datetime(year=2023, month=1, day=1, hour=int(times[4].text.split(':')[0]), 
                            minute=int(times[4].text.split(':')[1]), second=00
                            ) + timedelta(minutes=region.time_on_minute+5)
            time_model.shom = shom
            xufton = datetime(year=2023, month=1, day=1, hour=int(times[5].text.split(':')[0]), 
                              minute=int(times[5].text.split(':')[1]), second=00
                            ) + timedelta(minutes=region.time_on_minute)
            time_model.xufton = xufton

            time_model.save()
            region.solat_times = time_model
            region.save()
