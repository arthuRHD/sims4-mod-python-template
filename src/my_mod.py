from sims4.tuning.instances import TunableSingletonFactory
from sims4.tuning.tunable import TunableTuple

class MyMod(TunableSingletonFactory):
    FACTORY_TUNABLES = {
        'example': TunableTuple(
            description="Example tuning",
            value=10
        )
    }

    def __call__(self):
        return self.example.value

mod_instance = MyMod()
print("My mod value:", mod_instance())
