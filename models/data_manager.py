import json
from pathlib import Path

class DataManager:
    def __init__(self, config_path="models/config.json", example_path="models/config.example.json"):
        self.config_path = Path(config_path)
        self.example_path = Path(example_path)
        self.data = self.load_data()

    def load_data(self) -> dict:
        """
        Verifica si existe el archivo de configuración local. 
        Si no existe, lo crea copiando la plantilla de ejemplo.
        """
        if not self.config_path.exists():
            if self.example_path.exists():
                example_data = json.loads(self.example_path.read_text(encoding="utf-8"))
                self.config_path.write_text(
                    json.dumps(example_data, ensure_ascii=False, indent=4), 
                    encoding="utf-8"
                )
            else:
                raise FileNotFoundError(
                    f"No se encontró el archivo de ejemplo en la ruta: {self.example_path}"
                )

        return json.loads(self.config_path.read_text(encoding="utf-8"))

    def get_current_patient(self) -> dict:
        """Devuelve el diccionario del paciente activo de forma segura."""
        current_id = self.data.get("current_patient_id")
        patients = self.data.get("patients", [])
        
        if not patients:
            return {}
            
        for patient in patients:
            if patient.get("id") == current_id:
                return patient
                
        return patients[0]

    def get_routines(self) -> list:
        """Devuelve las rutinas del paciente activo."""
        patient = self.get_current_patient()
        return patient.get("routines", [])

    def get_categories_for_routine(self, routine_id: str) -> list:
        """Devuelve las categorías (pestañas) de una rutina específica."""
        routines = self.get_routines()
        for routine in routines:
            if routine.get("id") == routine_id:
                return routine.get("categories", [])
        return []