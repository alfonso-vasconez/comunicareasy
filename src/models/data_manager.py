import json
from pathlib import Path

class DataManager:
    def __init__(self, config_path=None, example_path=None):
        # Directorio absoluto donde vive este archivo (models/)
        base_dir = Path(__file__).resolve().parent
        
        # Rutas absolutas seguras
        self.config_path = Path(config_path) if config_path else base_dir / "config.json"
        self.example_path = Path(example_path) if example_path else base_dir / "config.example.json"
        
        self.data = self.load_data()

    def load_data(self) -> dict:
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
        current_id = self.data.get("current_patient_id")
        patients = self.data.get("patients", [])
        
        if not patients:
            return {}
            
        for patient in patients:
            if patient.get("id") == current_id:
                return patient
                
        return patients[0]

    def get_routines(self) -> list:
        patient = self.get_current_patient()
        return patient.get("routines", [])

    def get_categories_for_routine(self, routine_id: str) -> list:
        routines = self.get_routines()
        for routine in routines:
            if routine.get("id") == routine_id:
                return routine.get("categories", [])
        return []