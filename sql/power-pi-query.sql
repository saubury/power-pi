select 
  datetime(measure_time, '+10 hours') as measure_time
, printf("%.1f", temperature) as temperature
, printf("%.1f", humidity) as humidity
, sensor_count_1 
, sensor_count_2 
, sensor_count_1 + sensor_count_2 as w_hr
from measure_history
order by measure_time desc


-- delete from measure_history


