import math
from decimal import Decimal

print([f for f in dir(Decimal()) if not f.startswith("__")and not callable(f)])
print([f for f in dir(math) if not f.startswith("__") and not callable(f)])
