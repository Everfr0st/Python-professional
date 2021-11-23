from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print(f' Bogotá {bogota_date.strftime("%d/%m/%Y, %H:%M:%S")}')

MX_timezone = pytz.timezone("America/Mexico_City")
MX_date = datetime.now(MX_timezone)
print(f' México {MX_date.strftime("%d/%m/%Y, %H:%M:%S")}')

VZ_timezone = pytz.timezone("America/Caracas")
VZ_date = datetime.now(VZ_timezone)
print(f' Cáracas {VZ_date.strftime("%d/%m/%Y, %H:%M:%S")}')