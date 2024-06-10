import json
import os
from sims4.tuning.instances import TunableSingletonFactory
from sims4.tuning.tunable import TunableTuple
from interactions.base.super_interaction import SuperInteraction


def get_localized_string(key):
    locale = services.get_instance_manager(sims4.resources.Types.LANGUAGE).get_current_locale()
    localized_strings_file = os.path.join('src', 'locale', f'{locale}.json')
    
    try:
        with open(localized_strings_file, 'r', encoding='utf-8') as file:
            localized_strings = json.load(file)
            return localized_strings.get(key, f"String not found for key: {key}")
    except FileNotFoundError:
        return f"Localization file not found for locale: {locale}"

class CustomInteraction(SuperInteraction):
    INSTANCE_TUNABLES = {}

    def _run_interaction_gen(self, timeline):
        greeting = get_localized_string('my_mod.greeting')
        self.sim.sim_info.add_buff('buff_Happy')
        print(greeting)
        return True


class MyMod(TunableSingletonFactory):
    FACTORY_TUNABLES = {
        'example': TunableTuple(
            description="Example tuning",
            value=10
        )
    }

    def __call__(self):
        return self.example.value


custom_interaction = CustomInteraction.TunableFactory()
mod_instance = MyMod()
print("My mod value:", mod_instance())
