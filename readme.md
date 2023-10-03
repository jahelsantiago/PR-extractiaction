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

