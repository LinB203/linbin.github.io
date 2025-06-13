# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os

# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }

# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)

# from scholarly import scholarly, ProxyGenerator
# import jsonpickle
# import json
# from datetime import datetime
# import os
# from tqdm import tqdm  # Importing tqdm for the progress bar
# import time

# max_attempts = 100
# wait_seconds = 60  # 10 minutes

# for attempt in range(1, max_attempts + 1):
#     try:
#         # Setup proxy
#         pg = ProxyGenerator()
#         pg.FreeProxies()  # Use free rotating proxies
#         scholarly.use_proxy(pg)
        
#         # Function to add progress
#         def process_progress_bar(total, desc):
#             return tqdm(total=total, desc=desc, ncols=100)
        
#         # Search for author
#         author_id = 'GCOVDKoAAAAJ'
#         print(f"Searching for author with ID: {author_id}")
#         author = scholarly.search_author_id(author_id)
        
#         # Create a progress bar for filling in author details
#         progress = process_progress_bar(1, "Filling author data")
#         scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
#         progress.update(1)  # Update the progress bar after filling details
#         progress.close()
#         print(f"Attempt {attempt} success")
#         break  # Exit loop on first success
#     except Exception as e:
#         print(f"Attempt {attempt} failed with error: {e}")
#         time.sleep(wait_seconds)
# else:
#     print("All 100 attempts failed.")

# # Log the details of the author
# name = author['name']
# author['updated'] = str(datetime.now())

# # Format publications as a dictionary
# author['publications'] = {v['author_pub_id']: v for v in author['publications']}

# # Display author information in a formatted manner
# print("Author details have been filled.")
# print(json.dumps(author, indent=2))

# # Create the results directory if it doesn't exist
# os.makedirs('results', exist_ok=True)

# # Save the author's data to a JSON file
# print("Saving author data to 'gs_data.json'...")
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# # Create Shields.io data for citation count
# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }

# # Save Shields.io data
# print("Saving citation count to 'gs_data_shieldsio.json'...")
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)

# print("Process completed successfully.")
from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

max_attempts = 1000
wait_seconds = 1 

for attempt in range(1, max_attempts + 1):
    try:
        print(f"Attempt {attempt}:")
        # Setup proxy
        pg = ProxyGenerator()
        pg.FreeProxies()  # Use free rotating proxies
        scholarly.use_proxy(pg)
        
        author: dict = scholarly.search_author_id('GCOVDKoAAAAJ')
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        print(f"Attempt {attempt} success")
        break  # Exit loop on first success
    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e}")
        time.sleep(wait_seconds)
else:
    print("All 100 attempts failed.")

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
