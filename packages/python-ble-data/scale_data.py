import asyncio
from etekcity_esf551_ble import (
    IMPEDANCE_KEY,
    WEIGHT_KEY,
    EtekcitySmartFitnessScale,
    ScaleData,
    WeightUnit,
    BodyMetrics,
    Sex,
)

ADDRESS = "D0:4D:00:07:5E:39"

async def main():
    def notification_callback(data: ScaleData):
        print(f"Weight: {data.measurements[WEIGHT_KEY]} kg")
        print(f"Display Unit: {data.display_unit.name}")
        if IMPEDANCE_KEY in data.measurements:
            print(f"Impedance: {data.measurements[IMPEDANCE_KEY]} Ω")
            
            # Calculate body metrics
            # Note: Replace with your actual height, age and sex
            body_metrics = BodyMetrics(
                weight_kg=data.measurements[WEIGHT_KEY],
                height_m=1.85,  # Example height
                age=32,  # Example age
                sex=Sex.Male,  # Example sex
                impedance=data.measurements[IMPEDANCE_KEY]
            )
            print(f"Body Mass Index: {body_metrics.body_mass_index:.2f}")
            print(f"Body Fat Percentage: {body_metrics.body_fat_percentage:.1f}%")
            print(f"Fat-Free Weight: {body_metrics.fat_free_weight:.2f} kg")
            print(f"Subcutaneous Fat Percentage: {body_metrics.subcutaneous_fat_percentage:.1f}%")
            print(f"Visceral Fat Value: {body_metrics.visceral_fat_value}")
            print(f"Body Water Percentage: {body_metrics.body_water_percentage:.1f}%")
            print(f"Basal Metabolic Rate: {body_metrics.basal_metabolic_rate} calories")
            print(f"Skeletal Muscle Percentage: {body_metrics.skeletal_muscle_percentage:.1f}%")
            print(f"Muscle Mass: {body_metrics.muscle_mass:.2f} kg")
            print(f"Bone Mass: {body_metrics.bone_mass:.2f} kg")
            print(f"Protein Percentage: {body_metrics.protein_percentage:.1f}%")
            print(f"Metabolic Age: {body_metrics.metabolic_age} years")

    # Replace XX:XX:XX:XX:XX:XX with your scale's Bluetooth address
    scale = EtekcitySmartFitnessScale(ADDRESS, notification_callback)
    scale.display_unit = WeightUnit.KG  # Set display unit to kilograms

    await scale.async_start()
    await asyncio.sleep(30)  # Wait for measurements
    await scale.async_stop()

asyncio.run(main())