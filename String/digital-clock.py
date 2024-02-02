def convert_to_digital_clock(minutes):
    # Calculate hours and minutes
    hours = minutes // 60
    minutes %= 60
    
    # Format the time as a string
    time_str = f"{hours:02d}:{minutes:02d}"
    
    return time_str

# Example usage
input_minutes = 1180
output_time = convert_to_digital_clock(input_minutes)
print(output_time)
