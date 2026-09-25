class CryMeta(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        is_abstract = namespace.get("abstract", False)

        if not is_abstract:
            cry = namespace.get("battle_cry")

            if not isinstance(cry, str) or not cry.strip():
                raise TypeError(
                    f"Класс {name} обязан объявить battle_cry "
                    f"(непустую строку) в своём теле."
                )

        return super().__new__(mcls, name, bases, namespace, **kwargs)