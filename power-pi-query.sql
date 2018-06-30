select *
from measure_history

select 
  datetime(measure_time, '+10 hours') as measure_time
, printf("%.2f", temperature) as temperature
, printf("%.2f", humidity) as humidity
, sensor_count_1 + sensor_count_2 as w_hr
from measure_history


delete from measure_history

drop table if exists measure_history ;

create table measure_history(
  measure_history_id integer primary key autoincrement
, measure_time timestamp not null default current_timestamp
, temperature number
, humidity number
, sensor_count_1 integer
, sensor_count_2 integer
);
