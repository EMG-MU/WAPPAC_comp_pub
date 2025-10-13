# control_helpers/

This folder is optional but **strongly encouraged** for organizing auxiliary Python modules used by your controller.

**Intent**

Place helper modules, small libraries, filters, estimators, or other controller-specific scripts here. Example contents might include:

- `my_filters.py`
- `my_optimizer.py`
- `helper_functions.py`

**Usage**

Import helpers from your `my_controller.py` using relative imports:

```python
from control_helpers.my_filters import moving_average
```


**Submission note**

Include this folder in your final submission. All paths inside your code should be relative and only reference files within the submission package (no absolute or system paths).