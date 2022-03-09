# Dependencies
- Python 3.9.7 
- Conda 4.11.0
- Django 2.2.26
- Pillow 9.0.1

# Environment setup (first time only)
- Install [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- `conda create -n coursemate python=3.9`
- `conda activate coursemate`
- `pip install django==2.2.26`
- `pip install pillow==9.0.1`
## Environment checks
- `python --version`
- `python`
```python
import django
django.get_version()
exit()
```

# Activate (run every time)
- `conda activate coursemate`

# Run Django local server
- `cd` to file location
- `python manage.py runserver` (access at http://127.0.0.1:8000/)
- `python manage.py 127.0.0.1:5555` (also specifying IP and TCP port)
