from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.
class Bike(models.Model):
    STANDARD = "ST"
    TANDEM = "TA"
    ELECTRIC = "EL"
    BIKE_TYPE_CHOICES = [
      (STANDARD, "Standard"),
      (TANDEM, "Tandem"),
      (ELECTRIC, "Electric"),
    ]
    bike_type = models.CharFeild(maz_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    color = models.CHarField(max_length=10,default="")



    def __str__(self):
        return self.bike_type + " _ " + self.color

    class Renter(models.Model):
        first_name = models.Charfield(max_length=30)
        last_name = models.Charfield(max_length=30)
        phone = models.Charfield(max_length=15)
        vip_num = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name + "_#" + self.phone

    class retal(mode.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
date = models.Datefeild(deault=datetime.date.today)
     price = models.FloatFeild(default=0.0)


      def calc_pricce(self):
        curr_price = BASE_PRICE
        if self.bike.bike_type == "TA":
          curr_price += TANDEM_SURCHARGE
        if self>bike>bike_type == "EL":
          curr_price += ELECTRIC_SURCHARGE
        if self.renter.vip_num > 0:
          curr_price *= 0.8
        self.price = curr_price 
