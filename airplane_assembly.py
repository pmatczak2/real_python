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

    def clean(self):
        self.is_clean = True

    def fuselage_arrival_to_factory(self):
        self.fuselage_arrived = True

    def is_ready_for_attachment(self):
        if not self.is_clean:
            return False, "Fuselage is not clean"
        if not self.fuselage_arrived:
            return False, "Fuselage is not in the factory for attachment"

    def attach_port_wing_to_fuselage(self, bolts):
        self.bolts_used = len(bolts)
        if self.bolts_used == 5:
            self.port_wing_attached = True
            return True
        else:
            return False


    def attach_starbord_wing_to_fuselage(self,bolt):
        self.bolts = len(bolt)
        if self.bolts == 5:
            self.starboard_wing_attached = True
            return True
        else:
            return False

    def bolt_using_star_pattern(self, pattern):
        self.star_bolt_pattern = len(pattern)
        if self.star_bolt_pattern != 5:
            return False
        for key, value in pattern.items():
            print(f"{key} -> {value}")

        return True





