
This script appends EXIF information to png & jpg files




##### LOADING EXAMPLE

REQUIRES USER ENVIRONMENTAL VARIABLE: 'SCRIPTS' for location of file

```python
    # Append metadata to figure
    if os.path.isdir(f"{os.environ['SCRIPTS']}"):
        sys.path.append(f"{os.environ['SCRIPTS']}")
        from plot_EXIF import *

        add_exif(f"{path_output}{plot_filename}")
```
