drop table if exists measure_history ;

create table measure_history(
  measure_history_id integer primary key autoincrement
, measure_time timestamp not null default current_timestamp
, temperature number
, humidity number
, sensor_count_1 integer
, sensor_count_2 integer
);
