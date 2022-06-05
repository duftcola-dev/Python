queries = {
    "select_posiciones" : "SELECT * FROM posiciones",
    "select_by_matricula":"SELECT * FROM vehiculo WHERE matricula = '{}' LIMIT 1",
    "select_all_vehicles":"SELECT * FROM vehiculo",
    "select_by_speed" :"SELECT id_vehiculo FROM posiciones WHERE velocidad > 10",
    "update_state_to_1":"UPDATE vehiculo SET id_estado = %s WHERE matricula = %s"
}