import schemes_templates

class schemes:

    def __init__(self) -> None:
        pass

    def create_vehicle_scheme(self):
        new_vehicle = schemes_templates.vehicle()
        return new_vehicle

    def create_position_scheme(self):
        new_position = schemes_templates.position()
        return new_position
    
    def create_response_scheme(self):
        new_response = schemes_templates.response()
        return new_response
    
    def create_status_scheme(self):
        new_status = schemes_templates.status()
        return new_status