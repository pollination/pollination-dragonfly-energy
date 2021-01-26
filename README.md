# Pollination Dragonfly Energy plugin.

The dragonfly-energy plugin adds daylight simulation functions to Pollination.

## Dependencies:

- `dragonfly-energy` Python package. [PyPI](https://pypi.org/project/dragonfly-energy/), [source](https://github.com/ladybug-tools/dragonfly-energy)

## Load as Queenbee plugin

Install the package using `pip install .`. Then you can use `queenbee_dsl` to load the
package as a Queenbee Plugin.

```python
from queenbee_dsl.package import load

plugin = load(python_package)
print(plugin.yaml())
```
