import pandas as pd
import os

def load_and_transform_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    
    # Basic cleaning
    df = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df.shape}")
    
    # Feature engineering
    df['total_device_hours'] = (df['phone_usage_hours'] + 
                               df['laptop_usage_hours'] + 
                               df['tablet_usage_hours'] + 
                               df['tv_usage_hours'])
    
    # Wellness index on scale of 0-100
    df['wellness_index'] = (
        (df['sleep_quality'] / 10 * 30) + 
        (df['physical_activity_hours_per_week'] / 10 * 30) + 
        ((10 - df['stress_level']) / 10 * 20) + 
        (df['mindfulness_minutes_per_day'] / 30 * 20)
    ).clip(0, 100)  # Ensure values stay within 0-100
    
    # Create age groups to help with visuals
    df['age_group'] = pd.cut(df['age'], 
                            bins=[0, 25, 35, 50, 100], 
                            labels=['18-25', '26-35', '36-50', '50+'])
    
    print(f"Transformation complete with {len(df.columns)} columns")
    return df
    

def save_transformed_data(df, output_path):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # saves to csv
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")

if __name__ == "__main__":
    # this allows the script to be run directly for testing
    transformed_df = load_and_transform_data('data/digital_diet_mental_health.csv')
    save_transformed_data(transformed_df, 'data/processed/transformed_digital_diet_data.csv')