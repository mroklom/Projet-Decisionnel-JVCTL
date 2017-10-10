select t.addr_sect
, sum(d.collar) / sum(d.has_defect) * 100 as percentage_of_sick_on_collar
, sum(d.tree_crown)/ sum(d.has_defect) * 100 as percentage_of_sick_on_crown
, sum(d.roots)/ sum(d.has_defect) * 100 as percentage_of_sick_on_roots
, sum(d.trunk)/ sum(d.has_defect) * 100 as percentage_of_sick_on_trunk
from `jvctl-dataset-1`.diseases d natural join `jvctl-dataset-1`.trees t
group by t.addr_sect;