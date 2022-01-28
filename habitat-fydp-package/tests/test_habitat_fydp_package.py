from habitat_fydp_package import __version__
from habitat_fydp_package import list_station_measurment_types

def test_version():
    assert __version__ == '0.0.1'

def test_list_station_measurment_types():
    station = 'Toledo Pump Station'
    result = list_station_measurment_types(station)
    assert result == {'body_of_water': 'lake-erie', 'obs_dataset_id': 23, 'org_platform_id': 'TOLLSPS', 'parameters': [{'name_vocabulary': 'cf', 'standard_name': 'sea_water_electrical_conductivity'}, {'name_vocabulary': 'glos', 'standard_name': 'oxidation_reduction_potential'}, {'name_vocabulary': 'cf', 'standard_name': 'sea_water_ph_reported_on_total_scale'}, {'name_vocabulary': 'glos', 'standard_name': 'mass_concentration_of_blue_green_algae_in_sea_water_rfu'}, {'name_vocabulary': 'cf', 'standard_name': 'sea_surface_temperature'}, {'name_vocabulary': 'ioos', 'standard_name': 'chlorophyll_fluorescence'}, {'name_vocabulary': 'cf', 'standard_name': 'sea_water_turbidity'}, {'name_vocabulary': 'glos', 'standard_name': 'concentration_of_fluorescent_dissolved_organic_matter_rfu'}], 'platform_event': 'activated', 'platform_name': 'Toledo Pump Station', 'platform_type': 'fixed'}