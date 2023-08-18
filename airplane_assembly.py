#  check if the fuselage is ready for port and starboard attachment
# attach port wing
# attach starboard wing
class Fuselage:
    def __init__(self):
        self.is_clean = False
        self.fuselage_arrived = False
        self.port_wing_attached = False
        self.starboard_wing_attached = False
        self.star_bolt_pattern = 0
        self.bolts_used = 0
        self.engine_attached = 0

    def clean(self):
        self.is_clean = True

    def fuselage_arrival_to_factory(self):
        self.fuselage_arrived = True

    def attach_engine(self):
        self.attach_engine = True

    def is_ready_for_attachment(self):
        if not self.is_clean:
            return False, "Fuselage is not clean"
        if not self.fuselage_arrived:
            return False, "Fuselage is not in the factory for attachment"

    def attach_port_wing_to_fuselage(self, pattern):
        self.star_bolt_pattern = len(pattern)
        if self.star_bolt_pattern != 5:
            return False
        for key, value in pattern.items():
            print(f"{key} -> {value}")

        self.port_wing_attached = True
        return True


    def attach_starbord_wing_to_fuselage(self, pattern):
        self.star_bolt_pattern = len(pattern)
        if self.star_bolt_pattern != 5:
            return False
        for key, value in pattern.items():
            print(f"{key} -> {value}")

        self.port_wing_attached = True
        return True

    def attach_engines_to_wing(self):
        if not self.port_wing_attached or not self.starboard_wing_attached:
            return False, "Port wing must be attached before attaching engines"

        self.engine_attached = 2
        return True, "Port and Starboard wing must be attached before attaching"








