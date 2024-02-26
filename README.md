# jinja2loader

YamlLoader is a template loader for jinja2 template framework.
It loads templates from yaml-files. Useful when you need to
store many small templates in one file.

## Install

```bash
pip install jinja2yaml
```

### Related packages:

- [Collection of utils for jinja2](https://github.com/vd2org/jinja2utils)

#### Usage:

```yaml
# templates.yaml
home:
  welcome: |
    Welcome, {{username}}!
  goodbye: |
    Goodbye, {{username}}!
```

```python
# main.py
from jinja2 import Environment
from jinja2yaml import YamlLoader

jinja = Environment(loader=YamlLoader('templates.yaml'))

username = 'John Doe'
template1 = jinja.get_template('home/welcome')
rendered1 = template1.render(username=username)
print(rendered1)  # Welcome, John Doe!

template2 = jinja.get_template('home/goodbye')
rendered2 = template2.render(username=username)
print(rendered2)  # Goodbye, John Doe!
``` 
