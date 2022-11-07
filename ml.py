import csv 
import json 

# Open the CSV
f = open( 'english-hindi-dictionary/English-Hindi Dictionary.csv' , 'rU' )
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader( f, fieldnames = ( "Word" , "Meaning" ))
# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ])
print ( "JSON parsed!" )
# Save the JSON
f = open( 'ml.json' , 'w' )
f.write(out)
print ( "JSON saved!" )