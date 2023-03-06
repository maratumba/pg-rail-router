import overpy
api = overpy.Overpass()

q = """
/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[timeout:1200];
// gather results
(
  // query part for: “railway=rail”
  node["railway"="rail"];
  way["railway"="rail"];
  relation["railway"="rail"];
);
// print results
out body;
>;
out skel qt;
"""

result = api.query(q)