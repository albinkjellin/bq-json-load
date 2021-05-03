import io
import json
from google.cloud import bigquery

#You will need to create your credentials before this and set an enviornment variable:
#export GOOGLE_APPLICATION_CREDENTIALS=""

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "curious-destiny-304908.shipping.shippingaddress"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

data = json.load(open('name_address.json'))

load_job = client.load_table_from_json(
        data,
        table_id,
        location="US",  # Must match the destination dataset location.
        job_config=job_config,
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))
