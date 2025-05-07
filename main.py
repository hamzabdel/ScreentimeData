import pandas as pd

df = pd.read_csv('digital_diet_mental_health.csv')

df = df.drop_duplicates()
df['total_device_hours'] = df['phone_usage_hours'] + df['laptop_usage_hours'] + df['tablet_usage_hours'] + df['tv_usage_hours']

#wellness index on scale of 0-100
df['wellness_index'] = (
    (df['sleep_quality'] / 10 * 30) + 
    (df['physical_activity_hours_per_week'] / 10 * 30) + 
    ((10 - df['stress_level']) / 10 * 20) + 
    (df['mindfulness_minutes_per_day'] / 30 * 20)
)

#creates age groups to help with visuals
df['age_group'] = pd.cut(df['age'], bins=[0,25,35,50,100], labels=['18-25', '26-35', '36-50', '50+'])

print(df.columns)
