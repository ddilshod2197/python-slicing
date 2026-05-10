class Malumot:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"

malumot = Malumot(ism="Ali", yosh=22)
print(malumot.info())
```

```python
class Malumot:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __str__(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"

malumot = Malumot(ism="Ali", yosh=22)
print(malumot)
```

```python
class Malumot:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __repr__(self):
        return f"Malumot('{self.ism}', {self.yosh})"

malumot = Malumot(ism="Ali", yosh=22)
print(malumot)
