# Shardshotgun Extractor

This Python script processes a given file and extracts data based on specific patterns. The extracted data is then written to an Excel file.

## Requirements

- Python 3.6 or higher
- pandas library

## Usage

To use this script, you need to provide the path to the file you want to process as a command-line argument:

```bash
python shardshotgun_extractor.py <file_path>
```

Here's a sample input file
```
running on Pod 20 Shard twentyone
         customer_root_id         |      customer_name       |         legal_entity_id          |         legal_entity_name         |     erp      
----------------------------------+--------------------------+----------------------------------+-----------------------------------+--------------
 dfsdfsdf | Canada a Centre      | asadasdsd | Canada Games Centre Society       | sage300

(8 rows)

running on Pod 20 Shard twentytwo
         customer_root_id         |          customer_name          |         legal_entity_id          |               legal_entity_name                |     erp      
----------------------------------+---------------------------------+----------------------------------+------------------------------------------------+--------------

```