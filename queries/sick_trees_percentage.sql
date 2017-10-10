SELECT t.species
, count(d.has_defect) as number_of_sick_trees
, t2.number_of_trees
, count(d.has_defect) / t2.number_of_trees * 100 as percentage_of_sick
FROM `jvctl-dataset-1`.diseases d,`jvctl-dataset-1`.trees t,
(
select species
, count(t3.id) as number_of_trees
from `jvctl-dataset-1`.trees t3
where t3.species is not null
group by t3.species
order by number_of_trees
) t2
where d.id = t.id
and t2.species = t.species
and t.species is not null
and d.has_defect = 1
group by t.species
order by percentage_of_sick desc;