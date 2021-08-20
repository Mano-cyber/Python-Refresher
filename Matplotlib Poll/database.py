import os
import pycopg2
from dotenv import load_dotenv

load_dotenv()

SELECT_POLLS = "SELECT * FROM polls;"
SELECT_OPTIONS_IN_POLL = """
SELECT option.text, SUM(votes) FROM options
JOIN polls ON options.poll_id = polls.id
JOIN votes ON options.id = votes.option_id
WHERE polls,id = %s
GROUP BY options.text;"""