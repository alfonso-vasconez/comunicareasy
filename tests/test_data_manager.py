import json
from pathlib import Path
from models.data_manager import DataManager

def test_data_manager_creates_config_if_missing(tmp_path):
    """
    Prueba que el DataManager crea un archivo config.json nuevo 
    a partir del ejemplo si este no existe. Utiliza 'tmp_path' 
    para no afectar los archivos reales del proyecto.
    """
    fake_example = tmp_path / "config.example.json"
    fake_config = tmp_path / "config.json"
    
    sample_data = {
        "current_patient_id": "person1",
        "patients": [{"id": "person1", "name": "Juan Pérez", "routines": []}]
    }
    fake_example.write_text(json.dumps(sample_data), encoding="utf-8")
    
    # Comprobamos que el archivo de configuración operativo no existe inicialmente
    assert not fake_config.exists()
    
    # Instanciamos el DataManager con las rutas temporales
    manager = DataManager(config_path=fake_config, example_path=fake_example)
    
    # Validamos que se haya creado automáticamente
    assert fake_config.exists()
    
    # Validamos que lea correctamente los datos
    patient = manager.get_current_patient()
    assert patient["name"] == "Juan Pérez"