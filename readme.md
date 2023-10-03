This script is for extracting all the comments and associated information from a fixed user of a given repository.
It will output a JSON file with the format:

```JSON
{
    id: number;
    body: string;
    diff_hunk: string;
    path: string;
    position: number;
    original_position: number;
    commit_id: string;
    original_commit_id: string;
    html_url: string;
    pull_request_url: string;
}
```

# installation 
create virtual environment
```bash
python3 -m venv venv
```
activate virtual environment
```bash
source venv/bin/activate
```
install requirements
```bash
pip install -r requirements.txt
```

# run
Edit the `main.py` file to change the github access token and the repository name.
```python
# Replace with your info
#-------------------------------------
github_access_token = "<accet_token>"
repo_owner = "jahelsantiago"
repo_name = "frasier-testing"
user_to_extract_comments = "jahelsantiago"
#-------------------------------------
```


Then run the main.py file
```bash
python3 main.py
```

