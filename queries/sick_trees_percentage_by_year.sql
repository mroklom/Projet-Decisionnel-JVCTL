select t.diagnosis_year 
, count(t.id) as number_of_sick_trees
, t2.number_of_diagnosed_trees
, count(t.id) / t2.number_of_diagnosed_trees * 100 as percentage_of_sick
from `jvctl-dataset-1`.diseases d natural join `jvctl-dataset-1`.trees t,
(
select t3.diagnosis_year 
, count(t3.id) as number_of_diagnosed_trees
from `jvctl-dataset-1`.trees t3
where t3.diagnosis_year is not null
group by t3.diagnosis_year
) t2
where d.has_defect = 1
and t.diagnosis_year = t2.diagnosis_year
and t.diagnosis_year is not null
group by t.diagnosis_year
order by percentage_of_sick desc;