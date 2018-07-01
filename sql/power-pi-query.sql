select 
  datetime(measure_time, '+10 hours') as measure_time
, printf("%.1f", temperature) as temperature
, printf("%.1f", humidity) as humidity
, sensor_count_1 
, sensor_count_2 
, sensor_count_1 + sensor_count_2 as sensor_count_total
, sensor_1_rate_mwh
, sensor_2_rate_mwh
, sensor_1_rate_mwh + sensor_2_rate_mwh as sensor_rate_mwh_total
from measure_history
order by measure_time desc;



